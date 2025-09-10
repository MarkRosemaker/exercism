import random
import string

# Maximum number of attempts to generate a unique robot name before raising an error.
MAX_ATTEMPTS: int = 10000


class Robot:
    """
    Manage robot factory settings.
    """

    _names_taken: set[str] = set()

    def __init__(self):
        """
        Initialize a robot with no name.
        """
        self._name: str = ""

    def reset(self):
        """
        Reset the robot to factory settings, wiping its name.
        The next time the name is requested, a new unique random name is generated.
        """
        self._name = ""

    @property
    def name(self) -> str:
        """
        Read-only property for the robot's name. Generates a new unique random name if none exists.
        """
        if not self._name:
            self._name = Robot._gen_name_unique()

        return self._name

    @staticmethod
    def _gen_name() -> str:
        """
        Generate a random robot name in the format: two uppercase letters followed by three digits.
        Example: RX837 or BC811
        """
        return "".join(
            # 2 letters
            random.choices(string.ascii_uppercase, k=2)
            # 3 digits
            + random.choices(string.digits, k=3)
        )

    @staticmethod
    def _gen_name_unique() -> str:
        """
        Generate a unique robot name, ensuring no collisions with existing robots.
        """
        # Limit attempts to avoid infinite loop if all names are exhausted
        for _ in range(MAX_ATTEMPTS):
            name = Robot._gen_name()
            if name not in Robot._names_taken:
                Robot._names_taken.add(name)
                return name

        raise RuntimeError("Exhausted all possible unique robot names.")
