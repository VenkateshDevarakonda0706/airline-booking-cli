class AirlineBookingError(Exception):
    """Base exception for the airline booking application."""


class FlightNotFoundError(AirlineBookingError):
    """Raised when a requested flight cannot be found."""


class InvalidPassengerError(AirlineBookingError):
    """Raised when passenger information is invalid."""


class SeatUnavailableError(AirlineBookingError):
    """Raised when a requested seat is unavailable."""


class NoAvailableSeatsError(AirlineBookingError):
    """Raised when a flight has no available seats."""


class BookingNotFoundError(AirlineBookingError):
    """Raised when a booking cannot be found."""


class BookingCancellationError(AirlineBookingError):
    """Raised when a booking cannot be cancelled."""


class InvalidBookingError(AirlineBookingError):
    """Raised when a booking operation contains invalid data."""
