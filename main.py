from src.Algorithm.GeneticAlgorithm import GeneticAlgorithm
from src.Algorithm.SimulatedAnnealing import SA
from src.Algorithm.HillClimbingRestart import HillClimbingRestart
from src.Domain.EightQueens import EightQueenProblem


def main():
    problem = EightQueenProblem()
    hill = HillClimbingRestart(200, problem, 8)
    ga = GeneticAlgorithm(50, 20, 0.20, problem)
    sa = SA(problem, 1000, 0.01)
    best_hill = hill.solve()
    best_sa = sa.solve(8)
    best_ga = ga.solve()

    print(f"""
    HillClimbingRestart: {best_hill}
    SimulatedAnnealing: {best_sa}
    GeneticAlgorithm: {best_ga}
""")


if __name__ == '__main__':
    main()
