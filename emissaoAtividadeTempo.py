import pandas as pd
import matplotlib.pylab as plt

df = pd.read_excel("dados_tratados_GEE.xlsx")

df = df.drop(columns=['Estado', 'Gás'])

dfAgrupado = df.groupby('Nível 1 - Setor').sum()

for estado in dfAgrupado.index:
    plt.plot(dfAgrupado.columns, dfAgrupado.loc[estado], label=estado)

# Configurações do gráfico
plt.title('Toneladas de GEE por Atividade Econômica (1970-2021)')
plt.xlabel('Ano')
plt.ylabel('Toneladas de GEE')
plt.legend(title='Estados', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)  # Girar os rótulos do eixo X para melhor visualização
plt.tight_layout()

# Mostrar o gráfico
plt.show()