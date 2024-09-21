import pandas as pd

emissoes_gases = pd.read_excel('1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx', sheet_name = 'GEE Estados')

emissoes_gases = emissoes_gases.drop(columns=['Nível 2', 'Nível 3', 'Nível 4', 'Nível 5', 'Nível 6', 'Atividade Econômica', 'Produto'])

emissoes_gases = emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'] == 'Emissão']

emissoes_gases = emissoes_gases.drop(columns=['Emissão / Remoção / Bunker'])

emissoes_gases.to_excel('dados_tratados_GEE.xlsx', sheet_name='Dados Tratados GEE', index=False)