import itertools
from Domain.HeuristicProblem import HeuristicProblem, Solution
import numpy as np


class EightQueenSolution(Solution):

    _combination: np.ndarray[int]  # type: ignore

    def __init__(self, combination: np.ndarray[int]) -> None:  # type: ignore
        self.value: np.ndarray[int] = combination.copy()  # type: ignore

    @property
    def value(self) -> np.ndarray[int]:  # type: ignore
        return self._combination.copy()

    @value.setter
    def set_value(self, comb: np.ndarray[int]):  # type: ignore

        if not isinstance(comb, np.ndarray) or comb.size == 0 or not isinstance(comb[0], int):

            raise ValueError(f"Combination: {comb}, is invalid")

        self._combination = comb

    def __count_line_attacks(self):
        """
        Função que recebe um Vetor-Tabuleiro e retorna o número de pares de rainhas
        se atacando mutuamente nas linhas.
        """
        N = len(self._combination)
        ataques = 0

        for col1, col2 in itertools.combinations(range(N), 2):
            if self._combination[col1] == self._combination[col2]:
                ataques += 1

        return ataques

    def __count_diagonals_attacks(self):
        """
        Função que recebe um Vetor-Tabuleiro e retorna o número de pares de rainhas
        se atacando mutuamente nas diagonais.
        """
        N = len(self._combination)
        ataques = 0

        for col1, col2 in itertools.combinations(range(N), 2):
            lin1 = self._combination[col1]
            lin2 = self._combination[col2]

            d1 = lin1 - col1
            d2 = lin2 - col2
            s1 = lin1 + col1
            s2 = lin2 + col2

            if d1 == d2 or s1 == s2:
                ataques += 1

        return ataques

    def evaluation(self) -> float:

        return self.__count_line_attacks() + self.__count_diagonals_attacks()


class EightQueenProblem(HeuristicProblem):

    BOARD_SIZE: int = 8

    def create_solution(self, base_solution: Solution | None = None) -> Solution:

        # TODO: Validate base
        # TODO: isn't Valid -> wise raise an error
        # TODO: base is None -> return random solution
        # TODO: base is valid -> return a neighbot of the solution

        if base_solution is None:
            comb = np.random.randint(
                low=1, high=self.BOARD_SIZE + 1, size=self.BOARD_SIZE)

            return EightQueenSolution(comb)

        elif not isinstance(base_solution, Solution):
            raise ValueError(
                "base solution informed doesn't follow the required class")

        return EightQueenSolution(comb)
