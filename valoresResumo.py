import pandas as pd
df = pd.read_excel("dados_tratados_GEE.xlsx")
df = df.drop(columns=['Gás', 'Estado', 'Nível 1 - Setor'])
resumo = df.describe()
print(resumo)