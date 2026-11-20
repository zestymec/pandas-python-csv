import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

api_key = os.getenv("API_KEY")
if not api_key:
    raise RuntimeError("Set API_KEY in day-35/.env")

params = {
    "lat": 31.52,
    "lon": 74.32,
    "appid": api_key,
    "units": "metric",
    "cnt": 4,
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast",
    params=params
)
response.raise_for_status()

weather_data = response.json()

will_rain = any(
    forecast["weather"][0]["id"] < 700
    for forecast in weather_data["list"]
)

conditions = [
    forecast["weather"][0]["description"]
    for forecast in weather_data["list"]
]
weather_summary = ", ".join(conditions)

if will_rain:
    print("Bring umbrella")
    warning = "Rain, snow, or a storm is expected. Bring an umbrella."
else:
    print("No rain expected in the next 12 hours")
    warning = "No rain, snow, or storm is expected."

sender = os.getenv("MAIL_SENDER")
password = os.getenv("MAIL_PASSWORD")
recipient = os.getenv("MAIL_RECIPIENT")
if not sender or not password or not recipient:
    raise RuntimeError(
        "Set MAIL_SENDER, MAIL_PASSWORD, and MAIL_RECIPIENT in sms-sender/.env"
    )

message = EmailMessage()
message["Subject"] = "Weather forecast for the next 12 hours"
message["From"] = sender
message["To"] = recipient
message.set_content(
    f"Weather forecast for the next 12 hours:\n\n"
    f"{weather_summary}\n\n"
    f"{warning}"
)

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(sender, password)
    connection.send_message(message)

print(f"Weather email sent to {recipient}")