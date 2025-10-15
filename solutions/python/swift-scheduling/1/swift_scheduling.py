from calendar import FRIDAY, SATURDAY, SUNDAY, WEDNESDAY, monthrange
from datetime import datetime, timedelta

# Constants for date calculations
DAYS_IN_WEEK = 7
MONTHS_IN_QUARTER = 3

# Time constants (hours)
NOW_DELAY_HOURS = 2
WORKDAY_START_HOUR = 8
ASAP_CUTOFF_HOUR = 13
EOD_HOUR = 17
EOW_SUNDAY_HOUR = 20


def delivery_date(start: str, description: str) -> str:
    """
    Convert a delivery date description to an actual delivery date.

    Args:
        start: ISO format string representing the meeting start datetime
        description: Delivery date description in corporate lingo format
                    Fixed formats: "NOW", "ASAP", "EOW"
                    Variable formats: "<N>M" (N-th month), "Q<N>" (N-th quarter)

    Returns:
        ISO format string representing the calculated delivery date

    Examples:
        >>> delivery_date("2023-10-15T10:00:00", "NOW")
        "2023-10-15T12:00:00"

        >>> delivery_date("2023-10-15T10:00:00", "ASAP")
        "2023-10-15T17:00:00"

        >>> delivery_date("2023-10-15T10:00:00", "3M")
        "2024-03-01T08:00:00"

    Note:
        - "NOW": Two hours after the meeting started
        - "ASAP": Today at 17:00 if before 13:00, otherwise tomorrow at 13:00
        - "EOW": Friday 17:00 if Mon-Wed, Sunday 20:00 if Thu-Fri
        - "<N>M": First workday of N-th month at 8:00
        - "Q<N>": Last workday of N-th quarter at 8:00
    """
    try:
        dt_start = datetime.fromisoformat(start)
    except ValueError as e:
        raise ValueError(f"Invalid ISO format: {start}") from e

    # Handle fixed delivery date descriptions
    match description:
        case "NOW":
            # Two hours after the meeting started
            return (dt_start + timedelta(hours=NOW_DELAY_HOURS)).isoformat()
        case "ASAP":
            # Today at 17:00 if before 13:00, otherwise tomorrow at 13:00
            if dt_start.hour < ASAP_CUTOFF_HOUR:
                return _eod(dt_start).isoformat()
            else:
                return (
                    _at_hour(dt_start, ASAP_CUTOFF_HOUR) + timedelta(days=1)
                ).isoformat()
        case "EOW":
            # End of week: Friday 17:00 if Mon-Wed, Sunday 20:00 if Thu-Fri
            current_weekday = dt_start.weekday()
            if current_weekday <= WEDNESDAY:  # Monday, Tuesday, or Wednesday
                return (
                    _eod(dt_start) + timedelta(days=FRIDAY - current_weekday)
                ).isoformat()
            else:  # Thursday or Friday
                return (
                    _at_hour(dt_start, EOW_SUNDAY_HOUR)
                    + timedelta(days=SUNDAY - current_weekday)
                ).isoformat()
        case _:
            # Handle variable delivery date descriptions below
            pass

    if description[-1] == "M":
        # Handle "<N>M" format: N-th month delivery
        # At 8:00 on the first workday of this year's or next year's N-th month
        month = int(description[:-1])
        year = dt_start.year

        # If current month is >= target month, use next year
        if dt_start.month >= month:
            year += 1

        # Find the first workday (Monday-Friday) of the target month
        d = datetime(year, month, 1)

        # If the 1st falls on weekend, move to the next Monday
        if d.weekday() >= SATURDAY:
            d += timedelta(days=(-d.weekday() % DAYS_IN_WEEK))

        return _at_hour(d, WORKDAY_START_HOUR).isoformat()

    if description[0] == "Q":
        # Handle "Q<N>" format: N-th quarter delivery
        # At 8:00 on the last workday of this year's or next year's N-th quarter

        # Last month of the quarter (3, 6, 9, or 12)
        quarter = int(description[1:])
        month = quarter * MONTHS_IN_QUARTER

        # If current month is after the N-th quarter, use next year
        year = dt_start.year
        if dt_start.month > quarter * MONTHS_IN_QUARTER:
            year += 1

        # Get the last day of the quarter's last month
        d = datetime(year, month, monthrange(year, month)[1])

        # If we're on the weekend, move to the previous Friday
        if d.weekday() >= SATURDAY:
            d -= timedelta(days=d.weekday() - FRIDAY)

        return _at_hour(d, WORKDAY_START_HOUR).isoformat()

    raise ValueError(f"Unknown delivery description: {description}")


def _at_hour(dt: datetime, hour: int) -> datetime:
    """
    Create a new datetime with the specified hour on the same date.

    Args:
        dt: The source datetime object
        hour: The target hour (0-23)

    Returns:
        A new datetime object with the specified hour and zero minutes/seconds
    """
    return datetime(dt.year, dt.month, dt.day, hour, 0)


def _eod(dt: datetime) -> datetime:
    """
    Get the end-of-day datetime (17:00) for the given date.

    Args:
        dt: The source datetime object

    Returns:
        A new datetime object at 17:00 (5 PM) on the same date
    """
    return _at_hour(dt, EOD_HOUR)
