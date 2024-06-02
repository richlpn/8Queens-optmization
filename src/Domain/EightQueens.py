import itertools
from Domain.HeuristicProblem import HeuristicProblem, Solution
import numpy as np


class EightQueenSolution(Solution):

    _combination: np.ndarray

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
    ...
