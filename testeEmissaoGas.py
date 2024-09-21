import pandas as pd
import matplotlib.pylab as plt

df = pd.read_excel("dados_tratados_GEE.xlsx")

df = df.drop(columns=['Estado', 'Nível 1 - Setor'])

dfAgrupado = df.groupby('Gás').sum()

dfAgrupado['Emissão Total'] = dfAgrupado.sum(axis=1)

df_result = dfAgrupado[['Emissão Total']].reset_index()

print(df_result.describe())

#plt.bar(df_result['Gás'], df_result['Emissão Total'])

'''
plt.boxplot(df_result['Emissão Total'])

plt.xlabel('Gás')
plt.ylabel('Emissão total (em toneladas)')
plt.title('Emissão total por Gás')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
'''