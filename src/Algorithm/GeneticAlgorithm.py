from random import choice
import numpy as np
from Domain.HeuristicProblem import HeuristicProblem, Solution
from dataclasses import dataclass


@dataclass
class Population:
    individuals: list[Solution]


class GeneticAlgorithm:

    _gen_size: int
    _population_size: int
    _mutation_rate: float

    _problem: HeuristicProblem
    _board_size: int

    def __init__(self, generations: int,
                 population_size: int,
                 mutation_rate: float,
                 domain: HeuristicProblem, board_size: int = 8) -> None:

        self._gen_size = generations
        self._problem = domain
        self._board_size = board_size
        self._population_size = population_size
        self._mutation_rate = mutation_rate

    def crossover(self, parent1: Solution, parent2: Solution) -> tuple[Solution, Solution]:
        N = len(parent1.value)
        c = np.random.randint(1, N-1)

        child1 = np.concatenate((parent1.value[:c], parent2.value[c:]))
        child2 = np.concatenate((parent2.value[:c], parent1.value[c:]))

        return self._problem.create_solution(child1), self._problem.create_solution(child2)

    def mutate(self, individual: Solution) -> Solution:
        VT_mutated = individual.value
        p = np.random.rand()

        if p < self._mutation_rate:
            col = np.random.randint(0, self._board_size)
            linha = np.random.randint(1, self._board_size+1)
            VT_mutated[col] = linha

        return self._problem.create_solution(VT_mutated)

    def selection(self, population: Population) -> Solution:
        candidato1 = choice(population.individuals)
        candidato2 = choice(population.individuals)

        a1 = candidato1.evaluation
        a2 = candidato2.evaluation

        # eleito o candidato com menor custo
        eleito = candidato1 if a1 <= a2 else candidato2

        return eleito

    def create_initial_population(self) -> Population:
        populacao = []
        for _ in range(self._population_size):
            individuo = self._problem.create_solution(size=self._board_size)
            populacao.append(individuo)

        return Population(populacao)

    def crossover_population(self, population: Population) -> Population:
        population_size = len(population.individuals) // 2
        new_population = []
        for _ in range(population_size):
            parent1 = self.selection(population)
            parent2 = self.selection(population)
            child1, child2 = self.crossover(parent1, parent2)
            new_population.extend([child1, child2])
        return Population(new_population)

    def mutate_population(self, population: Population) -> Population:
        """
        Applies mutation to each individual in the population.

        Args:
            population: List of individuals (NumPy arrays in your case).

        Returns:
            List of individuals with mutations applied.
        """
        new_population = [self.mutate(individual)
                          for individual in population.individuals]
        return Population(new_population)

    def selection_population(self, population: Population) -> Population:
        """
        Selects individuals from the population to create a new population of desired size.

        Args:
            population: List of individuals (NumPy arrays in your case).
            population_size: Desired size of the new population.

        Returns:
            List of selected individuals to form the new population.

        Raises:
            Exception: If the original population size is smaller than the desired new population size.
        """
        if len(population.individuals) < self._population_size:
            raise Exception(
                "The population can't be smaller than the expected size of the new population")

        new_population = []
        while len(new_population) < self._population_size:
            selected = self.selection(population)
            new_population.append(selected)

        return Population(new_population)

    def fitness(self, population: Population) -> list[tuple[Solution, float]]:
        return [(i, i.evaluation) for i in population.individuals]

    def solve(self) -> Solution:

        population = self.create_initial_population()

        custosPopulacao = self.fitness(population)

        while True:
            children = self.crossover_population(population)
            children = self.mutate_population(children)
            population.individuals.extend(children.individuals)

            # Selection
            population = self.selection_population(population)

            # UNTIL population has converged
            custosPopulacao = self.fitness(population)
            new_best = min(custosPopulacao, key=lambda x: x[1])
            if new_best[1] == 0:
                return new_best[0]
