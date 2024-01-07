import pandas as pd
from datetime import date
from functions import recebendo_dados, get_data
from lists import lista_produtos, lista_quantidade, lista_datas

with open("janeiro01.txt", 'r', encoding="utf-8") as arquivo:

    get_data()
    for valor in arquivo:

        valor = valor.replace("\n" ,"").split(":")
        # Exclua os elementos que contêm "[" ou "]"
        dados_sem_colchetes = [linha for linha in valor if all('[' not in item and ']' not in item for item in linha)]
        recebendo_dados(dados_sem_colchetes)


    dados = {'Produtos': lista_produtos, 'Quantidade': lista_quantidade, 'Data': lista_datas}
    df = pd.DataFrame(dados)
    print(df)