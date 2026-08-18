from collections.abc import Iterable

from .models import Booking, Flight


def display_flights(flights: Iterable[Flight]) -> None:
    """Display a list of available flights."""

    flights = list(flights)

    if not flights:
        print("No flights found.")
        return

    print("\nAvailable Flights")
    print("-" * 70)

    for flight in flights:
        print(flight)


def display_bookings(bookings: Iterable[Booking]) -> None:
    """Display all bookings."""

    bookings = list(bookings)

    if not bookings:
        print("No bookings found.")
        return

    print("\nBookings")
    print("-" * 70)

    for booking in bookings:
        print(booking)


def display_booking(booking: Booking) -> None:
    """Display one booking."""

    print("\nBooking Details")
    print("-" * 70)
    print(booking)
