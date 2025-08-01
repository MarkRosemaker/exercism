"""Functions to automate Conda airlines ticketing system."""

LETTERS = "ABCD"
NUM_LETTERS = len(LETTERS)
SUPERSTITION_NUMBER = 13
TICKET_CODE_LEN = 12


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    for i in range(number):
        yield LETTERS[i % NUM_LETTERS]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    letters = generate_seat_letters(number)
    row = 0

    for i in range(number):
        # Move to the next row after every 4 seats
        if i % NUM_LETTERS == 0:
            row += 1

            # Skip row 13
            if row == SUPERSTITION_NUMBER:
                row += 1

        # Generate seat number
        yield f"{row}{next(letters)}"


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    return {
        passenger: seat
        for passenger, seat in zip(passengers, generate_seats(len(passengers)))
    }


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat_number in seat_numbers:
        yield f"{seat_number}{flight_id}".ljust(TICKET_CODE_LEN, "0")
