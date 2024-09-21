import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

pd.set_option('display.max_columns', 16)
sns.set_style('white')

dataframe = pd.read_excel("dados_tratados_GEE.xlsx")

# criando uma lista com a soma dos valores de cada ano
coluna_anos = dataframe.columns[3:]
emissao_ano = dataframe[coluna_anos].sum()
print(emissao_ano)

# gráfico de barras
sns.lineplot(x=emissao_ano.index, y=emissao_ano.values).set(title="Emissão Total x Ano")

plt.xticks(rotation=90)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Emissão Total (toneladas)', fontsize=12)
plt.tight_layout()
plt.show()