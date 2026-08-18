from airline.search import FlightSearch
from sample_data import flights


search = FlightSearch(flights)

print("HYD -> DEL")
for flight in search.find_by_route("HYD", "DEL"):
    print(flight)

print("\nFlights under ₹4000")
for flight in search.find_by_max_price(4000):
    print(flight)

print("\nSorted by price")
for flight in search.sort_by_price():
    print(flight)

print("\nAvailable flights")
for flight in search.available_flights():
    print(flight)

print("\nDestinations")
print(search.destinations())

print("\nFlights grouped by source")
for source, source_flights in search.flights_by_source().items():
    print(source, [flight.flight_number for flight in source_flights])