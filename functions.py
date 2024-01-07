from datetime import datetime
from lists import datas, lista_produtos, lista_quantidade, lista_datas

def get_data():
    data_init = input("Data Início: ")
    data_convert(data_init)

def data_convert(value: str) -> object:
    data_converter = datetime.strptime(value, "%d/%m/%Y").date()
    datas.append(data_converter)

def recebendo_dados(file):
    lista_frutas = ['Melancia', 'Melão', 'Melão Português', 'Mamão Avai', 'Mamão Formosa', 'Melão Japonês', 'Jerimum']
    for i, v in enumerate(file):
        if '+' in file[i]:
            v = v.replace('kg', '').replace('+', ' ').split(' ')
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
            lista_datas.append(datas[0])


        else:
            v = v.replace('kg', '').replace('kl', '').lower()
            if 'dia' not in v:
                if 'boa noite' not in v:
                    v = v.replace('kg', '').split(' ')
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
                                        lista_datas.append(datas[0])
                                        lista_produto_minimo.clear()
                                    else:
                                        if valor2 in lista_frutas:
                                            if valor2 == 'Melão' or valor2 == 'Melao':
                                                valor2 = 'Melão Espanhol'
                                                lista_produto_minimo.append(valor2.capitalize())
                                            else:
                                                lista_produto_minimo.append(valor2.capitalize())
                                        else:
                                            if valor2 == 'Formosa' and len(lista_produto_minimo) == 0:
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
                    lista_datas.append(datas[0])