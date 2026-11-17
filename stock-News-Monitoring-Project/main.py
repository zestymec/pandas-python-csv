import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

import requests
from dotenv import load_dotenv


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

PROJECT_FOLDER = Path(__file__).resolve().parent
load_dotenv(PROJECT_FOLDER / ".env")


def get_required_setting(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Set {name} in stock News-Monitoring-Project/.env")
    return value


# STEP 1: Get the stock prices from Alpha Vantage.
alpha_vantage_key = get_required_setting("ALPHA_VANTAGE_API_KEY")

stock_response = requests.get(
    "https://www.alphavantage.co/query",
    params={
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": alpha_vantage_key,
    },
)
stock_response.raise_for_status()
stock_data = stock_response.json()

if "Time Series (Daily)" not in stock_data:
    raise RuntimeError(f"Alpha Vantage response did not contain stock prices: {stock_data}")

daily_prices = stock_data["Time Series (Daily)"]
latest_two_days = list(daily_prices.items())[:2]
if len(latest_two_days) < 2:
    raise RuntimeError("Alpha Vantage did not return two trading days.")

latest_close = float(latest_two_days[0][1]["4. close"])
previous_close = float(latest_two_days[1][1]["4. close"])
percentage_change = ((latest_close - previous_close) / previous_close) * 100

print(f"{STOCK} changed by {percentage_change:.2f}%")


# STEP 2: If the change is 5% or more, get the first 3 news articles.
if abs(percentage_change) >= 2:
    news_api_key = get_required_setting("NEWS_API_KEY")

    news_response = requests.get(
        "https://newsapi.org/v2/everything",
        params={
            "q": COMPANY_NAME,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 3,
            "apiKey": news_api_key,
        },
    )
    news_response.raise_for_status()
    news_data = news_response.json()

    if news_data.get("status") != "ok":
        raise RuntimeError(f"NewsAPI request failed: {news_data}")

    articles = news_data.get("articles", [])[:3]
    if not articles:
        raise RuntimeError(f"No news articles were found for {COMPANY_NAME}.")

    # STEP 3: Send the stock change and news to MAIL_RECIPIENT.
    sender = get_required_setting("MAIL_SENDER")
    mail_password = get_required_setting("MAIL_PASSWORD")
    recipient = get_required_setting("MAIL_RECIPIENT")

    direction = "increased" if percentage_change > 0 else "decreased"
    email_lines = [
        f"{STOCK} {direction} by {abs(percentage_change):.2f}%.",
        f"News about {COMPANY_NAME}:",
        "",
    ]

    for number, article in enumerate(articles, start=1):
        email_lines.extend(
            [
                f"{number}. {article.get('title', 'No title')}",
                f"Brief: {article.get('description') or 'No description available.'}",
                f"Link: {article.get('url', 'No link available.')}",
                "",
            ]
        )

    message = EmailMessage()
    message["Subject"] = f"{STOCK} stock news alert"
    message["From"] = sender
    message["To"] = recipient
    message.set_content("\n".join(email_lines))

    # Google Workspace SMTP: use a Gmail/Workspace App Password.
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(sender, mail_password)
        connection.send_message(message)

    print(f"News email sent to {recipient}")
else:
    print("The change is less than 2%, so no news email was sent.")
