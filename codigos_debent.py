#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from bs4 import BeautifulSoup


#Abre o arquivo baixado anteriormente. O 'r' é para ler o arquivo.
with open('debents.html', 'r') as f:
    conteudo = f.read()
    soup = BeautifulSoup(conteudo, 'lxml')


# Em lista ficarão armazenados todos os links que é onde os nomes das debenures estão
lista = []
for a in soup.find_all('a', href=True):
    lista.append(a['href'])


#Esse loop exclui das listas aqueles links que contem precos no final do link
filtrado = []
for i in range(len(lista)):
    if('precos' in lista[i]):
        None
    else:
        filtrado.append(lista[i])
filtrado


#Nesse ultimo loop ele adiciona à variavel final apenas o que está dentro do 9 segmento do link que é onde fica o nome da debenture
final = []
for i in range(len(filtrado)):
    final.append(filtrado[i].split('/')[9])
final


df_final = pd.DataFrame(final)
df_final.to_csv('codigos1.csv', encoding='latin1')