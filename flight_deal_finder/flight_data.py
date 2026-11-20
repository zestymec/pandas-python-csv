class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date


def find_cheapest_flight(data):
    """SerpAPI ke raw JSON mein se sabse sasti flight nikalta hai."""
    if data is None:
        return None

    # SerpAPI flights ko 'best_flights' aur 'other_flights' do lists mein deta hai
    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    if not all_flights:
        return None

    # Sabse kam 'price' wali flight select karein
    cheapest = min(all_flights, key=lambda x: x.get("price", float("inf")))
    lowest_price = cheapest.get("price")

    if lowest_price is None:
        return None

    # Flight ki details extract karein
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