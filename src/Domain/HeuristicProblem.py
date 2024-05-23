from abc import ABC, abstractmethod


class Solution(ABC):
    """Base class for solutions. All soltions must be immutable, therefore, the values inside the solution must be storage inside a private variable"""

    @property
    @abstractmethod
    def evaluation(self) -> float:
        """Return how good or bad the current solution is.

        Returns:
            float: Score that represents the evaluated solution
        """
        pass

    @property
    @abstractmethod
    def value(self):
        """Return the value of the solution (data structure or whatever you choose to be)."""
        pass


class HeuristicProblem(ABC):
    """Abstract class to represent a heuristic problem."""

    def __init__(self) -> None:
        ...

    @abstractmethod
    def create_solution(self, base_solution: Solution | None = None) -> Solution:
        """Creates a random solution for the given problem.

        Args:
            base_solution (Solution | None, optional): if informed the solution generated will be based on this solution. Defaults to None.
        Returns:
            Solution: Newly generated solution.
        """
        ...
