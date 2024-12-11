import pandas as pd
from math import sqrt
pd.set_option('display.max_columns', None)
df = pd.read_excel("dados_tratados_GEE.xlsx")

num_amostra = 100

df_gas = df["Gás"].sample(num_amostra)
df_gas = df_gas.str.replace("CO2.*", "CO2", regex=True)

prop_co2 = df_gas.value_counts().get("CO2", 0) / num_amostra
print(f"\nProporção CO2: {(prop_co2)} = {(prop_co2*100)}%")


proporcao_h2 = 0.5 # 50% (Hipótese Nula: a proporção é 50%)
nivel_sig = 0.05   # 5%  (nível de significância)

Z = (prop_co2 - proporcao_h2) / sqrt(proporcao_h2 * (1 - proporcao_h2) / num_amostra)
Ztab = 1.645 # vendo a tabela z com alfa = 0.05
print(f"Z = {Z}")
print(f"Z tabelado = {Ztab}")