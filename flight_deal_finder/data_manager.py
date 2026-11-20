import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:

    def __init__(self):
        self.sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
        if not self.sheety_endpoint:
            raise RuntimeError("Set SHEETY_ENDPOINT before running.")
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.sheety_endpoint, timeout=30)
        response.raise_for_status()
        try:
            payload = response.json()
        except ValueError as error:
            raise RuntimeError(
                "SHEETY_ENDPOINT returned a non-JSON response. "
                "Check that it is the Sheety API endpoint."
            ) from error

        prices = payload.get("prices")
        if prices is None and isinstance(payload, dict):
            list_values = [
                value
                for value in payload.values()
                if isinstance(value, list)
            ]
            if len(list_values) == 1:
                prices = list_values[0]
        if not isinstance(prices, list):
            keys = (
                ", ".join(payload)
                if isinstance(payload, dict)
                else type(payload).__name__
            )
            detail = payload.get("error") if isinstance(payload, dict) else None
            raise RuntimeError(
                "SHEETY_ENDPOINT did not return a destination list. "
                f"Response keys/type: {keys}. "
                f"API detail: {detail or 'not provided'}. "
                "Use the Sheety endpoint for the worksheet's API JSON."
            )

        self.destination_data = prices
        return self.destination_data