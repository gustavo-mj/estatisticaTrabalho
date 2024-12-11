import pandas as pd
import matplotlib.pylab as plt
import math
from scipy.stats import t

def graus_de_liberdade(s1, n1, s2, n2):
    numerador = (s1**2 / n1 + s2**2 / n2)**2
    denominador = ((s1**2 / n1)**2 / (n1 - 1)) + ((s2**2 / n2)**2 / (n2 - 1))
    g = numerador / denominador
    return int(g)

df = pd.read_excel("dados_tratados_GEE.xlsx")
df = df.drop(columns=['Gás', 'Nível 1 - Setor'])

norte_nordeste = ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO', 'MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA']
sul_sudeste_centrooeste = ['PR', 'RS', 'SC', 'SP', 'RJ', 'ES', 'MG', 'MT', 'MS', 'GO', 'DF']

# Manipulação dos dados
df_norte_nordeste = df[df['Estado'].isin(norte_nordeste)]
df_sul_sudeste_centrooeste = df[df['Estado'].isin(sul_sudeste_centrooeste)]
df_norte_nordeste['Emissão Total'] = df_norte_nordeste.loc[:, 1970:2021].sum(axis=1)
df_sul_sudeste_centrooeste['Emissão Total'] = df_sul_sudeste_centrooeste.loc[:, 1970:2021].sum(axis=1)
df_result_nn = df_norte_nordeste[['Emissão Total']].reset_index()
df_result_ssc = df_sul_sudeste_centrooeste[['Emissão Total']].reset_index()

# Separação das amostras
tamanho_amostra = 100
amostra_base_nn = df_result_nn.sample(n=tamanho_amostra, random_state=42)
amostra_base_ssc = df_result_ssc.sample(n=tamanho_amostra, random_state=42)

mediaNN = amostra_base_nn["Emissão Total"].mean()
dpNN = amostra_base_nn["Emissão Total"].std()
mediaSSC = amostra_base_ssc["Emissão Total"].mean()
dpSSC = amostra_base_ssc["Emissão Total"].std()
print("Norte-Nordeste")
print("Média: " + str(mediaNN))
print("Desvio padrão: " + str(dpNN))
print("Sul-Sudeste-Centro-Oeste")
print("Média: " + str(mediaSSC))
print("Desvio padrão: " + str(dpSSC))

# Intervalo de Confiança para Média NN:
alpha = 0.05

# Calculando o valor crítico t para o intervalo de confiança
t_critical = t.ppf(1 - alpha / 2, df=tamanho_amostra - 1)

# Calculando o erro padrão da média
erro_padrao = dpNN / math.sqrt(tamanho_amostra)

# Calculando o intervalo de confiança
margem_erro = t_critical * erro_padrao
intervalo_inferior = mediaNN - margem_erro
intervalo_superior = mediaNN + margem_erro

print(f"Intervalo de Confiança para Média NN: ({intervalo_inferior:.2f}, {intervalo_superior:.2f})")

# Intervalo de Confiança para Média SSC:

alpha = 0.05

# Calculando o valor crítico t para o intervalo de confiança
t_critical = t.ppf(1 - alpha / 2, df=tamanho_amostra - 1)

# Calculando o erro padrão da média
erro_padrao = dpSSC / math.sqrt(tamanho_amostra)

# Calculando o intervalo de confiança
margem_erro = t_critical * erro_padrao
intervalo_inferior = mediaSSC - margem_erro
intervalo_superior = mediaSSC + margem_erro

print(f"Intervalo de Confiança para Média SSC: ({intervalo_inferior:.2f}, {intervalo_superior:.2f})")

# Teste de Hipótese para duas amostras independentes:
# amostra tem distribuição aproximadamente normal ou 𝑛>30
# usa-se distribuição t de Student

t_calculado = ( (mediaNN - mediaSSC) / math.sqrt( ((dpNN**2)/tamanho_amostra) + ((dpSSC**2)/tamanho_amostra) ) )
gl = graus_de_liberdade(dpNN, tamanho_amostra, dpSSC, tamanho_amostra)

# Calcular o valor p (teste unilateral à direita)
p_valor = t.sf(t_calculado, gl)
alfa = 0.05

print("Nível de significância: " + str(int(alfa*100)) + "%")
print("Tamanho das amostras: " + str(tamanho_amostra))
print("Graus de liberdade: " + str(gl))
print("Valor t: " + str(t_calculado))
print("Valor p: " + str(p_valor))

if p_valor < alfa:
    print(f"Rejeitamos H0 (t = {t_calculado:.2f}, p = {p_valor:.4f})")
else:
    print(f"Não rejeitamos H0 (t = {t_calculado:.2f}, p = {p_valor:.4f})")