print("""In Day 47, you are building an Automated Amazon Price Tracker—a Python bot that watches a product on Amazon and emails you the moment its price drops below your target budget.

Here is the simple breakdown of each step:

345. Day 47 Goal
Pick any item you want to buy on Amazon, set your target price (e.g., $100), and write a Python script that checks the live price and sends you an email alert when it gets cheap enough to buy.

346. Step 1 — Scrape the Product Price (BeautifulSoup)
Use requests.get() to download the product's HTML page (the course starts with a static practice page first so you can test easily).

Use BeautifulSoup to locate the HTML tag holding the price (usually inside a <span> with a class like a-price-whole and a-price-fraction).

Clean up the text (remove the $ sign and commas) and convert it into a Python float (e.g., 99.99) so you can compare numbers.

347. Step 2 — Send an Email Alert (smtplib)
Write a simple if condition: if current_price < TARGET_PRICE:

Use Python's smtplib (just like you did in your Flight Deal Finder) to send yourself an email containing the product name, current low price, and the Amazon link.

348. Step 3 — Add HTTP Headers (User-Agent & Accept-Language)
If a Python script visits Amazon with no extra info, Amazon immediately detects it's a bot and blocks it with a CAPTCHA.

To look like a real human browsing from Chrome/Safari, you pass a headers={...} dictionary inside requests.get(url, headers=headers) containing your User-Agent (your browser/OS info) and Accept-Language (e.g., en-US,en;q=0.9).

349. Step 4 — Scrape the Live Amazon Site
Swap out the static practice URL for a real, live Amazon product URL.

Run your script with the headers attached, verify it pulls the real-time price, and confirm your email alert triggers properly.

Optional Copilot Prompt (If You Want Copilot to Generate It)
Build a simple Python Amazon Price Tracker using requests, BeautifulSoup, smtplib, and python-dotenv. Fetch a live Amazon product URL using realistic User-Agent and Accept-Language headers, parse the product title and price as a float, and send an email alert via Gmail SMTP if the price drops below a target threshold. Load email credentials from .env. dil apna purana papi hay barso se namai bna na ska""")
name = input("whats your name")
print(name)