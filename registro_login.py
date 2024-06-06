class Login:
    def __init__(self):
        self.usuario_digitado = ""
        self.usuario = []
        self.login_resultado = None

    def procurar_usuario(self):
        if self.usuario_digitado != 'Adm2023@_369_':

            with open("app_data/usuarios.txt", "r") as arquivo_usuarios:
                linhas = arquivo_usuarios.readlines()
                numero_linhas = len(linhas)
                arquivo_usuarios.seek(0)

                if numero_linhas > 0:

                    for numero_linha, linha in enumerate(arquivo_usuarios, start=0):

                        if numero_linha != numero_linhas:
                            conteudo = linha
                            self.usuario = conteudo.strip().split(', ')

                        if self.usuario_digitado == self.usuario[0]:
                            self.login_resultado = 1
                            break

                        else:
                            self.login_resultado = 0

                else:
                    print("arquivo vazio")
        else:
            self.login_resultado = 2023

class Registro:
    def __init__(self):
        self.dados = []  # Variavel inutilizada (mais tarde)

    def registrar(self, dados):
        with open("app_data/usuarios.txt", "a") as arquivo_usuarios:
            arquivo_usuarios.write("\n")
            for dado in dados:
                if dado != dados[3]:
                    arquivo_usuarios.write(dado + ", ")
                else:
                    arquivo_usuarios.write(dado)
