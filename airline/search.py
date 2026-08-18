from collections.abc import Generator, Iterable

from .models import Flight


class FlightSearch:
    """Provides search and filtering operations for flights."""

    def __init__(self, flights: Iterable[Flight]) -> None:
        self.flights = list(flights)

    def find_by_route(
        self,
        source: str,
        destination: str,
    ) -> list[Flight]:
        """Returns flights matching the source and destination."""
        return [
            flight
            for flight in self.flights
            if flight.source.lower() == source.lower()
            and flight.destination.lower() == destination.lower()
        ]

    def find_by_max_price(self, max_price: float) -> list[Flight]:
        """Returns flights within the given maximum price."""
        return [
            flight
            for flight in self.flights
            if flight.price <= max_price
        ]

    def sort_by_price(self, descending: bool = False) -> list[Flight]:
        """Returns flights sorted by price."""
        return sorted(
            self.flights,
            key=lambda flight: flight.price,
            reverse=descending,
        )

    def available_flights(self) -> Generator[Flight, None, None]:
        """Yields flights that have available seats."""
        for flight in self.flights:
            if flight.available_seats > 0:
                yield flight

    def destinations(self) -> set[str]:
        """Returns all unique flight destinations."""
        return {flight.destination.upper() for flight in self.flights}

    def flights_by_source(self) -> dict[str, list[Flight]]:
        """Returns a dictionary mapping sources to their flights."""
        flights_by_source: dict[str, list[Flight]] = {}

        for flight in self.flights:
            if flight.source not in flights_by_source:
                flights_by_source[flight.source] = []

            flights_by_source[flight.source].append(flight)

        return flights_by_source