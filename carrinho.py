class Carrinho:
    def __init__(self):
        self.id = []
        self.qtd = []

    def exibir_pedido(self):
        with open("app_data/pedidos.txt", "r") as arq_produtos:
            lista_produtos = arq_produtos.readlines()

        for linha in lista_produtos:
            elementos_linha = linha.split(",")

            for x in range(1, len(elementos_linha), 2):
                if int(elementos_linha[x]) != 0:
                    self.id.append('c_' + str(elementos_linha[x - 1]).strip())
                    self.qtd.append(elementos_linha[x].strip())

    def valor_final(self):
        quant_elementos = []
        valor_produtos = [4129, 2370, 2949, 4999, 629.90, 189.90, 649.90, 499.90, 13499, 1659, 6759, 1999, 3219.90, 839,
                          599.90, 769.90, 1959.90, 239, 2999.90, 489.90, 1239, 469, 399.90, 199]
        soma_final = 0

        with open("app_data/pedidos.txt", "r") as arq_produtos:
            lista_produtos = arq_produtos.readlines()

        for linha in lista_produtos:
            elementos_linha = linha.split(",")

            for x in range(1, len(elementos_linha), 2):
                quant_elementos.append(float(elementos_linha[x]))

        for x in range(len(quant_elementos)):
            soma_final += ((quant_elementos[x]) * (valor_produtos[x]))
        print(str(soma_final))

        return soma_final

    def resetar_produtos(self):
        nova_lista = []
        with open("app_data/pedidos.txt", "r") as arq_produtos:
            lista_produtos = arq_produtos.readlines()

        for linha in lista_produtos:
            elementos_linha = linha.split(",")
            for i in range(1, len(elementos_linha), 2):
                if i != 7:
                    elementos_linha[i] = "0"
                else:
                    elementos_linha[i] = "0\n"

            nova_linha = ",".join(elementos_linha)
            nova_lista.append(nova_linha)

        with open("app_data/pedidos.txt", "w") as arq_produtos_:
            arq_produtos_.writelines(nova_lista)

        nova_lista.clear()
