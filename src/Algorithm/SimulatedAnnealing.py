import random
import math


from ..Domain.HeuristicProblem import HeuristicProblem, Solution


class SA:

    _domain: HeuristicProblem
    _init_temp: float
    _cooling_rate: float
    metrics: list[tuple[int, float]]

    def __init__(self, problem: HeuristicProblem,
                 initial_temperature: float, cooling_rate: float,) -> None:
        self._domain = problem
        self._init_temp = initial_temperature
        self._cooling_rate = cooling_rate
        self.metrics = []
        self._obj_calls = 0

    def acceptance_probability(self, current_fitness, new_fitness, temperature):

        if new_fitness > current_fitness:
            return 1.0
        else:
            return math.exp((new_fitness - current_fitness) / temperature)

    def objective_function(self, solution: Solution) -> float:
        self._obj_calls += 1
        return solution.evaluation

    def solve(self, size: int) -> Solution:

        current_solution = self._domain.create_solution(size=size)
        current_fitness = self.objective_function(current_solution)

        best_solution = current_solution
        best_fitness = current_fitness

        temperature = self._init_temp

        while temperature > 0.1:  # Adjust the termination condition as needed

            for neighbor in self._domain.generate_neighbor(current_solution):
                new_fitness = self.objective_function(neighbor)

                acceptance_prob = self.acceptance_probability(
                    current_fitness, new_fitness, temperature)

                if random.random() < acceptance_prob:
                    current_solution = neighbor
                    current_fitness = new_fitness

            if current_fitness < best_fitness:
                best_solution = current_solution
                best_fitness = current_fitness

            temperature *= self._cooling_rate

            self.metrics.append((self._obj_calls, best_fitness))

        return best_solution
