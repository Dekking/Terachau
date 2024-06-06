class Admin:
    def __init__(self):
        self.op_comando = ""
        self.titulo = "Digite o comando:"
        self.resultado = None

    def atualizar_registro(self, id_user):
        compra = [id_user]

        with open("app_data/pedidos.txt", "r") as arq_produtos:
            lista_produtos = arq_produtos.readlines()
            for linha in lista_produtos:
                elementos_linha = linha.strip().split(",")

                for x in range(1, len(elementos_linha), 2):
                    if int(elementos_linha[x]) != 0:
                        compra.append(elementos_linha[x - 1])
                        compra.append(elementos_linha[x])



        with open("app_data/registro.txt", 'a') as arq_rg:

            nova_compra = ",".join(compra) + '\n'
            arq_rg.write(nova_compra)

    def exibir_rg(self):
        with open("app_data/registro.txt", "r") as arq_produtos:
            lista_produtos = arq_produtos.readlines()

            if len(lista_produtos) == 0:
                return "Não há nenhum pedido feito"

            else:
                elementos_linha = ""
                for linha in lista_produtos:
                    elementos_linha = elementos_linha + linha

                return elementos_linha

    def excluir_rg(self, n_linha):
        dados = []
        with open("app_data/registro.txt", "r") as arq_produtos:
            pedidos = arq_produtos.readlines()

            for i in range(1, len(pedidos) + 1):

                if i != n_linha:
                    dados.append(pedidos[i - 1])

        with open("app_data/registro.txt", "w") as arq_produtos:
            for dado in dados:
                arq_produtos.write(dado)

    def comando(self, dado):
        dado = dado.lower()

        if dado == "exibir":
            self.resultado = self.exibir_rg()


        elif dado == "excluir":
            self.resultado = "Digite o numero referente a linha que deseja excluir:\n\n" + self.exibir_rg()
            self.op_comando = "xcl"

        elif self.op_comando == "xcl":
            self.excluir_rg(int(dado))
            self.resultado = self.exibir_rg()
            self.op_comando = ""

        else:
            self.resultado = "Comando Invalido"
