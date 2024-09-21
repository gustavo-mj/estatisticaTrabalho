import pandas as pd
import matplotlib.pylab as plt

df = pd.read_excel("dados_tratados_GEE.xlsx")

df = df.drop(columns=['Gás', 'Estado'])

dfAgrupado = df.groupby('Nível 1 - Setor').sum()

dfAgrupado['Emissão Total'] = dfAgrupado.sum(axis=1)

df_result = dfAgrupado[['Emissão Total']].reset_index()

print(df_result.describe())

#mapeamento = {categoria: i+1 for i, categoria in enumerate(df_result['Nível 1 - Setor'])}
#plt.bar([mapeamento[categoria] for categoria in df_result['Nível 1 - Setor']], df_result['Emissão Total'])

'''
plt.boxplot(df_result['Emissão Total'])

plt.xlabel('Setor produtivo')
plt.ylabel('Emissão total (em toneladas)')
plt.title('Emissão total por Setor Produtivo')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
'''