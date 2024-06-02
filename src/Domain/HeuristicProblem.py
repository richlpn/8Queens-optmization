from abc import ABC, abstractmethod
import numpy as np


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
    def value(self) -> np.ndarray[int]:  # type: ignore
        """Return the value of the solution (data structure or whatever you choose to be)."""
        pass

    @value.setter
    @abstractmethod
    def set_value(self, combination: np.ndarray):
        """Set the value of the solution

        Args:
            combination (np.ndarray): array of size 8 contaning integers
        """
        pass


class HeuristicProblem(ABC):
    """Abstract class to represent a heuristic problem."""

    @abstractmethod
    def create_solution(self, base_solution: Solution | None = None) -> Solution:
        """Creates a random solution for the given problem.

        Args:
            base_solution (Solution | None, optional): if informed the solution generated will be based on this solution. Defaults to None.
        Returns:
            Solution: Newly generated solution.
        """

    @abstractmethod
    def compare_solutions(self, solution1: Solution, solution2: Solution) -> Solution:
        """Compare two solutions returning the best one

        Args:
            solution1 (Solution): first solution
            solution2 (Solution): second solution

        Returns:
            Solution: best solution between the two solutions
        """
