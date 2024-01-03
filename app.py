import pandas as pd
from datetime import date

with open("alo.txt", 'r', encoding="utf-8") as arquivo:
    lista_frutas = ['Melancia', 'Melão', 'Melão Português', 'Mamão Avai', 'Mamão Formosa', 'Melão Japonês', 'Jerimum']
    lista_datas = []
    lista_produtos = []
    lista_quantidade = []
    for valor in arquivo:

        valor = valor.replace("\n" ,"").split(":")
        # Exclua os elementos que contêm "[" ou "]"
        dados_sem_colchetes = [linha for linha in valor if all('[' not in item and ']' not in item for item in linha)]
        for i ,v in enumerate(dados_sem_colchetes):
            data_atual = date.today()
            data_string = data_atual.strftime("%d-%m-%Y")
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
                lista_datas.append(data_string)


            else:
                v = v.replace('kg', '').replace('kl','').lower()
                if 'dia' not in v:
                    if 'boa noite' not in v:
                        v = v.replace('kg','').split(' ')
                        lista_produto_minimo = []
                        for valor2 in v:
                            if valor2 == '':
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
                                        if valor2 == 'e':
                                            lista_produtos.append(*lista_produto_minimo)
                                            lista_datas.append(data_string)
                                            lista_produto_minimo.clear()
                                        else:
                                            if valor2 in lista_frutas:
                                                if valor2 == 'Melão' or valor2 == 'Melao':
                                                    valor2 = 'Melão Espanhol'
                                                    lista_produto_minimo.append(valor2.capitalize())
                                                else:
                                                    lista_produto_minimo.append(valor2.capitalize())
                                            else:
                                                if valor2 == 'Formosa' and len(lista_produto_minimo) ==0:
                                                    valor2 = 'Mamão Formosa'
                                                    lista_produto_minimo.append(valor2.capitalize())
                                                else:
                                                    if valor2 == 'Melào':
                                                        valor2 = 'Melão'
                                                        lista_produto_minimo.append(valor2.capitalize())
                                                    elif valor2 == 'Espanho':
                                                        valor2 = 'Espanhol'
                                                        lista_produto_minimo.append(valor2.capitalize())
                                                    else:
                                                        lista_produto_minimo.append(valor2.capitalize())
                                    else:
                                        pass

                        if len(lista_produto_minimo) > 1:
                            lista_produtos.append(f"{lista_produto_minimo[0]} {lista_produto_minimo[1].lower()}")
                        else:
                            lista_produtos.append(*lista_produto_minimo)
                        lista_datas.append(data_string)


    dados = {'Produtos': lista_produtos, 'Quantidade': lista_quantidade, 'Data': lista_datas}
    df = pd.DataFrame(dados)
    df.to_excel('arquivo2.xlsx')
    print(df)