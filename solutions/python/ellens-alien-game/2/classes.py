"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        """
        Initialize an Alien object with x and y coordinates.

        Parameters
        ----------
        x_coordinate : int
            Position on the x-axis.
        y_coordinate : int
            Position on the y-axis.
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        """
        Decreases the object's health by 1 if it is greater than 0.

        This method simulates the object being hit, reducing its health.
        If health is already 0 or less, it does nothing.
        """
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        """
        Check if the alien is alive.

        Returns:
            bool: True if the alien's health is greater than 0, indicating it is alive; False otherwise.
        """
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        """
        Move the object to a new position by updating its x and y coordinates.

        Args:
            x_coordinate (int or float): The new x-coordinate to teleport to.
            y_coordinate (int or float): The new y-coordinate to teleport to.
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other):
        """Detect collision with another Alien (not yet implemented)."""
        pass


def new_aliens_collection(positions):
    """
    Create a list of Alien objects from an iterable of coordinate pairs.

    Args:
        positions (Iterable[Tuple[int, int]]):
            An iterable (such as a list, tuple, or generator) containing pairs of integers.
            Each pair represents the (x, y) coordinates for an Alien instance.
            Example: [(1, 2), (3, 4), (5, 6)]

    Returns:
        List[Alien]:
            A list containing Alien objects. Each Alien is initialized at the corresponding
            (x, y) coordinates provided in the positions argument.
            Example: [Alien(1, 2), Alien(3, 4), Alien(5, 6)]
    """
    return [Alien(*pos) for pos in positions]
