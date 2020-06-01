#APP Ler txt e separar por linhas
import pandas as pd
from sys import argv

param = argv[1:]
#df = pd.read_excel('base_in/0502.xlsx')
nome_arquivo = param[0]

caminho = 'base_in/Macroregiões/'+nome_arquivo
arquivo = open(caminho, 'r')

#print(arquivo.readlines())

lista = arquivo.read().split(',')
col = {'UF':nome_arquivo[6:8], 'Região':nome_arquivo[:3], 'Municipios':lista}

df = pd.DataFrame(col)
df.to_excel('base_out/Macroregiões/'+nome_arquivo+'.xlsx')

arquivo.close()
