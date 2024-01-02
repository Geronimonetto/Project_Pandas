import pandas as pd
from datetime import date

with open("archive.txt", 'r', encoding="utf-8") as arquivo:
    lista_datas = []
    lista_produtos = []
    lista_quantidade = []
    for valor in arquivo:

        valor = valor.replace("\n" ,"").split(":")
        # Exclua os elementos que contêm "[" ou "]"
        dados_sem_colchetes = [linha for linha in valor if all('[' not in item and ']' not in item for item in linha)]
        for i ,v in enumerate(dados_sem_colchetes):
            if '+' in dados_sem_colchetes[i]:
                v= v.replace('kg','').replace('+',' ').split(' ')
                lista_numeros = []
                for valor in v:
                    if valor.isnumeric():
                        valor = int(valor)
                        lista_numeros.append(valor)
                    else:
                        if valor == '':
                            pass
                        else:
                            lista_produtos.append(valor)
                lista_quantidade.append(sum(lista_numeros))
                lista_numeros.clear()
                lista_datas.append(data_string)


            else:
                if "Dia" not in v:
                    v = v.replace('kg','').split(' ')
                    for valor2 in v:
                        if valor2 == '':
                            pass
                        else:
                            # if valor2 == 'Mamão' or valor2 == 'Formosa':
                            #     lista_produto_medio.append(valor2)
                            if valor2.isnumeric():
                                lista_quantidade.append(valor2)
                            else:

                                lista_produtos.append(valor2)
                    lista_datas.append(data_string)

                    dados = {'Produtos': lista_produtos, 'Quantidade': lista_quantidade, 'Data': lista_datas}
                    df = pd.DataFrame(dados)
                    print(df)

                else:
                    if "Dia" in v:
                        data_atual = date.today()
                        data_string = data_atual.strftime("%d-%m-%Y")
