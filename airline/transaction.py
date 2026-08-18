from .booking import BookingManager
from .models import Booking, Passenger


class BookingTransaction:
    """Manage booking operations with commit and rollback behavior."""

    def __init__(self, booking_manager: BookingManager) -> None:
        self.booking_manager = booking_manager

        self._bookings_snapshot: dict[str, Booking] = {}

        self._seat_snapshot: dict[str, int] = {}

    def __enter__(self) -> "BookingTransaction":
        """Save the current booking state before the transaction starts."""

        self._bookings_snapshot = self.booking_manager.bookings.copy()

        self._seat_snapshot = {
            flight_number: flight.available_seats
            for flight_number, flight in self.booking_manager.flights.items()
        }

        return self

    def book(
        self,
        flight_number: str,
        passenger: Passenger,
        seat_number: str,
    ) -> Booking:
        """Create a booking inside the transaction."""

        return self.booking_manager.create_booking(
            flight_number,
            passenger,
            seat_number,
        )

    def __exit__(
        self,
        exception_type: type[BaseException] | None,
        exception_value: BaseException | None,
        traceback: object | None,
    ) -> bool:
        """Commit successful transactions or rollback failed transactions."""

        if exception_type is not None:
            self.booking_manager.bookings = self._bookings_snapshot

            for flight_number, available_seats in self._seat_snapshot.items():
                self.booking_manager.flights[flight_number].available_seats = (
                    available_seats
                )

            print("[transaction] Rollback completed.")

            return False

        print("[transaction] Commit completed.")

        return False
