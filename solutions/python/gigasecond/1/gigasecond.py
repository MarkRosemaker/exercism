from datetime import datetime, timedelta

GIGASECOND = timedelta(seconds=1_000_000_000)


def add(moment: datetime) -> datetime:
    """
    Return the moment that is exactly one gigasecond (1,000,000,000 seconds) after the given datetime.

    Args:
        moment (datetime): The starting date and time. Both naive and timezone-aware datetime objects are supported; the returned datetime will have the same timezone information as the input.

    Returns:
        datetime: The date and time one gigasecond later, preserving the timezone info of the input.
    """

    return moment + GIGASECOND
