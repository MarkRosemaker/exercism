from heapq import nlargest


class HighScores:
    """
    Manage a game player's High Score list.

    This class provides methods to access the latest score, the highest score,
    and the top three highest scores from a list of scores, as required for the
    high-score component of the classic Frogger game.
    """

    def __init__(self, scores: list[int]) -> None:
        """
        Initialize the HighScores object with a list of scores.

        Args:
            scores (list[int]): A list of integer scores.
        """
        self.scores = scores

    def latest(self) -> int:
        """
        Return the latest (most recently added) score.

        If the score list is empty, returns 0.

        Returns:
            int: The last score in the list, or 0 if the list is empty.
        """
        return self.scores[-1] if self.scores else 0

    def personal_best(self) -> int:
        """
        Return the highest score from the list.

        Returns:
            int: The highest score, or 0 if the list is empty.
        """
        return max(self.scores, default=0)

    def personal_top_three(self) -> list[int]:
        """
        Return the top three highest scores in descending order.

        If there are fewer than three scores, returns as many as are available.

        Returns:
            list[int]: A list containing up to three highest scores, sorted from highest to lowest.
        """
        return nlargest(3, self.scores)
