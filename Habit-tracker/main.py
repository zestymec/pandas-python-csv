import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

today = datetime.now()
username = os.getenv("PIXELA_USERNAME")
token = os.getenv("PIXELA_TOKEN")
if not username or not token:
    raise RuntimeError("Set PIXELA_USERNAME and PIXELA_TOKEN before running.")

pixela_endpoint = "https://pixe.la/v1/users"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
headers = {"X-USER-TOKEN": token}
graph_url = f"{pixela_endpoint}/{username}/graphs/{graph_config['id']}.html"
print(f"Graph URL: {graph_url}")

delete_endpoint = (
    f"{pixela_endpoint}/{username}/graphs/{graph_config['id']}/"
    f"{today.strftime('%Y%m%d')}"
)
response = requests.delete(delete_endpoint, headers=headers, timeout=30)
response.raise_for_status()
print("Pixel deleted!")
