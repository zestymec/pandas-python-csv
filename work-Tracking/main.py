import os
import requests
from datetime import datetime
from pathlib import Path


PROJECT_FOLDER = Path(__file__).resolve().parent
ENV_FILE = PROJECT_FOLDER / ".env"


def load_environment():
    if not ENV_FILE.exists():
        raise RuntimeError("Set the required values in work-Tracking/.env")

    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        name, separator, value = line.partition("=")
        if separator:
            os.environ[name.strip()] = value.strip().strip("\"'")


def get_required_setting(name):
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Set {name} in work-Tracking/.env")
    return value


load_environment()

GENDER = get_required_setting("GENDER")
WEIGHT_KG = int(get_required_setting("WEIGHT_KG"))
HEIGHT_CM = int(get_required_setting("HEIGHT_CM"))
AGE = int(get_required_setting("AGE"))

APP_ID = get_required_setting("APP_ID")
API_KEY = get_required_setting("API_KEY")

exercise_endpoint = get_required_setting("EXERCISE_ENDPOINT")
sheet_endpoint = get_required_setting("SHEET_ENDPOINT")
sheet_username = get_required_setting("SHEET_USERNAME")
sheet_password = get_required_setting("SHEET_PASSWORD")

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(sheet_username, sheet_password),
    )
    sheet_response.raise_for_status()
    print(sheet_response.text)