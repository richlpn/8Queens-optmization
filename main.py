from src.Algorithm.GeneticAlgorithm import GeneticAlgorithm
from src.Algorithm.SimulatedAnnealing import SA
from src.Algorithm.HillClimbingRestart import HillClimbingRestart
from src.Domain.EightQueens import EightQueenProblem

import pandas as pd


def main():
    problem = EightQueenProblem()
    hill = HillClimbingRestart(20, problem, 8)
    ga = GeneticAlgorithm(50, 20, 0.2, problem)
    sa = SA(problem, 1000, 0.99)
    results = []
    metrics = []

    for i in range(1, 30):
        results.append((i, 'HC', hill.solve().evaluation))
        results.append((i, 'SA', sa.solve(8).evaluation))
        results.append((i, 'GA', ga.solve().evaluation))

        if i == 29:
            metrics.extend(
                [(c, b, 'SA')for c, b in sa.metrics] +
                [(c, b, 'HILL')for c, b in hill.metrics] +
                [(c, b, 'GA')for c, b in ga.metrics]
            )

    results_df = pd.DataFrame(results, columns=[
        'exec',  'algorithm', 'evaluation'])

    metrics_df = pd.DataFrame(metrics, columns=[
        'call', 'evaluation', 'algorithm', ])

    metrics_df.to_csv('./Report/data.csv', index=False)
    results_df.to_csv('./Report/results.csv', index=False)


if __name__ == '__main__':
    main()
