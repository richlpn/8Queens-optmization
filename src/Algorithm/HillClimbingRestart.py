
from ..Domain.HeuristicProblem import HeuristicProblem, Solution


class HillClimbingRestart:

    _max_restart: int
    _problem: HeuristicProblem
    _size: int

    def __init__(self, max_restart: int, domain: HeuristicProblem, board_size: int):
        self._max_restart = max_restart
        self._problem = domain
        self._size = board_size

    def get_best_neighbor(self, solution: Solution) -> Solution:

        best = solution
        for neighbor in self._problem.generate_neighbor(solution):
            best = self._problem.compare_solutions(neighbor, best)
        return best

    def solve(self) -> Solution:

        best_state: Solution = self._problem.create_solution(size=self._size)
        for x in range(self._max_restart):
            while True:
                neighbor = self.get_best_neighbor(best_state)
                if neighbor.evaluation > best_state.evaluation:
                    best_state = neighbor
                else:
                    break

        return best_state
