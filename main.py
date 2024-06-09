from src.Algorithm.GeneticAlgorithm import GeneticAlgorithm
from src.Algorithm.SimulatedAnnealing import SA
from src.Algorithm.HillClimbingRestart import HillClimbingRestart
from src.Domain.EightQueens import EightQueenProblem
from src.Utils import plots as plt
import argparse
import pandas as pd


def plot(*args, **kargs):
    problem = EightQueenProblem()
    hill = HillClimbingRestart(20, problem, 8)
    ga = GeneticAlgorithm(50, 20, 0.05, problem)
    sa = SA(problem, 1000, 0.99)
    results = []
    metrics = []

    for i in range(1, 31):
        results.append((i, 'HC', hill.solve().evaluation))
        results.append((i, 'SA', sa.solve(8).evaluation))
        results.append((i, 'GA', ga.solve().evaluation))

        if i == 30:
            metrics.extend(
                [(c, b, 'SA')for c, b in sa.metrics] +
                [(c, b, 'HC')for c, b in hill.metrics] +
                [(c, b, 'GA')for c, b in ga.metrics]
            )

    results_df = pd.DataFrame(results, columns=[
        'exec',  'algorithm', 'evaluation'])

    metrics_df = pd.DataFrame(metrics, columns=[
        'call', 'evaluation', 'algorithm', ])

    plt.evaluation_boxplot(metrics_df)
    plt.evaluation_evolution(metrics_df)
    plt.table_metrics(results_df)

    metrics_df.to_csv('./Report/results/datasets/data.csv', index=False)
    results_df.to_csv('./Report/results/datasets/results.csv', index=False)


def run(exec: int, *args, **kargs):
    problem = EightQueenProblem()
    hill = HillClimbingRestart(20, problem, 8)
    ga = GeneticAlgorithm(50, 20, 0.2, problem)
    sa = SA(problem, 1000, 0.99)

    for i in range(1, exec + 1):
        s1, s2, s3 = hill.solve(), sa.solve(8), ga.solve()
        print(f'Iteração {i}\nHC: {s1}\nSA: {s2}\nGA: {s3}')


def main():
    parser = argparse.ArgumentParser(description="Run or plot data")

    subparsers = parser.add_subparsers(title="Commands", dest="command")

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument(
        "-n", "--exec_times", type=int, required=False, help="How many times to execute all algorithm's",
        default=30
    )
    run_parser.set_defaults(func=run)

    plot_parser = subparsers.add_parser("plot")
    plot_parser.set_defaults(func=plot)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
    else:
        args.func(getattr(args, 'exec_times', None))


if __name__ == '__main__':
    main()
