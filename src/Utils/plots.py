import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

PATH = './Report/results/plots/'
plt.figure(figsize=(10, 6))


def evaluation_evolution(metrics_df: pd.DataFrame):
    sa = metrics_df[metrics_df['algorithm'] == 'SA']
    other = metrics_df[metrics_df['algorithm'] != 'SA']
    sns.lineplot(x='call', y='evaluation',
                 data=other, style='algorithm')

    plt.title('Evolução dos algoritmos HC x GA')
    plt.xlabel('Chamadas para função objeivo/Fitness')
    plt.ylabel('Função Objetivo')
    plt.savefig(f'{PATH}/evol2.png')
    plt.show()

    sns.lineplot(x='call', y='evaluation',
                 data=sa, style='algorithm')
    plt.title('Evolução do algoritmo SA')
    plt.xlabel('Chamadas para função objeivo/Fitness')
    plt.ylabel('Função Objetivo')
    plt.savefig(f'{PATH}/evol1.png')
    plt.show()


def evaluation_boxplot(metrics_df: pd.DataFrame):
    sns.boxplot(x='algorithm', y='evaluation', data=metrics_df)
    plt.title('Qualidade das otimizações ao longo de 30 execuções')
    plt.xlabel('Algoritmo')
    plt.ylabel('Função Objetivo')
    plt.savefig(f'{PATH}/cost.png')
    plt.show()


def table_metrics(results_df: pd.DataFrame):
    table = results_df.groupby(by='algorithm', as_index=False).describe()
    table = (table
             .set_index(table['algorithm'])
             .drop(['exec', 'algorithm'], axis='columns', level=0)
             .drop(['count', '25%',	'50%', '75%'], axis='columns', level=1)
             ['evaluation'].reset_index()
             )
    table.to_latex(f'{PATH}/table1.tex',
                   index=False, caption="Estátistica das execuções dos algoritmos",
                   sparsify=True,
                   float_format="%.3f", encoding='utf8')
