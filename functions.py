from datetime import datetime
from lists import datas, lista_produtos, lista_quantidade, lista_datas

def get_data():
    data_init = input("Data Início: ")
    data_convert(data_init)

def data_convert(value: str) -> object:
    data_converter = datetime.strptime(value, "%d/%m/%Y").date()
    datas.append(data_converter)

def recebendo_dados(file):

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
            if "Dia" not in v:
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
                                lista_quantidade.append(int(valor2))
                        if valor2.isalpha() or valor2 != 'e':
                            lista_produto_minimo.append(valor2)
                        else:
                            pass

                if len(lista_produto_minimo) > 1:
                    lista_produtos.append(f"{lista_produto_minimo[0]} {lista_produto_minimo[1]}")
                else:
                    lista_produtos.append(*lista_produto_minimo)
                # lista_datas.append(data_string)

            else:
                if "Dia" in v:
                    v = v.lstrip().split(' ')
                    if v[1] == '1':
                        lista_datas.append(datas[0])