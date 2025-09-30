_DEFAULT_STUDENTS = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry",
]

_PLANT_MAP = {
    "G": "Grass",
    "C": "Clover",
    "R": "Radishes",
    "V": "Violets",
}


class Garden:
    """
    Represents a kindergarten garden, assigning plants to students based on a diagram.

    The garden consists of two rows of cups, each containing seeds represented by letters.
    Each student is assigned four cups (two from each row), determined by their alphabetical order.
    The class can be initialized with a custom list of students or defaults to the standard roster.
    """

    def __init__(self, diagram: str, students: list[str] = _DEFAULT_STUDENTS):
        """
        Initializes the Garden with a diagram and an optional list of students.

        Args:
            diagram (str): A string representation of the garden, with two rows separated by a newline.
            students (list[str], optional): List of student names. Defaults to the standard roster.
        """
        self.rows: list[str] = diagram.splitlines()
        self.students: list[str] = sorted(students)

        # Precompute student index for fast lookup
        self._student_index: dict[str, int] = {
            name: idx for idx, name in enumerate(self.students)
        }

    def plants(self, student: str) -> list[str]:
        """
        Returns the list of plant names assigned to the given student.

        Args:
            student (str): The name of the student whose plants are requested.

        Returns:
            list[str]: List of plant names (e.g., ["Violets", "Radishes", ...]) for the student.

        Example:
            >>> g = Garden("VRCG\nVRCC", students=["Valorie", "Raven"])
            >>> g.plants("Valorie")
            ['Violets', 'Radishes', 'Violets', 'Radishes']
        """
        i = self._student_index[student]
        return [_PLANT_MAP[c] for row in self.rows for c in row[2 * i : 2 * i + 2]]
