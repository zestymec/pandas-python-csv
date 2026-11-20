import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:

    def __init__(self):
        self.api_key = os.getenv("SERPAPI_KEY")
        if not self.api_key:
            raise RuntimeError("Set SERPAPI_KEY before running.")
        self.endpoint = "https://serpapi.com/search.json"

    def check_flights(
        self, origin_city_code, destination_city_code, from_time, to_time
    ):
        params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "currency": "USD",
            "hl": "en",
            "api_key": self.api_key,
        }

        response = requests.get(url=self.endpoint, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
