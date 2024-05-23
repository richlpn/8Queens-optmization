from abc import ABC, abstractmethod


class Solution(ABC):
    """Base class for solutions. All soltions must be immutable"""

    def __init__(self, *args, **kargs) -> None:
        ...

    def __str__(self) -> str:
        ...

    @abstractmethod
    def evaluate(self) -> float:
        """Return how good or bad the current solution is.

        Returns:
            float: Score that represents the evaluated solution
        """
        ...


class HeuristicProblem(ABC):
    """Abstract class to represent a heuristic problem."""

    def __init__(self) -> None:
        ...

    @abstractmethod
    def random_solution(self, base_solution: Solution | None = None) -> Solution:
        """Creates a random solution for the given problem.

        Args:
            base_solution (Solution | None, optional): if informed the solution generated will be based on this solution. Defaults to None.
        Returns:
            Solution: Newly generated solution.
        """
        ...
