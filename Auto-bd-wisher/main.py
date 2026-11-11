import datetime as dt
import os
import random
import smtplib
from pathlib import Path

from dotenv import load_dotenv


PROJECT_DIR = Path(__file__).resolve().parent
load_dotenv(PROJECT_DIR / ".env")


def send_monday_quote() -> None:
    if dt.datetime.now().weekday() != 0:
        print("Today is not Monday. No email was sent.")
        return

    sender = os.getenv("MAIL_SENDER")
    password = os.getenv("MAIL_PASSWORD")
    recipient = os.getenv("MAIL_RECIPIENT")

    if not sender or not password or not recipient:
        raise RuntimeError(
            "Set MAIL_SENDER, MAIL_PASSWORD, and MAIL_RECIPIENT in .env"
        )

    with (PROJECT_DIR / "quotes.txt").open(encoding="utf-8") as file:
        quote = random.choice(file.readlines()).strip()

    message = f"Subject: Monday Motivation\n\n{quote}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(sender, password)
        connection.sendmail(sender, recipient, message)

    print("Random quote sent successfully.")


if __name__ == "__main__":
    send_monday_quote()
