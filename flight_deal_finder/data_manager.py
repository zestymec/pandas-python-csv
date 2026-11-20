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
        self.destination_data = response.json()["prices"]
        return self.destination_data