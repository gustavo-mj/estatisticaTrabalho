import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_excel("dados_tratados_GEE.xlsx")

num_amostra = 100

df_gas = df["Gás"].sample(num_amostra)
df_gas = df_gas.str.replace('CO2.*', 'CO2', regex=True)

prop_co2 = df_gas.value_counts()['CO2'] / num_amostra

print(df_gas.value_counts())
print(f"\nProporção CO2: {(prop_co2)} = {(prop_co2*100)}%")