import pandas as pd
from datetime import date, timedelta

with open("D:/Github/03.Projetc_Pandas/archive.txt", 'r', encoding="utf-8") as arquivo:
    lista_frutas = ['Melancia', 'Melão', 'Melão Português', 'Mamão Avai', 'Mamão Formosa', 'Melão Japonês', 'Jerimum']
    lista_datas = []
    lista_produtos = []
    lista_quantidade = []
    for valor in arquivo:

        valor = valor.replace("\n" ,"").split(":")
        # Exclua os elementos que contêm "[" ou "]"
        dados_sem_colchetes = [linha for linha in valor if all('[' not in item and ']' not in item for item in linha)]
        for i ,v in enumerate(dados_sem_colchetes):
            v = v.strip()
            data_atual = date.today()
            if v == 'Dia 1':
                data_espc = data_atual - timedelta(5)
            elif v == 'Dia 2':
                data_espc = data_atual - timedelta(4)
            elif v == 'Dia 3':
                data_espc = data_atual - timedelta(3)
            elif v == 'Dia 4':
                data_espc = data_atual - timedelta(2)
            elif v == 'Dia 5':
                data_espc = data_atual - timedelta(1)
            elif v == 'Dia 6':
                data_espc = data_atual


            if '+' in dados_sem_colchetes[i]:

                v= v.replace('kg','').replace('kl', '').replace('+',' ').split(' ')
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
                lista_datas.append(data_espc)


            else:
                v = v.replace('kg', '').replace('kl','').lower()
                if 'dia' not in v:
                    if 'boa noite' not in v:
                        v = v.replace('kg','').split(' ')
                        lista_produto_minimo = []
                        for valor2 in v:
                            if valor2 == '' or valor2 == 'und' or valor2 == 'm':
                                pass
                            else:
                                if valor2.isnumeric():
                                    if valor2 == '1':
                                        valor2 = 2
                                        lista_quantidade.append(valor2)
                                    else:
                                        valor2 = int(valor2)
                                        lista_quantidade.append(valor2)
                                else:
                                    if valor2.isalpha():
                                        valor2 = valor2.capitalize()
                                        if valor2 == 'E':
                                            lista_produtos.append(*lista_produto_minimo)
                                            lista_datas.append(data_espc)
                                            lista_produto_minimo.clear()
                                        else:
                                            if valor2 in lista_frutas:
                                                if valor2 == 'Melão' or valor2 == 'Melao':
                                                    valor2 = 'Melão espanhol'
                                                    lista_produto_minimo.append(valor2)
                                                else:
                                                    lista_produto_minimo.append(valor2)
                                            else:
                                                if valor2 == 'Formosa' and len(lista_produto_minimo) ==0:
                                                    valor2 = 'Mamão formosa'
                                                    lista_produto_minimo.append(valor2)
                                                else:
                                                    if valor2 == 'Melào':
                                                        valor2 = 'Melão'
                                                        lista_produto_minimo.append(valor2)
                                                    elif valor2 == 'Espanho':
                                                        valor2 = 'espanhol'
                                                        lista_produto_minimo.append(valor2)
                                                    elif valor2 =='Jirimum':
                                                        valor2 = 'Jerimum'
                                                        lista_produto_minimo.append(valor2)
                                                    else:
                                                        lista_produto_minimo.append(valor2)
                                    else:
                                        pass

                        if len(lista_produto_minimo) > 1:
                            lista_produtos.append(f"{lista_produto_minimo[0]} {lista_produto_minimo[1].lower()}")
                        else:
                            if lista_produto_minimo[0] == 'Melão':
                                lista_produtos.append('Melão espanhol')
                            else:
                                lista_produtos.append(*lista_produto_minimo)
                        lista_datas.append(data_espc)


    dados = {'Produtos': lista_produtos, 'Quantidade': lista_quantidade, 'Data': lista_datas}
    df = pd.DataFrame(dados)
    df.to_excel('D:/Github/03.Projetc_Pandas/archive.xlsx')
    print(df)