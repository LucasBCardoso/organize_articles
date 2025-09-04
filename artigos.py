#leia o arquivo leitura.csv e mostre as informações em um dataframe do pandas
import pandas as pd
df = pd.read_csv('leitura.csv')
#print(df)

#leia o df e crie um novo dataframe apenas com os artigos que possuem status FICA
df_fica = df[df['STATUS'] == 'FICA']
#print(df_fica)

#os artigos no df_fica começam com um texto do tipo "Silva, Michel Rocha da – ""
#note que o nome sempre termina com " – "
#remova esse texto do título do artigo, deixando apenas o título
df_fica['TÍTULO DO ARTIGO'] = df_fica['TÍTULO DO ARTIGO'].str.split(' – ').str[1]

#considere que o titulo dos artigos na pasta lidos pode não estar completo
#ex: "Calibration and evaluation of new irrigated" é o titulo parcial e o dado no df_fica é "Calibration and evaluation of new irrigated rice cultivars in the SimulArroz model"
#para resolver isso, vamos usar apenas os primeiros 30 caracteres do título do artigo para fazer a busca
df_fica['TÍTULO DO ARTIGO'] = df_fica['TÍTULO DO ARTIGO'].str[:30]

#varios artigos não foram encontrados, apesar de estarem na pasta lidos
#isso ocorre porque o título do artigo no df_fica pode conter caracteres especiais, como acentos
#para resolver isso, vamos remover os acentos do título do artigo
import unicodedata
def remove_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

df_fica['TÍTULO DO ARTIGO'] = df_fica['TÍTULO DO ARTIGO'].apply(remove_acentos)

import os
import shutil

found_count = 0
not_found_count = 0

def normalizar_nome(texto):
    texto = remove_acentos(texto)
    texto = texto.lower().replace("_", " ").replace("-", " ")
    return " ".join(texto.split())

for index, row in df_fica.iterrows():
    titulo = normalizar_nome(row['TÍTULO DO ARTIGO'])

    encontrado = False
    for file in os.listdir("lidos"):
        file_norm = normalizar_nome(file)

        # se o título (mesmo truncado) estiver dentro do nome normalizado do arquivo
        if titulo in file_norm:
            shutil.copy(os.path.join("lidos", file), "ler")
            print(f"✔ Arquivo {file} copiado para a pasta ler")
            found_count += 1
            encontrado = True
            break

    if not encontrado:
        print(f"✘ Arquivo não encontrado para o título: {titulo}")
        not_found_count += 1

print(f"\nNúmero de artigos encontrados: {found_count}")
print(f"Número de artigos não encontrados: {not_found_count}")