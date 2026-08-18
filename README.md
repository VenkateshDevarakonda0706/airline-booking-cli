# ✈️ Airline Booking CLI

A command-line based **Airline Booking System** built with Python.

This project simulates a real-world airline reservation workflow through a terminal-based interface. Users can search for available flights, view flight details, manage passenger information, book seats, view bookings, and cancel reservations.

The project focuses on building a clean, modular Python application while demonstrating practical concepts such as **Object-Oriented Programming, file handling, input validation, exception handling, CRUD operations, and CLI application design**.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Running the Application](#-running-the-application)
- [Application Workflow](#-application-workflow)
- [Available Operations](#-available-operations)
- [Example Usage](#-example-usage)
- [Data Management](#-data-management)
- [Input Validation](#-input-validation)
- [Error Handling](#-error-handling)
- [Project Design](#-project-design)
- [Testing](#-testing)
- [Learning Objectives](#-learning-objectives)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [License](#-license)

---

# 📖 Project Overview

The **Airline Booking CLI** is a terminal-based airline reservation application.

The system allows users to interact with airline data through a simple command-line interface instead of a graphical or web interface.

The application follows a typical airline booking workflow:

```text
Start Application
       │
       ▼
Display Main Menu
       │
       ├── Search Flights
       │
       ├── View Flight Details
       │
       ├── Book Flight
       │       │
       │       ├── Enter Passenger Details
       │       ├── Validate Input
       │       ├── Check Seat Availability
       │       └── Confirm Booking
       │
       ├── View Bookings
       │
       ├── Cancel Booking
       │
       └── Exit
```

The project is designed to demonstrate how a small real-world application can be structured using Python.

---

# 🚀 Features

## ✈️ Flight Management

- View available flights
- Search flights
- Display flight details
- Check available seats
- View source and destination
- View departure information
- View flight pricing

## 👤 Passenger Management

- Enter passenger details
- Validate passenger information
- Store passenger information
- Associate passengers with bookings

## 🎫 Booking Management

- Create a new booking
- Generate a booking/reference ID
- Check seat availability before booking
- Reduce available seats after successful booking
- View existing bookings
- Cancel bookings
- Restore seat availability after cancellation

## 🧾 Data Management

- Store application data using files/database used by the project
- Read existing records
- Create new records
- Update records
- Delete/cancel records
- Maintain consistent data after operations

## 🛡️ Validation

The application validates user input before processing operations.

Examples include:

- Invalid menu choices
- Invalid flight IDs
- Invalid passenger information
- Invalid booking IDs
- Invalid seat selections
- Empty input
- Incorrect numeric values
- Invalid dates where applicable

## ⚠️ Error Handling

The application handles common runtime and user-input errors without unnecessarily terminating the program.

Examples:

- Invalid user input
- Missing records
- Booking for unavailable flights
- Cancelling a non-existing booking
- Invalid file/data operations
- Insufficient seat availability

---

# 🛠️ Technologies Used

| Technology               | Purpose                                  |
| ------------------------ | ---------------------------------------- |
| Python                   | Core programming language                |
| Python OOP               | Application structure and business logic |
| CLI                      | User interaction                         |
| File Handling / Database | Data persistence                         |
| Exception Handling       | Error management                         |
| Git                      | Version control                          |
| GitHub                   | Source-code hosting                      |

---

# 📂 Project Structure

The project follows a modular structure to keep the application organized and maintainable.

```text
airline-booking-cli/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── flight.py
│   │   ├── passenger.py
│   │   └── booking.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── flight_service.py
│   │   ├── booking_service.py
│   │   └── passenger_service.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── validators.py
│   │   └── helpers.py
│   │
│   └── data/
│       └── ...
│
└── tests/
    ├── ...
```

> The exact files and folders may vary depending on the current implementation.

---

# 💻 Prerequisites

Before running the project, make sure the following are installed:

- Python 3.10 or later
- Git
- A terminal or command prompt

Check your Python installation:

```bash
python --version
```

or:

```bash
py --version
```

Check Git:

```bash
git --version
```

---

# 📥 Installation

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd airline-booking-cli
```

---

## 2. Create a Virtual Environment

It is recommended to use a virtual environment.

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

If the project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If the project does not require external packages, no additional installation is necessary.

---

# ▶️ Running the Application

From the project root directory, run:

```bash
python src/main.py
```

If the project uses a different entry point, run the appropriate main Python file.

For example:

```bash
python main.py
```

---

# 🔄 Application Workflow

A typical user workflow looks like this:

```text
                ┌──────────────────┐
                │  Start Program   │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   Main Menu      │
                └────────┬─────────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
    Search Flights   View Bookings   Exit
          │              │
          ▼              ▼
    Select Flight   Select Booking
          │              │
          ▼              ▼
    Enter Passenger   View Details
       Details
          │
          ▼
    Check Availability
          │
       ┌──┴───┐
       │      │
    Available  Full
       │      │
       ▼      ▼
    Confirm  Show Error
    Booking
       │
       ▼
  Generate Booking ID
       │
       ▼
  Save Booking Details
       │
       ▼
   Booking Complete
```

---

# 📋 Available Operations

The CLI provides operations similar to the following.

## 1. Search Flights

Users can search for available flights based on supported search criteria.

Example:

```text
Enter source: Hyderabad
Enter destination: Delhi
```

The system displays matching flights.

---

## 2. View Flight Details

Users can select a flight and view information such as:

```text
Flight ID
Airline
Source
Destination
Departure
Arrival
Price
Available Seats
```

---

## 3. Book a Flight

The booking process generally follows:

```text
Select Flight
      ↓
Check Seat Availability
      ↓
Enter Passenger Details
      ↓
Validate Details
      ↓
Confirm Booking
      ↓
Generate Booking ID
      ↓
Save Booking
```

After successful booking, the system displays the booking information.

Example:

```text
Booking Successful!

Booking ID : BK1001
Passenger  : John Doe
Flight     : AI101
Route      : Hyderabad → Delhi
Seat       : 12A
Status     : Confirmed
```

---

## 4. View Bookings

Users can view previously created bookings.

Example information:

```text
Booking ID
Passenger Name
Flight ID
Source
Destination
Seat
Booking Status
```

---

## 5. Cancel Booking

Users can cancel an existing booking using the booking/reference ID.

Example:

```text
Enter Booking ID: BK1001

Booking found.

Booking cancelled successfully.
```

After cancellation, the corresponding seat availability is updated.

---

# 🗃️ Data Management

The application maintains information required for the airline reservation workflow.

Typical entities include:

### Flight

```text
Flight ID
Airline
Source
Destination
Departure Time
Arrival Time
Price
Available Seats
```

### Passenger

```text
Passenger ID
Name
Age
Gender
Contact Information
```

### Booking

```text
Booking ID
Passenger ID
Flight ID
Seat Number
Booking Date
Booking Status
```

These entities allow the application to model the basic relationships between flights, passengers, and bookings.

---

# 🔐 Input Validation

Input validation is an important part of the application.

The system prevents invalid values from reaching the business logic.

Examples:

```text
Invalid menu option
        ↓
Display error
        ↓
Ask for input again
```

For example:

```text
Enter your choice: abc

Invalid input.
Please enter a valid option.
```

Similarly, attempting to book a flight with no available seats should not create a booking.

---

# ⚠️ Error Handling

The application uses exception handling and validation to make the CLI more reliable.

Common scenarios include:

### Invalid Flight

```text
Flight not found.
Please enter a valid flight ID.
```

### Invalid Booking

```text
Booking not found.
Please check the booking ID.
```

### No Available Seats

```text
No seats are available on this flight.
Please select another flight.
```

### Invalid Input

```text
Invalid input.
Please enter a valid value.
```

The goal is to handle expected errors gracefully instead of allowing the application to crash.

---

# 🧱 Project Design

The application is organized into separate responsibilities.

A simplified architecture is:

```text
┌──────────────────────┐
│      CLI / UI        │
│    User Interaction │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      Services        │
│  Business Operations │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       Models         │
│ Flight / Passenger   │
│      / Booking       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Data Storage      │
│ Files / Database     │
└──────────────────────┘
```

This separation makes the project easier to:

- Understand
- Test
- Debug
- Extend
- Maintain

---

# 🧪 Testing

Tests can be executed using the project's configured testing framework.

If `pytest` is used:

```bash
pytest
```

For verbose output:

```bash
pytest -v
```

Testing should cover important scenarios such as:

- Flight search
- Valid booking
- Invalid booking
- Seat availability
- Passenger validation
- Booking cancellation
- Invalid booking ID
- Invalid flight ID
- Data persistence
- Error handling

---

# 🎯 Learning Objectives

This project demonstrates practical understanding of several Python concepts.

## Python

- Variables
- Conditional statements
- Loops
- Functions
- Lists
- Dictionaries
- Modules
- Packages
- File handling
- Exception handling

## Object-Oriented Programming

- Classes
- Objects
- Encapsulation
- Methods
- Constructors
- Separation of responsibilities

## Application Development

- CLI application design
- Input validation
- Business logic
- CRUD operations
- Data persistence
- Modular architecture
- Error handling

## Software Development

- Project organization
- Git and GitHub
- Virtual environments
- Dependency management
- Testing
- Documentation

---

# 🔮 Future Improvements

The current CLI application can be extended with additional features.

### Authentication

Add:

- User registration
- Login
- Password management
- Admin and customer roles

### Advanced Flight Search

Add filters for:

- Date
- Price
- Airline
- Departure time
- Arrival time
- Number of stops

### Seat Selection

Provide a visual/text-based seat map:

```text
     A   B   C     D   E   F

1    □   □   □     □   □   □
2    □   □   □     □   □   □
3    □   □   □     □   □   □
4    X   □   □     □   X   □
```

Where:

```text
□ = Available
X = Occupied
```

### Payment Integration

A future version could integrate a payment gateway for real payment processing.

### Database Integration

The application can be migrated to a relational database such as:

```text
MySQL
PostgreSQL
SQLite
```

This would allow the system to support larger datasets and more reliable concurrent access.

### REST API

The business logic could be exposed through a REST API using frameworks such as:

```text
FastAPI
Flask
Django REST Framework
```

### Web Interface

A web frontend could be added using:

```text
React
HTML
CSS
JavaScript
```

The CLI would then become one client of the same backend services.

---

# 📊 Possible Database Model

A relational implementation could contain tables such as:

```text
┌──────────────┐
│   FLIGHTS    │
├──────────────┤
│ flight_id    │
│ airline      │
│ source       │
│ destination  │
│ departure    │
│ arrival      │
│ price        │
│ seats        │
└──────┬───────┘
       │
       │
       ▼
┌──────────────┐
│   BOOKINGS   │
├──────────────┤
│ booking_id   │
│ flight_id    │
│ passenger_id │
│ seat_number  │
│ booking_date │
│ status       │
└──────┬───────┘
       │
       │
       ▼
┌──────────────┐
│  PASSENGERS  │
├──────────────┤
│ passenger_id │
│ name         │
│ age          │
│ gender       │
│ contact      │
└──────────────┘
```

This design keeps flight, passenger, and booking information logically separated.

---

# 🔒 Data and Security Considerations

If this project is extended into a production application, additional security measures would be required.

These may include:

- Password hashing
- Authentication and authorization
- Input sanitization
- Secure database access
- Environment variables for secrets
- Protection against SQL injection
- Secure payment processing
- Logging and auditing
- Proper handling of personally identifiable information

**Never commit passwords, API keys, database credentials, or other secrets to GitHub.**

Use environment variables or a secure secret-management solution instead.

---

# 🧹 Code Quality

The project aims to follow good software development practices such as:

- Meaningful variable and function names
- Small reusable functions
- Modular code
- Separation of responsibilities
- Input validation
- Exception handling
- Avoiding unnecessary duplication
- Clear documentation
- Consistent formatting

---

# 📝 Example CLI Session

A typical session may look like:

```text
========================================
       AIRLINE BOOKING SYSTEM
========================================

1. Search Flights
2. View Flight Details
3. Book Flight
4. View Bookings
5. Cancel Booking
6. Exit

Enter your choice: 1

Enter source: Hyderabad
Enter destination: Delhi

Available Flights
----------------------------------------
Flight ID : AI101
Airline   : Air India
From      : Hyderabad
To        : Delhi
Price     : ₹5,500
Seats     : 24
----------------------------------------

Enter Flight ID to continue: AI101

Passenger Details
-----------------
Name : John Doe
Age  : 25

Booking confirmed successfully!

Booking ID : BK1001
Flight ID  : AI101
Passenger  : John Doe
Status     : Confirmed
```

---

# 🏆 Project Highlights

This project demonstrates the ability to build a complete command-line application rather than isolated Python programs.

### Key strengths

- ✈️ Real-world airline reservation use case
- 🐍 Python-based implementation
- 🧱 Modular application structure
- 👤 Passenger management
- 🎫 Booking management
- 💺 Seat availability management
- 🔎 Flight search
- 🛡️ Input validation
- ⚠️ Exception handling
- 💾 Persistent data management
- 🧪 Testable application design
- 📚 Clear project documentation

---

# 📌 Project Status

**Status:** Completed / Learning Project

The current version focuses on implementing the core airline booking workflow through a command-line interface.

Future versions can extend the system with database integration, authentication, payment processing, APIs, and a web interface.

---

# 👨‍💻 Author

**Venkatesh**

B.Tech — Computer Science and Engineering (AI & ML)

### Areas of Interest

- Python
- SQL
- Data Engineering
- Software Development
- AI / Machine Learning
- Backend Development

---

# 📄 License

This project is intended for educational and portfolio purposes.

If a specific open-source license is added to the repository, replace this section with the corresponding license information.

---

# ⭐ If You Like This Project

If you find this project useful or interesting:

- ⭐ Star the repository
- 🍴 Fork the repository
- 🐛 Report issues
- 💡 Suggest improvements
- 🔧 Contribute enhancements

---

## ✈️ Final Note

The **Airline Booking CLI** project was built to demonstrate how Python can be used to create a structured, practical, real-world application from the ground up.

It combines Python programming, object-oriented design, data management, validation, error handling, and software engineering practices into one complete project.
