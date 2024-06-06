from tkinter import *
from tkinter import messagebox

import admin
import carrinho
import imagens
import produtos
import registro_login


class AppGui:
    def __init__(self, window_pass):
        self.main_window = window_pass
        self.obj_imagens = imagens.Imagens()
        self.obj_login = registro_login.Login()
        self.obj_registro = registro_login.Registro()
        self.obj_produto = produtos.Produtos()
        self.obj_carrinho = carrinho.Carrinho()
        self.obj_adm = admin.Admin()
        self.voltar_tela = False  # teste

        self.frame1_tela1 = None
        self.frame_adm = None
        self.base_screen1 = None
        self.reciclavel1 = None
        self.input_text = None
        self.bt_register = None
        self.bt_enter = None
        self.bt_enter_registro = None
        self.bt_log = None

        self.login_resultado = False
        self.input_registro1 = None
        self.input_registro2 = None
        self.input_registro3 = None
        self.input_registro4 = None

        self.qtd_p = None
        self.logado = ""

        self.tela_1()

    def tela_1(self):
        base_background = Label(self.main_window, image=self.obj_imagens.img_bg, borderwidth=0)
        base_background.place(x=0, y=0)

        self.frame1_tela1 = Frame(
            self.main_window, width=700, height=648, bg='#000000')
        self.frame1_tela1.pack(side=RIGHT, padx=5)

        self.bt_register = Button(
            self.main_window,
            image=self.obj_imagens.img_bt_rg,
            borderwidth=0,
            highlightthickness=0,
            command=self.registro
        )

        self.bt_register.place(x=20, y=200)

        self.bt_log = Button(
            self.main_window,
            image=self.obj_imagens.img_bt_log,
            borderwidth=0,
            highlightthickness=0,
            command=self.login
        )
        self.bt_log.place(x=20, y=300)

        self.login()

    def login(self):
        for widget in self.frame1_tela1.winfo_children():
            widget.destroy()
        self.base_screen1 = Label(self.frame1_tela1, image=self.obj_imagens.img_base_s1, borderwidth=0)
        self.base_screen1.place(x=100, y=0)

        self.reciclavel1 = Label(self.frame1_tela1, image=self.obj_imagens.img_log_text, borderwidth=0)
        self.reciclavel1.place(x=150, y=200)

        self.input_text = Entry(
            self.frame1_tela1,
            width=30,
            bg='#a6a6a6',
            font=("Arial", 15)
        )
        self.input_text.place(x=152, y=255)

        self.bt_enter = Button(
            self.frame1_tela1,
            image=self.obj_imagens.img_bt_enter,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.login_verificar(self.input_text.get())
        )
        self.bt_enter.place(x=275, y=300)
        self.main_window.bind('<Return>', lambda event: self.login_verificar(self.input_text.get()))

    def login_verificar(self, usuario):

        self.obj_login.usuario_digitado = usuario
        self.input_text.delete(0, END)
        self.obj_login.procurar_usuario()
        login_resultado = self.obj_login.login_resultado

        if login_resultado == 1:  # Verifica o Login
            self.main_window.unbind('<Return>')
            self.logado = usuario
            self.tela_2()
        elif login_resultado == 2023:
            self.main_window.unbind('<Return>')
            self.admin()
        else:
            messagebox.showinfo("ALERTA", "NOME DE USUARIO INCORRETO")

    def registro(self):

        for widget in self.frame1_tela1.winfo_children():
            widget.destroy()
        self.base_screen1 = Label(self.frame1_tela1, image=self.obj_imagens.img_base_s1, borderwidth=0)

        self.base_screen1.place(x=100, y=0)

        label_regitro = Label(self.base_screen1, borderwidth=0, image=self.obj_imagens.img_reg_text)
        label_regitro.place(x=50, y=135)

        self.reciclavel1 = Label(self.base_screen1, image=self.obj_imagens.img_registro, borderwidth=0)
        self.reciclavel1.place(x=40, y=200)

        self.input_registro1 = Entry(
            self.base_screen1,
            width=23, bg='#a6a6a6', font=("Arial", 16), borderwidth=0, highlightthickness=0)
        self.input_registro1.place(x=124, y=200)

        self.input_registro2 = Entry(
            self.base_screen1,
            width=17, bg='#a6a6a6', font=("Arial", 16), borderwidth=0, highlightthickness=0)
        self.input_registro2.place(x=194, y=248.1)

        self.input_registro3 = Entry(
            self.base_screen1,
            width=20, bg='#a6a6a6', font=("Arial", 16), borderwidth=0, highlightthickness=0)
        self.input_registro3.place(x=161, y=296.5)

        self.input_registro4 = Entry(
            self.base_screen1,
            width=20, bg='#a6a6a6', font=("Arial", 16), borderwidth=0, highlightthickness=0)
        self.input_registro4.place(x=161, y=346)

        self.bt_enter_registro = Button(
            self.base_screen1,
            image=self.obj_imagens.bt_submit_registro,
            borderwidth=0,
            highlightthickness=0,
            command=self.registo_verificar
        )
        self.bt_enter_registro.place(x=160, y=400)

    def registo_verificar(self):
        dados = [self.input_registro2.get(),
                 self.input_registro1.get(),
                 self.input_registro3.get(), self.input_registro4.get()]

        verificar = any(dado == "" for dado in dados)  # Se tiver "" recebe True

        if not verificar:
            print("Nenhum em branco")
            self.obj_registro.registrar(dados)
            self.input_registro1.delete(0, END)
            self.input_registro2.delete(0, END)
            self.input_registro3.delete(0, END)
            self.input_registro4.delete(0, END)
            messagebox.showinfo("ALERTA", "REGISTRO FEITO COM SUCESSO!")
        else:
            print("La no obj registro vai mostrar a mensagem espaco vazio")

    def tela_2(self):
        for widget in self.main_window.winfo_children():
            widget.destroy()

        base_background = Label(self.main_window, image=self.obj_imagens.img_bg, borderwidth=0)
        base_background.place(x=0, y=0)

        bt_processador = Button(
            self.main_window,
            image=self.obj_imagens.bt_processador,
            borderwidth=0,
            highlightthickness=0,
            command=self.processadores
        )
        bt_processador.place(x=20, y=190)

        bt_ram = Button(
            self.main_window,
            image=self.obj_imagens.bt_ram,
            borderwidth=0,
            highlightthickness=0,
            command=self.ram
        )
        bt_ram.place(x=20, y=270)

        bt_gpu = Button(
            self.main_window,
            image=self.obj_imagens.bt_gpu,
            borderwidth=0,
            highlightthickness=0,
            command=self.gpu
        )
        bt_gpu.place(x=20, y=350)

        bt_placa_mae = Button(
            self.main_window,
            image=self.obj_imagens.bt_placa_mae,
            borderwidth=0,
            highlightthickness=0,
            command=self.pmae
        )
        bt_placa_mae.place(x=20, y=430)

        bt_memoria2 = Button(
            self.main_window,
            image=self.obj_imagens.bt_memoria2,
            borderwidth=0,
            highlightthickness=0,
            command=self.memoria2
        )
        bt_memoria2.place(x=20, y=510)

        bt_fonte = Button(
            self.main_window,
            image=self.obj_imagens.bt_fonte,
            borderwidth=0,
            highlightthickness=0,
            command=self.fonte
        )
        bt_fonte.place(x=20, y=590)

        bt_sair = Button(
            self.main_window,
            image=self.obj_imagens.bt_sair,
            borderwidth=0,
            highlightthickness=0,
            command=self.sair
        )
        bt_sair.place(x=270, y=630)

        self.processadores()

    def processadores(self):

        self.safe_reset()

        self.obj_produto.qtd = 0  # Utilizada para resetar o texto de qtd clicado
        self.frame()

        base_screen2 = Label(self.frame1_tela1, image=self.obj_imagens.base_tela2, borderwidth=0)
        base_screen2.place(x=30, y=32)

        bt_i9_13 = Button(
            base_screen2,
            image=self.obj_imagens.bt_I9_13900k,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(100)
        )
        bt_i9_13.place(x=41, y=107)

        bt_i9_11 = Button(
            base_screen2,
            image=self.obj_imagens.bt_I9_11900,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(101)
        )
        bt_i9_11.place(x=309, y=107)

        bt_ryzen9_7x = Button(
            base_screen2,
            image=self.obj_imagens.bt_ryzen9_79000X,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(102)
        )
        bt_ryzen9_7x.place(x=41, y=327)

        bt_ryzen9_7x30 = Button(
            base_screen2,
            image=self.obj_imagens.bt_ryzen9_7950X30,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(103)
        )
        bt_ryzen9_7x30.place(x=309, y=327)

        bt_carrinho = Button(
            base_screen2,
            image=self.obj_imagens.bt_carrinho,
            highlightthickness=0,
            borderwidth=1,
            command=self.carrinho
        )
        bt_carrinho.place(x=544, y=3)

    def ram(self):

        self.safe_reset()

        self.obj_produto.qtd = 0
        self.frame()

        base_screen2 = Label(self.frame1_tela1, image=self.obj_imagens.base_tela2, borderwidth=0)
        base_screen2.place(x=30, y=32)

        bt_ram_kingston = Button(
            base_screen2,
            image=self.obj_imagens.bt_ram_kingston,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(200)
        )
        bt_ram_kingston.place(x=45, y=100)

        bt_ram_spectrix = Button(
            base_screen2,
            image=self.obj_imagens.bt_ram_spectrix,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(201)
        )
        bt_ram_spectrix.place(x=313, y=101)

        bt_ram_zadak = Button(
            base_screen2,
            image=self.obj_imagens.bt_ram_zadak,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(202)
        )
        bt_ram_zadak.place(x=45, y=320)

        bt_ram_beast = Button(
            base_screen2,
            image=self.obj_imagens.bt_ram_beast,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(203)
        )
        bt_ram_beast.place(x=313, y=334)

        bt_carrinho = Button(
            base_screen2,
            image=self.obj_imagens.bt_carrinho,
            highlightthickness=0,
            borderwidth=1,
            command=self.carrinho
        )
        bt_carrinho.place(x=544, y=3)

    def gpu(self):

        self.safe_reset()

        self.obj_produto.qtd = 0
        self.frame()

        base_screen2 = Label(self.frame1_tela1, image=self.obj_imagens.base_tela2, borderwidth=0)
        base_screen2.place(x=30, y=32)

        bt_gpu_rtx4090 = Button(
            base_screen2,
            image=self.obj_imagens.bt_gpu_rtx4090,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(300)
        )
        bt_gpu_rtx4090.place(x=53, y=129)

        bt_gpu_rtx3050 = Button(
            base_screen2,
            image=self.obj_imagens.bt_gpu_rtx3050,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(301)
        )
        bt_gpu_rtx3050.place(x=321, y=120)

        bt_gpu_rx7900 = Button(
            base_screen2,
            image=self.obj_imagens.bt_gpu_rx7900,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(302)
        )
        bt_gpu_rx7900.place(x=53, y=343)

        bt_gpu_rx6650 = Button(
            base_screen2,
            image=self.obj_imagens.bt_gpu_rx6650,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(303)
        )
        bt_gpu_rx6650.place(x=321, y=340)

        bt_carrinho = Button(
            base_screen2,
            image=self.obj_imagens.bt_carrinho,
            highlightthickness=0,
            borderwidth=1,
            command=self.carrinho
        )
        bt_carrinho.place(x=544, y=3)

    def pmae(self):

        self.safe_reset()

        self.obj_produto.qtd = 0
        self.frame()

        base_screen2 = Label(self.frame1_tela1, image=self.obj_imagens.base_tela2, borderwidth=0)
        base_screen2.place(x=30, y=32)

        bt_pmae_b650 = Button(
            base_screen2,
            image=self.obj_imagens.bt_pmae_b650,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(400)
        )
        bt_pmae_b650.place(x=50, y=127)

        bt_pmae_b550m = Button(
            base_screen2,
            image=self.obj_imagens.bt_pmae_b550m,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(401)
        )
        bt_pmae_b550m.place(x=318, y=120)

        bt_pmae_h610m = Button(
            base_screen2,
            image=self.obj_imagens.bt_pmae_h610m,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(402)
        )
        bt_pmae_h610m.place(x=50, y=347)

        bt_pmae_b560m = Button(
            base_screen2,
            image=self.obj_imagens.bt_pmae_b560m,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(403)
        )
        bt_pmae_b560m.place(x=318, y=340)

        bt_carrinho = Button(
            base_screen2,
            image=self.obj_imagens.bt_carrinho,
            highlightthickness=0,
            borderwidth=1,
            command=self.carrinho
        )
        bt_carrinho.place(x=544, y=3)

    def memoria2(self):

        self.safe_reset()

        self.obj_produto.qtd = 0
        self.frame()

        base_screen2 = Label(self.frame1_tela1, image=self.obj_imagens.base_tela2, borderwidth=0)
        base_screen2.place(x=30, y=32)

        bt_memoria2_wd = Button(
            base_screen2,
            image=self.obj_imagens.bt_memoria2_wd,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(500)
        )
        bt_memoria2_wd.place(x=65, y=110)

        bt_memoria2_wdblue = Button(
            base_screen2,
            image=self.obj_imagens.bt_memoria2_wdblue,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(501)
        )
        bt_memoria2_wdblue.place(x=333, y=110)

        bt_memoria2_ssdkingston = Button(
            base_screen2,
            image=self.obj_imagens.bt_memoria2_ssdkingston,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(502)
        )
        bt_memoria2_ssdkingston.place(x=58, y=330)

        bt_memoria2_ssdwd = Button(
            base_screen2,
            image=self.obj_imagens.bt_memoria2_ssdwd,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(503)
        )
        bt_memoria2_ssdwd.place(x=326, y=344)

        bt_carrinho = Button(
            base_screen2,
            image=self.obj_imagens.bt_carrinho,
            highlightthickness=0,
            borderwidth=1,
            command=self.carrinho
        )
        bt_carrinho.place(x=544, y=3)

    def fonte(self):

        self.safe_reset()

        self.obj_produto.qtd = 0
        self.frame()

        base_screen2 = Label(self.frame1_tela1, image=self.obj_imagens.base_tela2, borderwidth=0)
        base_screen2.place(x=30, y=32)

        bt_fonte_thermaltake = Button(
            base_screen2,
            image=self.obj_imagens.bt_fonte_thermaltake,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(600)
        )
        bt_fonte_thermaltake.place(x=52, y=120)

        bt_fonte_smart = Button(
            base_screen2,
            image=self.obj_imagens.bt_fonte_smart,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(601)
        )
        bt_fonte_smart.place(x=320, y=120)

        bt_fonte_scoolerv3 = Button(
            base_screen2,
            image=self.obj_imagens.bt_fonte_scoolerv3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(602)
        )
        bt_fonte_scoolerv3.place(x=55, y=340)

        bt_fonte_reddragon = Button(
            base_screen2,
            image=self.obj_imagens.bt_fonte_reddragon,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.vendas(603)
        )
        bt_fonte_reddragon.place(x=318, y=340)

        bt_carrinho = Button(
            base_screen2,
            image=self.obj_imagens.bt_carrinho,
            highlightthickness=0,
            borderwidth=1,
            command=self.carrinho
        )
        bt_carrinho.place(x=544, y=3)

    def vendas(self, ident):

        self.destruir(self.frame1_tela1)
        self.frame()

        img = self.item_clicado(ident)

        base_vendas = Label(
            self.frame1_tela1,
            image=self.obj_imagens.base_vendas,
            borderwidth=0
        )
        base_vendas.place(x=30, y=32)

        img_clicada = Label(
            base_vendas,
            image=img,
            borderwidth=0
        )
        img_clicada.place(x=45, y=170)

        bt_mais = Button(
            base_vendas,
            image=self.obj_imagens.bt_mais,
            highlightthickness=0,
            borderwidth=1,
            command=lambda: self.exe_duas_func_ari(True)
        )
        bt_mais.place(x=440, y=170)

        self.qtd_modficado(0)

        bt_menos = Button(
            base_vendas,
            image=self.obj_imagens.bt_menos,
            highlightthickness=0,
            borderwidth=1,
            command=lambda: self.exe_duas_func_ari(False)

        )
        bt_menos.place(x=440, y=270)

        bt_add_carrinho = Button(
            base_vendas,
            image=self.obj_imagens.bt_add_carrinho,
            highlightthickness=0,
            borderwidth=1,
            command=lambda: self.exe_duas_func_add_c(ident)
        )
        bt_add_carrinho.place(x=220, y=450)

        bt_carrinho = Button(
            base_vendas,
            image=self.obj_imagens.bt_carrinho,
            highlightthickness=0,
            borderwidth=1,
            command=self.carrinho
        )
        bt_carrinho.place(x=544, y=3)

        bt_voltar = Button(
            base_vendas,
            image=self.obj_imagens.bt_voltar,
            highlightthickness=0,
            borderwidth=0,
            command=lambda: self.voltar(ident)
        )
        bt_voltar.place(x=10, y=6)

    def carrinho(self):  # lembrar de resetar as var do carrinho
        self.destruir(self.frame1_tela1)
        self.frame()

        base_carrinho = Label(self.frame1_tela1, image=self.obj_imagens.base_tela2, borderwidth=0)
        base_carrinho.place(x=30, y=32)

        scroll = Scrollbar(base_carrinho, orient=VERTICAL)

        valor_canvas = Canvas(
            base_carrinho,
            width=504,
            height=45,
            bg='black',
            highlightthickness=0
        )
        valor_canvas.create_rectangle(2, 0, 502, 43, outline='white', width=4, fill='#717171')
        valor = self.obj_carrinho.valor_final()

        distancia = len(str(valor))
        if distancia < 6:
            distancia = distancia - 1

        x_area = 215 + (5 * ((98 + distancia) % 10))

        valor_canvas.create_text(90, 20, text='VALOR TOTAL: ', font=('Norwester', 18), fill='white')
        valor_canvas.create_text(180, 20, text='R$ ', font=('Norwester', 18), fill='#00bf63')
        valor_canvas.create_text(x_area, 20, text=f"{valor:,.{2}f}", font=('Norwester', 18), fill='white')

        carrinho_canvas = Canvas(
            base_carrinho,
            width=500,
            height=350,
            bg='#717171',
            yscrollcommand=scroll.set
        )

        scroll.config(command=carrinho_canvas.yview)
        scroll.place(x=550, y=65, height=350)
        carrinho_canvas.place(x=40, y=65)
        valor_canvas.place(x=40, y=420)

        count = 0
        self.obj_carrinho.exibir_pedido()
        if self.obj_carrinho.id:
            i = 0
            for image_id in self.obj_carrinho.id:

                c_image = getattr(self.obj_imagens, image_id)  # Pega o item image_id que esta no obj
                carrinho_canvas.create_image(0, count, anchor=NW, image=c_image)

                carrinho_canvas.create_rectangle(432, count + 10, 496, count + 60,
                                                 outline='white', fill='#717171')
                carrinho_canvas.create_text(464, count + 35, text=self.obj_carrinho.qtd[i], font=('Arial', 21), fill='black')


                count = count + 85
                i = i + 1
        else:
            print(self.obj_carrinho.id)

        carrinho_canvas.config(scrollregion=carrinho_canvas.bbox('all'))

        bt_finalizar = Button(
            base_carrinho,
            image=self.obj_imagens.bt_finalizar,
            highlightthickness=0,
            borderwidth=1,
            command=self.exe_duas_func_fnlzr
        )
        bt_finalizar.place(x=200, y=470)

    def exe_duas_func_ari(self, aritmetica):
        if aritmetica:
            self.obj_produto.contador_soma()
        else:
            self.obj_produto.contador_subtrai()

        self.qtd_modficado(self.obj_produto.qtd)

    def exe_duas_func_add_c(self, ident):

        if self.obj_produto.qtd != 0:
            self.obj_produto.salvar_produtos(ident, self.obj_produto.qtd)
            self.qtd_modficado(0)
            messagebox.showinfo("Parabens!", "ADICIONADO(S) AO CARRINHO")
        else:
            messagebox.showinfo("Alerta!", "ESCOLHA A QUANTIDADE DO PRODUTO")

    def exe_duas_func_fnlzr(self):
        self.obj_adm.atualizar_registro(self.logado)
        self.obj_carrinho.resetar_produtos()
        messagebox.showinfo("Obrigado(a)!", "COMPRA FINALIZADA")
        self.processadores()

    def admin(self):
        if not self.voltar_tela:
            for widget in self.main_window.winfo_children():
                widget.destroy()
                self.voltar_tela = True

        self.main_window.config(bg='black')


        titulo_label = Label(
            self.main_window,
            text="Digite o comando", bg='#000000', font=('Arial', 36), fg='white')
        titulo_label.place(x=350, y=5)

        self.input_text = Entry(self.main_window, width=60, font=('Arial', 18))
        self.input_text.place(x=30, y=80)
        mostrar_conteudo = Button(
            self.main_window,
            text='CONFIRMAR',
            font=('Times', 18),
            command=lambda: self.exe_duas_func_adm(self.input_text.get())
        )
        mostrar_conteudo.place(x=850, y=70)
        self.main_window.bind('<Return>', lambda event: self.exe_duas_func_adm(self.input_text.get()))

        bt_sair = Button(
            self.main_window,
            image=self.obj_imagens.bt_sair,
            borderwidth=0,
            highlightthickness=0,
            command=self.sair
        )
        bt_sair.place(x=30, y=0)


    def exe_duas_func_adm(self, dado):

        self.obj_adm.comando(dado)
        self.conteudo_adm()
        self.input_text.delete(0, END)


    def conteudo_adm(self):
        if not self.voltar_tela:
            for widget in self.frame_adm.winfo_children():
                widget.destroy()
        else:
            self.voltar_tela = False

        self.frame_adm = Frame(
            self.main_window,
            width=1080,
            height=620,
            bg='black'
        )
        self.frame_adm.place(x=0, y=125)

        conteudo = Text(
            self.frame_adm,
            font=('Arial', 16),
            width=580,
            bg='#717171',
            fg='yellow'
        )
        scroll = Scrollbar(self.frame_adm, orient=VERTICAL)
        scroll.place(x=1063, y=0, height=585)
        conteudo.config(yscrollcommand=scroll.set)

        conteudo.insert(END, self.obj_adm.resultado)
        scroll.config(command=conteudo.yview)
        conteudo.place(x=0, y=0)

    def qtd_modficado(self, qtd_add):

        self.qtd_p = Label(
            self.frame1_tela1,
            text=str(qtd_add),
            width=3,
            font=("Times", 30),
            bg='#737373',
        )
        self.qtd_p.place(x=453, y=247)

    def item_clicado(self, id_h):  # da para colocar em outro lugar
        img = None

        if 99 < id_h < 104:
            processadores = [self.obj_imagens.i9_13900k,
                             self.obj_imagens.i9_11900,
                             self.obj_imagens.r9_79000x, self.obj_imagens.r9_7950x3d]
            i = id_h % 10
            img = processadores[i]

        elif 199 < id_h < 204:
            ram = [self.obj_imagens.kingston_ddr4,
                   self.obj_imagens.xpg_ddr4,
                   self.obj_imagens.zadak_ddr5, self.obj_imagens.kingston_ddr5]
            i = id_h % 10
            img = ram[i]

        elif 299 < id_h < 304:
            ram = [self.obj_imagens.rtx_4090,
                   self.obj_imagens.rtx_3050,
                   self.obj_imagens.rx_7900xt, self.obj_imagens.rx_6650xt]
            i = id_h % 10
            img = ram[i]
        elif 399 < id_h < 404:
            ram = [self.obj_imagens.pmae_b650,
                   self.obj_imagens.pmae_b550m,
                   self.obj_imagens.pmae_h610m, self.obj_imagens.pmae_b560m]
            i = id_h % 10
            img = ram[i]
        elif 499 < id_h < 504:
            ram = [self.obj_imagens.hdd_purple,
                   self.obj_imagens.hdd_blue,
                   self.obj_imagens.ssd_kingston, self.obj_imagens.ssd_green]
            i = id_h % 10
            img = ram[i]
        elif 599 < id_h < 604:
            ram = [self.obj_imagens.f_thermaltake_t,
                   self.obj_imagens.f_thermaltake_s,
                   self.obj_imagens.f_scoolerm, self.obj_imagens.f_reddragon]
            i = id_h % 10
            img = ram[i]

        return img

    def destruir(self, local):
        for widget in local.winfo_children():
            widget.destroy()
        self.frame1_tela1.destroy()

    def frame(self):
        self.frame1_tela1 = Frame(
            self.main_window, width=700, height=648, bg='#000000'
        )
        self.frame1_tela1.pack(side=RIGHT, padx=5)

    def safe_reset(self):
        if self.voltar_tela:
            if self.qtd_p:
                self.qtd_p.destroy()
            if self.obj_carrinho.id:
                self.obj_carrinho.id.clear()
                self.obj_carrinho.qtd.clear()
            self.destruir(self.frame1_tela1)

        else:
            self.voltar_tela = True

    def sair(self):
        resultado = messagebox.askyesno("Alerta!", "DESEJA SAIR?")
        if resultado:
            for widget in self.main_window.winfo_children():
                widget.destroy()

            self.main_window.unbind('<Return>')
            if self.voltar_tela:
                self.frame1_tela1.destroy()
            self.logado = ""
            self.tela_1()
            self.voltar_tela = False

    def voltar(self, id_h):
        self.destruir(self.frame1_tela1)
        self.voltar_tela = False

        if 99 < id_h < 104:
            self.processadores()
        elif 199 < id_h < 204:
            self.ram()
        elif 299 < id_h < 304:
            self.gpu()
        elif 399 < id_h < 404:
            self.pmae()
        elif 499 < id_h < 504:
            self.memoria2()
        elif 599 < id_h < 604:
            self.fonte()

# -----------------------------------
if __name__ == "__main__":
    window = Tk()
    window.geometry("1080x720")
    window.resizable(False, False)

    app = AppGui(window)
    window.mainloop()
