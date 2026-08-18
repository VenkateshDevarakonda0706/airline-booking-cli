from collections.abc import Iterable

from .exceptions import (
    BookingCancellationError,
    BookingNotFoundError,
    FlightNotFoundError,
    NoAvailableSeatsError,
    SeatUnavailableError,
)
from .models import Booking, Flight, Passenger


class BookingManager:
    """Manage flight bookings and cancellations."""

    def __init__(self, flights: Iterable[Flight]) -> None:
        self.flights = {
            flight.flight_number: flight
            for flight in flights
        }
        self.bookings: dict[str, Booking] = {}
        self.booking_counter = 1000

    def _get_flight(self, flight_number: str) -> Flight:
        """Retrieve a flight by its flight number."""
        flight = self.flights.get(flight_number)

        if flight is None:
            raise FlightNotFoundError(
                f"Flight {flight_number} not found."
            )

        return flight

    def _generate_booking_id(self) -> str:
        """Generate a unique booking ID."""
        self.booking_counter += 1
        return f"BK{self.booking_counter}"

    def _validate_seat(
        self,
        flight: Flight,
        seat_number: str,
    ) -> None:
        """Validate that the requested seat can be booked."""

        if flight.available_seats <= 0:
            raise NoAvailableSeatsError(
                f"No available seats on flight {flight.flight_number}."
            )

        if len(seat_number) < 2:
            raise SeatUnavailableError(
                f"Invalid seat number: {seat_number}."
            )

        row_part = seat_number[:-1]
        seat_letter = seat_number[-1]

        if not row_part.isdigit() or seat_letter not in {
            "A",
            "B",
            "C",
            "D",
        }:
            raise SeatUnavailableError(
                f"Invalid seat number: {seat_number}."
            )

        row_number = int(row_part)

        seats_per_row = 4
        max_row = (
            flight.total_seats + seats_per_row - 1
        ) // seats_per_row

        if not 1 <= row_number <= max_row:
            raise SeatUnavailableError(
                f"Seat {seat_number} is unavailable on "
                f"flight {flight.flight_number}."
            )

        occupied_seats = {
            booking.seat_number
            for booking in self.bookings.values()
            if (
                booking.flight.flight_number
                == flight.flight_number
                and not booking.cancellation_status
            )
        }

        if seat_number in occupied_seats:
            raise SeatUnavailableError(
                f"Seat {seat_number} is already booked."
            )

    def create_booking(
        self,
        flight_number: str,
        passenger: Passenger,
        seat_number: str,
    ) -> Booking:
        """Create a booking for a passenger."""

        flight = self._get_flight(flight_number)

        seat_number = seat_number.upper().strip()

        self._validate_seat(
            flight,
            seat_number,
        )

        booking = Booking(
            booking_id=self._generate_booking_id(),
            passenger=passenger,
            flight=flight,
            seat_number=seat_number,
        )

        self.bookings[booking.booking_id] = booking
        flight.available_seats -= 1

        return booking

    def get_booking(self, booking_id: str) -> Booking:
        """Retrieve a booking by its ID."""

        booking = self.bookings.get(booking_id)

        if booking is None:
            raise BookingNotFoundError(
                f"Booking {booking_id} was not found."
            )

        return booking

    def cancel_booking(
        self,
        booking_id: str,
        reason: str = "Cancelled by passenger",
    ) -> Booking:
        """Cancel a booking and release its seat."""

        booking = self.get_booking(booking_id)

        if booking.cancellation_status:
            raise BookingCancellationError(
                f"Unable to cancel booking {booking_id}: "
                "booking is already cancelled."
            )

        try:
            booking.cancel(reason)
        except ValueError as exc:
            raise BookingCancellationError(
                f"Unable to cancel booking {booking_id}."
            ) from exc

        booking.flight.available_seats += 1

        return booking

    def list_bookings(self) -> list[Booking]:
        """Return all bookings."""
        return list(self.bookings.values())