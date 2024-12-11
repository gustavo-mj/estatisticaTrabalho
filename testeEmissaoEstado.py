import pandas as pd
import matplotlib.pylab as plt

df = pd.read_excel("dados_tratados_GEE.xlsx")

df = df.drop(columns=['Gás', 'Nível 1 - Setor'])

dfAgrupado = df.groupby('Estado').sum()

print(dfAgrupado)

dfAgrupado['Emissão Total'] = dfAgrupado.sum(axis=1)


df_result = df[['Emissão Total']].reset_index()

print(df_result)

#print(df_result.describe())

#plt.bar(df_result['Estado'], df_result['Emissão Total'])

'''
plt.boxplot(df_result['Emissão Total'])

plt.xlabel('Estado')
plt.ylabel('Emissão total (em toneladas)')
plt.title('Emissão total por Estado')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
'''