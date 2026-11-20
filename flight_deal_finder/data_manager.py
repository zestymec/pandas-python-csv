import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:

    def __init__(self):
        self.sheety_endpoint = os.getenv("SHEETY_ENDPOINT")
        if not self.sheety_endpoint:
            raise RuntimeError("Set SHEETY_ENDPOINT before running.")
        self.users_endpoint = os.getenv("SHEETY_USERS_ENDPOINT")
        if not self.users_endpoint:
            raise RuntimeError("Set SHEETY_USERS_ENDPOINT before running.")
        self.destination_data = {}
        self.user_data = []

    def _get_sheet_list(self, endpoint, possible_keys):
        response = requests.get(url=endpoint, timeout=30)
        response.raise_for_status()
        try:
            payload = response.json()
        except ValueError as error:
            raise RuntimeError(
                "SHEETY_ENDPOINT returned a non-JSON response. "
                "Check that it is the Sheety API endpoint."
            ) from error

        rows = None
        if isinstance(payload, dict):
            for key in possible_keys:
                if isinstance(payload.get(key), list):
                    rows = payload[key]
                    break
            if rows is None:
                list_values = [
                    value for value in payload.values()
                    if isinstance(value, list)
                ]
                if len(list_values) == 1:
                    rows = list_values[0]

        if not isinstance(rows, list):
            keys = (
                ", ".join(payload)
                if isinstance(payload, dict)
                else type(payload).__name__
            )
            detail = payload.get("error") if isinstance(payload, dict) else None
            raise RuntimeError(
                "Sheety endpoint did not return a row list. "
                f"Response keys/type: {keys}. "
                f"API detail: {detail or 'not provided'}. "
                "Use the Sheety endpoint for the worksheet's API JSON."
            )
        return rows

    def get_destination_data(self):
        self.destination_data = self._get_sheet_list(
            self.sheety_endpoint,
            ("prices", "destinations"),
        )
        return self.destination_data

    def get_user_emails(self):
        self.user_data = self._get_sheet_list(
            self.users_endpoint,
            ("users", "subscribers"),
        )
        emails = []
        for user in self.user_data:
            email = None
            for key in ("email", "mail", "Email", "Mail"):
                value = user.get(key)
                if isinstance(value, str) and value.strip():
                    email = value.strip()
                    break
            if email and "@" in email:
                emails.append(email)
        return list(dict.fromkeys(emails))