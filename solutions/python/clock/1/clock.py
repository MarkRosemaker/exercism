MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24


class Clock:
    def __init__(self, hour: int, minute: int):
        """Initialize a clock with the given hour and minute, normalizing to 24-hour format."""
        self.hour = (hour + minute // MINUTES_IN_HOUR) % HOURS_IN_DAY
        self.minute = minute % MINUTES_IN_HOUR

    def __repr__(self) -> str:
        """Return the developer-facing string representation of the clock."""
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self) -> str:
        """Return the user-facing string representation of the clock in HH:MM format."""
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other: object) -> bool:
        """Check if two clocks represent the same time."""
        if not isinstance(other, Clock):
            return NotImplemented
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes: int) -> "Clock":
        """Add minutes to the clock and return a new Clock instance."""
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes: int) -> "Clock":
        """Subtract minutes from the clock and return a new Clock instance."""
        return Clock(self.hour, self.minute - minutes)
