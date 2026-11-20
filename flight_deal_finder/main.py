from datetime import datetime, timedelta
import requests_cache
from data_manager import DataManager
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager

requests_cache.install_cache("flight_cache", expire_after=86400)

ORIGIN_CITY_IATA = "LHE"


def run():
    data_manager = DataManager()
    flight_search = FlightSearch()

    sheet_data = data_manager.get_destination_data()
    tomorrow = datetime.now() + timedelta(days=1)
    six_months_later = tomorrow + timedelta(days=180)

    for destination in sheet_data:
        destination_code = destination.get("iataCode")
        lowest_price = destination.get("lowestPrice")
        if not destination_code or lowest_price is None:
            raise ValueError(
                "Each Sheety row must contain 'iataCode' and 'lowestPrice'."
            )

        raw_flights = flight_search.check_flights(
            origin_city_code=ORIGIN_CITY_IATA,
            destination_city_code=destination_code,
            from_time=tomorrow,
            to_time=six_months_later,
        )
        cheapest_flight = find_cheapest_flight(raw_flights)
        if cheapest_flight is None:
            print(f"No flights found for {destination_code}.")
            continue

        if cheapest_flight.price < float(lowest_price):
            message = (
                f"Low price flight found: "
                f"{cheapest_flight.origin_airport} to "
                f"{cheapest_flight.destination_airport}, "
                f"${cheapest_flight.price}, "
                f"{cheapest_flight.out_date} to {cheapest_flight.return_date}."
            )
            NotificationManager().send_email(message)
            print(message)
        else:
            print(
                f"No lower price found for {destination_code}. "
                f"Best price: ${cheapest_flight.price}."
            )


if __name__ == "__main__":
    run()
