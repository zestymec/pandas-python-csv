import os
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
    "units": "metric"
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/weather",
    params=params
)

print(response.status_code)

data = response.json()

print(data)