import os
import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:

    def __init__(self):
        self.sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.sheety_endpoint)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data