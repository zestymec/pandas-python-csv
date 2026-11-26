import os
import re
import smtplib
from email.message import EmailMessage
from pathlib import Path
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

MAIL_SENDER = os.getenv("MAIL_SENDER") or os.getenv("EMAIL_ADDRESS")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD") or os.getenv("EMAIL_PASSWORD")
MAIL_RECIPIENT = os.getenv("MAIL_RECIPIENT") or os.getenv("RECIPIENT_EMAIL") or MAIL_SENDER
TARGET_PRICE = float(os.getenv("TARGET_PRICE", "100.00"))

DEFAULT_URL = "https://www.amazon.com/dp/B075CYMYK6"
PRODUCT_URL = os.getenv("PRODUCT_URL", DEFAULT_URL)

REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}


def get_amazon_product_details(url: str):
    print(f"Fetching product data from: {url}")
    response = requests.get(url, headers=REQUEST_HEADERS, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    if "Robot Check" in soup.text or "Type the characters you see in this image" in soup.text:
        raise RuntimeError("Amazon CAPTCHA detected. Try using updated headers or rotating proxies.")

    title_element = soup.find(id="productTitle")
    if not title_element:
        title_element = soup.select_one("h1 span") or soup.select_one("#title")

    if not title_element:
        raise ValueError("Could not find product title on the page.")

    title = " ".join(title_element.get_text().split())

    price = None

    price_span = soup.select_one(".a-price .a-offscreen")
    if price_span:
        raw_price = price_span.get_text().strip()
        price = _extract_price_float(raw_price)

    if price is None:
        whole = soup.select_one(".a-price-whole")
        fraction = soup.select_one(".a-price-fraction")
        if whole:
            fraction_text = fraction.get_text().strip() if fraction else "00"
            clean_whole = whole.get_text().replace(",", "").replace(".", "").strip()
            try:
                price = float(f"{clean_whole}.{fraction_text}")
            except ValueError:
                pass

    if price is None:
        for selector in ["#priceblock_ourprice", "#priceblock_dealprice", "#priceblock_saleprice", ".priceToPay span"]:
            element = soup.select_one(selector)
            if element:
                extracted = _extract_price_float(element.get_text().strip())
                if extracted is not None:
                    price = extracted
                    break

    if price is None:
        raise ValueError("Could not extract price from the product page.")

    return title, price


def _extract_price_float(price_str: str):
    match = re.search(r"([0-9]{1,3}(?:,[0-9]{3})*(?:\.[0-9]+)?)", price_str)
    if match:
        clean_num = match.group(1).replace(",", "")
        try:
            return float(clean_num)
        except ValueError:
            return None
    return None


def send_price_alert(title: str, current_price: float, target_price: float, product_url: str):
    if not MAIL_SENDER or not MAIL_PASSWORD:
        print("[WARNING] Gmail credentials not configured in .env. Skipping email dispatch.")
        print("Please set MAIL_SENDER and MAIL_PASSWORD in your .env file.")
        return False

    msg = EmailMessage()
    msg["Subject"] = f"Amazon Price Alert: Price dropped to ${current_price:.2f}!"
    msg["From"] = MAIL_SENDER
    msg["To"] = MAIL_RECIPIENT

    body_content = (
        f"Good news! The price for the item you are tracking has dropped below your target.\n\n"
        f"Product: {title}\n"
        f"Current Price: ${current_price:.2f}\n"
        f"Target Price: ${target_price:.2f}\n\n"
        f"Buy it now here:\n{product_url}\n"
    )
    msg.set_content(body_content)

    print("Connecting to Gmail SMTP server (smtp.gmail.com:587)...")
    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=20) as server:
        server.starttls()
        server.login(user=MAIL_SENDER, password=MAIL_PASSWORD)
        server.send_message(msg)

    print(f"[SUCCESS] Email alert sent to {MAIL_RECIPIENT}!")
    return True


def check_price():
    print("=" * 60)
    print("Amazon Price Tracker Running...")
    print(f"Target Price Threshold: ${TARGET_PRICE:.2f}")
    print("=" * 60)

    try:
        title, current_price = get_amazon_product_details(PRODUCT_URL)
        print(f"\nProduct: {title}")
        print(f"Current Price: ${current_price:.2f}")

        if current_price < TARGET_PRICE:
            print(f"\n[ALERT] Current price (${current_price:.2f}) is below target price (${TARGET_PRICE:.2f})!")
            send_price_alert(title, current_price, TARGET_PRICE, PRODUCT_URL)
        else:
            print(f"\n[INFO] Price (${current_price:.2f}) is above target (${TARGET_PRICE:.2f}). No alert sent.")

    except Exception as e:
        print(f"\n[ERROR] Failed to track price: {e}")


if __name__ == "__main__":
    check_price()
