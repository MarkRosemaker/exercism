import bisect


class Student:
    def __init__(self, name: str, grade: int):
        """Initialize a student with a name and grade."""
        self.name = name
        self.grade = grade

    def __lt__(self, other: object) -> bool:
        """Compare students by grade, then by name."""
        if not isinstance(other, Student):
            return NotImplemented

        # First compare by grade, then by name for sorting
        if self.grade != other.grade:
            return self.grade < other.grade
        return self.name < other.name


class School:
    def __init__(self):
        """Initialize an empty school roster."""
        self.students: list[Student] = []  # Sorted list of Student objects
        self.added_log: list[bool] = []  # Tracks if each add_student call succeeded
        self._names: set[str] = set()  # Set of student names for fast duplicate checks

    def add_student(self, name: str, grade: int):
        """Add a student to the roster if not already present."""
        # Check for duplicate student name
        if name in self._names:
            self.added_log.append(False)
            return

        # Add name to set to prevent future duplicates
        self._names.add(name)
        # Insert student in sorted order using bisect
        bisect.insort(self.students, Student(name, grade))
        # Log successful addition
        self.added_log.append(True)

    def roster(self) -> list[str]:
        """Return a sorted list of all student names."""
        # Extract names from sorted students list
        return list(student.name for student in self.students)

    def grade(self, grade: int) -> list[str]:
        """Return a sorted list of student names in the given grade."""
        # Filter students by grade and return their names
        return list(student.name for student in self.students if student.grade == grade)

    def added(self) -> list[bool]:
        """Return a list indicating if each add_student call succeeded."""
        # Return the log of add_student results
        return self.added_log
