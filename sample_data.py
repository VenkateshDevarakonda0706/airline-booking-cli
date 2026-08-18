from datetime import datetime

from airline.models import Flight


flights = [
    Flight(
        "AI101",
        "HYD",
        "DEL",
        datetime(2026, 8, 20, 8, 30),
        4500,
        100,
        10,
    ),
    Flight(
        "AI102",
        "HYD",
        "BLR",
        datetime(2026, 8, 20, 10, 0),
        2800,
        80,
        8,
    ),
    Flight(
        "AI103",
        "HYD",
        "DEL",
        datetime(2026, 8, 20, 14, 0),
        3500,
        120,
        0,
    ),
    Flight(
        "AI104",
        "BLR",
        "MUM",
        datetime(2026, 8, 20, 16, 30),
        3200,
        90,
        15,
    ),
]