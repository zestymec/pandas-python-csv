from datetime import datetime, timedelta
import requests_cache
from data_manager import DataManager
from flight_search import FlightSearch

# Cache install karein taake API credits zaya na hon
requests_cache.install_cache("flight_cache", expire_after=86400)

ORIGIN_CITY_IATA = "LHE" 

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
six_months_later = datetime.now() + timedelta(days=30)

# Pehle sirf pehli city (e.g. Tokyo HND) test karein
first_city = sheet_data[0]
raw_flights = flight_search.check_flights(
    origin_city_code=ORIGIN_CITY_IATA,
    destination_city_code=first_city["iataCode"],
    from_time=tomorrow,
    to_time=six_months_later,
)

print(raw_flights)