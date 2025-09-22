# Globals for the directions
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

ADVANCE_VECTORS = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
)


class Robot:
    """
    Simulates a robot on an infinite grid that can turn left, turn right, and advance.
    """

    def __init__(self, direction: int = NORTH, x_pos: int = 0, y_pos: int = 0):
        """
        Initialize the robot's direction and coordinates.

        Args:
            direction (int): Initial direction (EAST=0, NORTH=1, WEST=2, SOUTH=3).
            x_pos (int): Initial x-coordinate.
            y_pos (int): Initial y-coordinate.
        """
        self.coordinates = (x_pos, y_pos)
        self.direction = direction

    def move(self, instructions: str):
        """
        Execute a sequence of instructions to move the robot, where:
        - 'R' turns the robot right,
        - 'L' turns the robot left,
        - 'A' advances the robot one unit in its current direction.

        Args:
            instructions (str): String of instructions consisting of 'R', 'L', and 'A'.
        """
        for instruction in instructions:
            match instruction:
                case "R":
                    self.direction = (self.direction + 1) % 4
                case "L":
                    self.direction = (self.direction - 1) % 4
                case "A":
                    x, y = self.coordinates
                    dx, dy = ADVANCE_VECTORS[self.direction]
                    self.coordinates = (x + dx, y + dy)
                case _:
                    raise ValueError(f"Invalid instruction: {instruction}")
