from dataclasses import dataclass
from datetime import datetime
from .exceptions import InvalidPassengerError


@dataclass(slots=True)
class Flight:
    """Represents an available airline flight."""

    flight_number: str
    source: str
    destination: str
    departure_time: datetime
    price: float
    total_seats: int
    available_seats: int

    def __str__(self) -> str:
        return (
            f"Flight {self.flight_number}: {self.source} to {self.destination} | "
            f"{self.departure_time:%Y-%m-%d %H:%M} | Price: {self.price: .2f} | "
            f"Seats Available: {self.available_seats}/{self.total_seats}"
        )

    def __lt__(self, other: "Flight") -> bool:
        """Compare flights by ticket price."""
        if not isinstance(other, Flight):
            return NotImplemented
        return self.price < other.price


@dataclass(frozen=True, slots=True)
class Passenger:
    """Represent a passenger."""

    name: str
    age: int

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise InvalidPassengerError("Passenger name cannot be empty.")

        if self.age < 0:
            raise InvalidPassengerError("Passenger age cannot be negative.")


@dataclass(slots=True)
class Booking:
    """Represents a confirmed flight booking."""

    booking_id: str
    passenger: Passenger
    flight: Flight
    seat_number: str
    cancellation_status: bool = False
    cancellation_reason: str | None = None

    def cancel(self, reason: str = "Cancelled by passenger") -> None:
        "Cancelling the booking."
        if self.cancellation_status:
            raise ValueError("Booking is already cancelled.")

        self.cancellation_status = True
        self.cancellation_reason = reason

    def __str__(self) -> str:
        status = "Cancelled" if self.cancellation_status else "Confirmed"

        return (
            f"Booking ID: {self.booking_id} | Passenger: {self.passenger.name} | "
            f"Flight: {self.flight.flight_number} | Seat: {self.seat_number} | "
            f"Status: {status}"
        )
