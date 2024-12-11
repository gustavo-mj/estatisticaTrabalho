import pandas as pd
import math
from scipy.stats import pearsonr
from scipy.stats import t

df = pd.read_excel("dados_tratados_GEE.xlsx")

df = df.drop(columns=['Estado', 'Nível 1 - Setor'])

co2_gases = df[df['Gás'].str.startswith('CO2')]
co2_sum = co2_gases.iloc[:, 1:].sum()

other_gases = df[~df['Gás'].str.startswith('CO2')]
other_sum = other_gases.iloc[:, 1:].sum()

print(co2_sum.values)
print(other_sum.values)

# Calculando o coeficiente de correlação de Pearson
coeficiente, p_valor = pearsonr(co2_sum.values, other_sum.values)

# Exibindo os resultados
print(f'Coeficiente de Correlação de Pearson: {coeficiente}')

n = 94749

# Calcular o valor p usando a distribuição t de Student
df = n - 2  # graus de liberdade

r = coeficiente

t_value = r * math.sqrt(n - 2) / math.sqrt(1 - r**2)

# Para um teste bicaudal:
p_value = 2 * (1 - t.cdf(abs(t_value), df))

print(f'Valor p: {p_value}')

# Interpretando os resultados
if p_value < 0.05:
    print("A correlação não é estatisticamente significativa!")
else:
    print("A correlação é estatisticamente significativa.")