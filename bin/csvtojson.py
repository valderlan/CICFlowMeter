import csv
import json
import os

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # ler arquivos csv
    with open("./csv/"+csvFilePath, encoding = 'utf-8') as csvf:
        # carregar dados do arquivo csv usando o leitor de dicionário da biblioteca csv
        csvReader = csv.DictReader(csvf)
        # converter cada linha csv em dict python
        for row in csvReader:
            # adicione este dict python ao array json
            jsonArray.append(row)
    # converter python jsonArray para JSON String e gravar no arquivo
    with open("./json/"+jsonFilePath, 'w',encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray,indent=4)
        jsonf.write(jsonString)
        

root, dirs, arquivos = next(os.walk("./csv/")) #'.'
# root : diretórios apenas do que você especificou.
# dirs : subdiretórios da raiz.
# arquivos : Nomes todos os arquivos da raiz e diretórios.
extensoes = ['csv']

for i in arquivos:
    '''if extensoes == []:
        print(i)
    else:'''
    extensao = i.split('.')[-1]
    if extensao in extensoes:
        nome, meio, fim=str(i).split(".")
        csvFilePath = i
        jsonFilePath = nome + '.json'
        csv_to_json(csvFilePath, jsonFilePath)
            