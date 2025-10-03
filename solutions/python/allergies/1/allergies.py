ALLERGENS: list[str] = [
    "eggs",
    "peanuts",
    "shellfish",
    "strawberries",
    "tomatoes",
    "chocolate",
    "pollen",
    "cats",
]


class Allergies:
    """Determine allergies from a numeric score."""

    def __init__(self, score: int):
        """Initialize with allergy score."""
        self.allergens = {
            allergen for i, allergen in enumerate(ALLERGENS) if score & (1 << i)
        }

    def allergic_to(self, item: str) -> bool:
        """Check if allergic to given item."""
        return item in self.allergens

    @property
    def lst(self) -> list[str]:
        """Return list of all allergens."""
        return list(self.allergens)
