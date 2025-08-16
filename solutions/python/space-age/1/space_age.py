class SpaceAge:
    """
    SpaceAge calculates a person's age on different planets in the Solar System, given an age in seconds.

    This class provides methods to determine the equivalent age in years on Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. Each method returns the age rounded to two decimal places, based on the planet's orbital period relative to Earth years.

    Instance Attributes:
        earth_years (float): The age in Earth years, calculated from the input seconds.

    Example:
        >>> SpaceAge(1000000000).on_earth()
        31.69
    """

    SECONDS_PER_EARTH_YEAR = 31_557_600
    ORBITAL_PERIODS = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds: int):
        """
        Initialize SpaceAge with a number of seconds.
        """
        self.seconds: int = seconds

    def _age_on(self, planet: str) -> float:
        """
        Internal helper to calculate age on a given planet.
        Returns the age in the given planet's years, rounded to two decimal places.
        """
        # Calculate age in planet years:
        # 1. Convert seconds to Earth years.
        # 2. Divide by the planet's orbital period (in Earth years) to get age in planet years.
        # 3. Round the result to two decimal places.
        return round(
            self.seconds / self.SECONDS_PER_EARTH_YEAR / self.ORBITAL_PERIODS[planet], 2
        )

    def on_mercury(self) -> float:
        """Returns the age in Mercury years, rounded to two decimal places."""
        return self._age_on("mercury")

    def on_venus(self) -> float:
        """Returns the age in Venus years, rounded to two decimal places."""
        return self._age_on("venus")

    def on_earth(self) -> float:
        """Returns the age in Earth years, rounded to two decimal places."""
        return self._age_on("earth")

    def on_mars(self) -> float:
        """Returns the age in Mars years, rounded to two decimal places."""
        return self._age_on("mars")

    def on_jupiter(self) -> float:
        """Returns the age in Jupiter years, rounded to two decimal places."""
        return self._age_on("jupiter")

    def on_saturn(self) -> float:
        """Returns the age in Saturn years, rounded to two decimal places."""
        return self._age_on("saturn")

    def on_uranus(self) -> float:
        """Returns the age in Uranus years, rounded to two decimal places."""
        return self._age_on("uranus")

    def on_neptune(self) -> float:
        """Returns the age in Neptune years, rounded to two decimal places."""
        return self._age_on("neptune")
