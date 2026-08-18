from datetime import datetime

from airline.models import Flight


def create_sample_flights() -> list[Flight]:
    """Create sample flights for the application."""

    return [
        Flight(
            flight_number="AI101",
            source="HYD",
            destination="DEL",
            departure_time=datetime(2026, 8, 20, 8, 30),
            price=4500.0,
            total_seats=100,
            available_seats=10,
        ),
        Flight(
            flight_number="AI102",
            source="HYD",
            destination="BLR",
            departure_time=datetime(2026, 8, 20, 10, 0),
            price=2800.0,
            total_seats=80,
            available_seats=8,
        ),
        Flight(
            flight_number="AI103",
            source="HYD",
            destination="DEL",
            departure_time=datetime(2026, 8, 20, 14, 0),
            price=3500.0,
            total_seats=120,
            available_seats=0,
        ),
        Flight(
            flight_number="AI104",
            source="BLR",
            destination="MUM",
            departure_time=datetime(2026, 8, 20, 16, 30),
            price=3200.0,
            total_seats=90,
            available_seats=15,
        ),
    ]
