class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

def find_cheapest_flight(data):
    """Return the cheapest valid flight in a SerpAPI response."""
    if data is None:
        return None

    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    if not all_flights:
        return None

    valid_flights = [
        flight
        for flight in all_flights
        if flight.get("price") is not None and flight.get("flights")
    ]
    if not valid_flights:
        return None

    cheapest = min(valid_flights, key=lambda flight: flight["price"])
    lowest_price = cheapest.get("price")

    if lowest_price is None:
        return None

    first_leg = cheapest["flights"][0]
    last_leg = cheapest["flights"][-1]

    origin = first_leg["departure_airport"]["id"]
    destination = first_leg["arrival_airport"]["id"]
    out_date = first_leg["departure_airport"]["time"].split()[0]
    return_date = last_leg["departure_airport"]["time"].split()[0]

    return FlightData(
        price=lowest_price,
        origin_airport=origin,
        destination_airport=destination,
        out_date=out_date,
        return_date=return_date,
    )