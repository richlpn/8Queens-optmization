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

    @property
    @abstractmethod
    def value(self) -> np.ndarray[int]:  # type: ignore
        """Return the value of the solution (data structure or whatever you choose to be)."""

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
    def create_solution(self, base_solution: np.ndarray | None = None, size: int | None = None) -> Solution:
        """Creates a random solution for the given problem.

        Args:
            base_solution (np.ndarray[int]):if not informed the solution generated will random. Defaults to None. 
            size (int | None): Solution size. Must be informe when the base is None. Defaults to None.
        Returns:
            Solution: Newly generated solution.
        """

    @abstractmethod
    def generate_neighbor(self, base: Solution) -> Solution:
        """Returns a closer combination to the informed base.

        Args:
            base (Solution | None): Base solution used to generate a new combination

        Returns:
            Solution: Neighbor
        """
