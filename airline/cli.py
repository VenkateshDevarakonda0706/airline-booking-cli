import argparse

from sample_data import create_sample_flights

from .booking import BookingManager
from .exceptions import AirlineBookingError
from .models import Passenger
from .report import display_booking, display_bookings, display_flights
from .search import FlightSearch
from .transaction import BookingTransaction


def create_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""

    parser = argparse.ArgumentParser(
        description="Airline booking command-line application."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    search_parser = subparsers.add_parser(
        "search",
        help="Search for flights.",
    )

    search_parser.add_argument(
        "--source",
        help="Departure airport code.",
    )

    search_parser.add_argument(
        "--destination",
        help="Arrival airport code.",
    )

    search_parser.add_argument(
        "--max-price",
        type=float,
        help="Maximum ticket price.",
    )

    book_parser = subparsers.add_parser(
        "book",
        help="Book a flight.",
    )

    book_parser.add_argument(
        "--flight",
        required=True,
        help="Flight number.",
    )

    book_parser.add_argument(
        "--name",
        required=True,
        help="Passenger name.",
    )

    book_parser.add_argument(
        "--age",
        required=True,
        type=int,
        help="Passenger age.",
    )

    book_parser.add_argument(
        "--seat",
        required=True,
        help="Seat number such as 12A.",
    )

    cancel_parser = subparsers.add_parser(
        "cancel",
        help="Cancel a booking.",
    )

    cancel_parser.add_argument(
        "--booking",
        required=True,
        help="Booking ID.",
    )

    cancel_parser.add_argument(
        "--reason",
        default="Cancelled by passenger",
        help="Reason for cancellation.",
    )

    subparsers.add_parser(
        "list-bookings",
        help="Display all bookings.",
    )

    return parser


def handle_search(
    flight_search: FlightSearch,
    args: argparse.Namespace,
) -> None:
    """Handle the search command."""

    if args.source and args.destination:
        flights = flight_search.find_by_route(
            args.source,
            args.destination,
        )
    else:
        flights = list(flight_search.available_flights())

    if args.max_price is not None:
        flights = [flight for flight in flights if flight.price <= args.max_price]

    display_flights(flights)


def handle_booking(
    booking_manager: BookingManager,
    args: argparse.Namespace,
) -> None:
    """Handle the booking command."""

    passenger = Passenger(
        name=args.name,
        age=args.age,
    )

    with BookingTransaction(booking_manager) as booking_transaction:
        booking = booking_transaction.book(
            flight_number=args.flight,
            passenger=passenger,
            seat_number=args.seat,
        )

    display_booking(booking)


def handle_cancellation(
    booking_manager: BookingManager,
    args: argparse.Namespace,
) -> None:
    """Handle the cancellation command."""

    booking = booking_manager.cancel_booking(
        booking_id=args.booking,
        reason=args.reason,
    )

    display_booking(booking)


def handle_list_bookings(
    booking_manager: BookingManager,
) -> None:
    """Handle the list-bookings command."""

    display_bookings(booking_manager.list_bookings())


def main() -> None:
    """Run the airline booking CLI."""

    parser = create_parser()
    args = parser.parse_args()

    flights = create_sample_flights()

    flight_search = FlightSearch(flights)
    booking_manager = BookingManager(flights)

    try:
        if args.command == "search":
            handle_search(flight_search, args)

        elif args.command == "book":
            handle_booking(booking_manager, args)

        elif args.command == "cancel":
            handle_cancellation(booking_manager, args)

        elif args.command == "list-bookings":
            handle_list_bookings(booking_manager)

    except AirlineBookingError as exc:
        print(f"Error: {exc}")
