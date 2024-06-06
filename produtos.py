class Produtos:
    def __init__(self):
        self.qtd = 0

    def salvar_produtos(self, id_produto, quant_produto):
        nova_lista = []

        if self.qtd != 0:
            with open("app_data/pedidos.txt", "r") as arq_produtos:
                lista_produtos = arq_produtos.readlines()

            for linha in lista_produtos:
                elementos_linha = linha.split(",")

                for x in range(0, len(elementos_linha), 2):
                    if elementos_linha[x].find(str(id_produto)) != -1:
                        if x + 1 == (len(elementos_linha) - 1):
                            if elementos_linha[x + 1] != '0':
                                new_item = int(elementos_linha[x+1]) + quant_produto
                                elementos_linha[x + 1] = str(new_item) + "\n"

                            else:
                                elementos_linha[x + 1] = str(quant_produto) + "\n"
                        else:
                            if elementos_linha[x + 1] != 0:
                                new_item = int(elementos_linha[x + 1]) + quant_produto
                                elementos_linha[x + 1] = str(new_item)

                            else:
                                elementos_linha[x + 1] = str(quant_produto)

                nova_linha = ",".join(elementos_linha)
                nova_lista.append(nova_linha)

            with open("app_data/pedidos.txt", "w") as arq_produtos_:
                arq_produtos_.writelines(nova_lista)

            nova_lista.clear()
            self.qtd = 0


    def contador_soma(self):

        if not self.qtd:
            self.qtd = 1
        else:
            self.qtd = self.qtd + 1


    def contador_subtrai(self):
        if self.qtd > 0:
            self.qtd = self.qtd - 1
