# flake8: noqa
import tkinter as tk
from calendar import monthrange
from datetime import datetime, timedelta, date
##from tkinter import PhotoImage, ttk, messagebox,RAISED, RIDGE
from tkinter import messagebox, ttk

import bcrypt
import holidays
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry

import bd_sistemas_de_escala as bd


class Screens:
    def __init__(self, master):
        self.login_screen = master
        self.login_screen.title("Login")
        self.login_screen.geometry('961x573')
        self.login_screen.configure(bg='#D9D9D9')
        self.login_screen.resizable(False, False)

        self.top_frm = tk.Frame(self.login_screen, height=100, width=100, bg='#94939B')
        self.top_frm.pack(fill=tk.X, padx=20, pady=20)

        self.top_lbl = tk.Label(self.top_frm, text = "BEM VINDO", font=('Inter',28,'bold'), fg='#0B0B0B', bg='#94939B')
        self.top_lbl.pack(side=tk.TOP, pady=10, padx=50)

        self.left_frm = tk.Frame(self.login_screen,bg='#D9D9D9')
        self.left_frm.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=10)

        #self.img_pf = tk.PhotoImage(file="images/image 1.png", height=425, width=336)
        self.img_pf = ImageTk.PhotoImage(Image.open(f"images/image1.png"))

        self.left_lbl = tk.Label(self.left_frm, image=self.img_pf, height=425, width=336, bg='#D9D9D9')
        self.left_lbl.pack(side=tk.LEFT, pady=10, padx=50,fill=tk.BOTH,expand=True)

        self.left_lbl.configure(image=self.img_pf)
        self.left_lbl.image=self.img_pf

        self.right_frm = tk.Frame(self.login_screen, width=421, height=542)
        self.right_frm.pack(side=tk.LEFT, fill=tk.Y, expand=True, padx=20, pady=20)

        self.right_lbl = tk.Label(self.right_frm, bg='#94939B')
        self.right_lbl.pack(side=tk.LEFT, fill=tk.BOTH)

        self.text_lbl = tk.Label(self.right_lbl, bg='#94939B', text='LOGIN', font=('Inter', 24, 'bold'), fg='#0B0B0B')
        self.text_lbl.pack(side=tk.TOP, pady=30, padx=20)

        self.entry_nome = tk.Entry(self.right_lbl, width=200, bg='#D9D9D9', justify="center", font=('Inter', 24 , 'bold'), fg='#94939B')
        self.entry_nome.insert(0, "Nome de Usuario")
        self.entry_nome.bind("<FocusIn>", self.limpar_entry)
        self.entry_nome.bind("<FocusOut>", self.restaurar_entry)
        self.entry_nome.pack(side=tk.TOP, pady=20, padx=20)

        self.entry_senha = tk.Entry(self.right_lbl, width=200, bg='#D9D9D9', justify="center",font=('Inter', 24, 'bold'), fg='#94939B', show='*')
        self.entry_senha.insert(0, "Senha")
        self.entry_senha.bind("<FocusIn>", self.limpar_entry)
        self.entry_senha.bind("<FocusOut>", self.restaurar_entry)
        self.entry_senha.pack(side=tk.TOP, pady=20, padx=20)

        self.bttn_login = tk.Button(self.right_lbl, font=('Inter', 24, 'bold'), fg='#FFFFFF', text="ENTRAR", bg='#6A6666', command=self.confirm_login, borderwidth=0)
        self.bttn_login.pack(side=tk.TOP, pady=10, padx=100)

        # self.bttn_help = tk.Button(self.right_lbl, font=('Inter', 20, 'bold'), fg='#6A6666', text=" Escalas ", bg='#94939B', borderwidth=0,command=self.Escalas)
        # self.bttn_help.pack(fill=tk.BOTH)
        # self.bttn_help.config()
        #self.verifica_termino_escalas()
        self.DIAS = [
        'Segunda-feira',
        'Terça-feira',
        'Quarta-feira',
        'Quinta-Feira',
        'Sexta-feira',
        'Sábado',
        'Domingo'
        ]

    def confirm_login(self):
        nome = self.entry_nome.get()
        senha = self.entry_senha.get().encode("utf-8")
        if nome == "":
            messagebox.showinfo("Insira o nome", "O campo nome está vazio!")
        elif senha == "":
            messagebox.showinfo("Insira a senha", "O campo senha está vazio!")
        else:
            query = 'SELECT nome_usuario, senha, super_usuario FROM usuario;'
            valores = bd.consultar(query)
            logado = False
            for i in valores:
                if i[0] == nome:
                    hash = i[1][2:len(i[1]) - 1].encode("utf-8")
                    if bcrypt.checkpw(senha, hash):
                        logado = True
                        self.user_logged = i[2]
            if logado:
                if self.user_logged == 1:
                    self.enter()
                else:
                    self.enter()  # MODIFICAR PARA TELA DE USUARIO COMUM
            else:
                messagebox.showinfo("Dados incorretos", "Usuário ou senha inválido")


    def limpar_entry(self, event):
        entry = event.widget
        if entry.get() == "Nome de Usuario" or entry.get() == "Senha":
            entry.delete(0, tk.END)

    def restaurar_entry(self, event):
        entry = event.widget
        if not entry.get():
            if entry == self.entry_nome:
                entry.insert(0, "Nome de Usuario")
            elif entry == self.entry_senha:
                entry.insert(0, "Senha")

    def enter(self):
        self.login_screen.destroy()
        self.MainScreen()

    def MainScreen(self):
        self.main_screen = tk.Tk()
        self.main_screen.title("Main Screen")
        self.main_screen.geometry('1253x588')
        self.main_screen.configure(bg='#D9D9D9')
        self.main_screen.resizable(False, False)

        self.main_frame = tk.Frame(self.main_screen,width=1253,height=588,bg='#94939B')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.right_frm_2 = tk.Frame(self.main_frame, bg='#565656', width=830, height=516)
        self.right_frm_2.pack(fill=tk.BOTH, expand=True, padx=20, pady=20, side=tk.RIGHT)

        self.left_frm_2 = tk.Frame(self.main_frame,bg='#94939B')
        self.left_frm_2.pack(padx=20, pady=20,side=tk.LEFT)

        self.top_lbl_02 = tk.Label(self.left_frm_2, text='CONTROLE DE ESCALAS',font=('Inter',18,'bold'),fg='#FFF', bg='#94939B')
        self.top_lbl_02.pack(side=tk.TOP)


        self.top_lbl_03 = tk.Label(self.left_frm_2, text='VERSÃO 1.0', font=('Inter', 10, 'bold'), fg='#FFF',bg='#94939B')
        self.top_lbl_03.pack(side=tk.TOP,padx=10)


        self.img_pf_02 = ImageTk.PhotoImage(Image.open(f"images/image1.png"))

        self.left_lbl_02 = tk.Label(self.left_frm_2, image=self.img_pf_02, height=425, width=336, bg='#94939B')
        self.left_lbl_02.pack(side=tk.TOP,padx=10,pady=10)

        self.img_calendar = ImageTk.PhotoImage(Image.open((f'images/calendar_icon.png')))
        self.img_user = ImageTk.PhotoImage(Image.open((f'images/user_icon.png')))
        self.img_roster = ImageTk.PhotoImage(Image.open((f'images/roster_icon.png')))
        self.img_roster_02 = ImageTk.PhotoImage(Image.open(f'images/roster_icon_02.png'))
        self.img_reports = ImageTk.PhotoImage(Image.open((f'images/chart-bar.png')))
        self.img_edit = ImageTk.PhotoImage(Image.open((f'images/calendar-minus.png')))


        self.top_frame = tk.Frame(self.right_frm_2,bg='#565656')
        self.top_frame.pack(side=tk.TOP,padx=10,pady=10,fill=tk.BOTH,expand=True)

        self.bottom_frame = tk.Frame(self.right_frm_2, bg='#565656')
        self.bottom_frame.pack(side=tk.BOTTOM,padx=10,pady=10,fill=tk.BOTH,expand=True)

        button_images = [
            (self.img_calendar, "Calendário", self.calendar),
            (self.img_reports, "Relatórios", self.reports),
            (self.img_user, "Usuários", self.user),
            # (self.img_roster, "Atribuir", self.roster),
            (self.img_roster_02, "Tipos de Escalas", self.type_manage),
            (self.img_edit, "Escalas", self.manage)
        ]
        button_width = max(img.width() for img, _, _ in button_images)

        for img, text, command in button_images:
            button = tk.Button(
                self.top_frame if command in [self.calendar, self.reports, self.user] else self.bottom_frame,
                bg='#6E716E',
                text=text,
                image=img,
                compound=tk.TOP,
                borderwidth=0,
                command=command,
                font=('Inter', 24, 'bold'),
                fg='#FFF',
                pady=20
            )
            button.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)
            button.config(width=button_width)

    # USER SCREEN
    def user(self):
        self.main_screen.destroy()
        self.UserScreen()

    def voltar_user(self):
        self.user_screen.destroy()
        self.MainScreen()

    def open_create_user(self):
        self.user_screen.iconify()
        self.CreateUserScreen()

    def open_edit_user(self):
        selecionado = self.tvw_usuario.selection()
        if selecionado != ():
            self.user_screen.iconify()
            self.EditUserScreen()

    def voltar_create_user(self):
        self.create_user.destroy()
        self.user_screen.deiconify()

    def voltar_edit_user(self):
        self.edit_user.destroy()
        self.user_screen.deiconify()
    # END User Screen

    # Manage Roster Screen
    def manage(self):
        self.main_screen.destroy()
        self.RosterManage()

    def voltar_manage(self):
        self.roster_manage.destroy()
        self.MainScreen()

    def create_roster(self):
        self.roster_manage.iconify()
        self.CreateRoster()

    def voltar_create_roster(self):
        self.create_roster_screen.destroy()
        self.roster_manage.deiconify()

    def edit_roster(self):
        selecionado = self.tvw_escala.selection()
        if selecionado != ():
            self.roster_manage.iconify()
            self.RosterEdit()

    def voltar_edit_roster(self):
        self.edit_roster_screen.destroy()
        self.roster_manage.deiconify()
    # END Manage Roster

    # Type Manage Screen
    def type_manage(self):
        self.main_screen.destroy()
        self.TypeManage()

    def create_type(self):
        self.type_manage_screen.iconify()
        self.CreateTypeScreen()

    def edit_type(self):
        selecionado = self.tvw_type_manage.selection()
        if selecionado != ():
            self.type_manage_screen.iconify()
            self.EditeTypeScreen()

    def type_edit_close(self):
        self.edite_type.destroy()
        self.type_manage_screen.deiconify()

    def type_close(self):
        self.create_screen.destroy()
        self.type_manage_screen.deiconify()

    def voltar_type_manage(self):
        self.type_manage_screen.destroy()
        self.MainScreen()

    def type_manage_close(self):
        self.type_manage_screen.destroy()
        self.MainScreen()
    # END Type Manage

    def roster(self):
        self.main_screen.destroy()
        self.RosterScreen()

    def voltar_roster(self):
        self.roster_screen.destroy()
        self.MainScreen()
    def voltar_escala(self):
        self.roster_screen.destroy()
        self.RosterManage()
    def calendar(self):
        self.main_screen.destroy()
        self.CalendarScreen()

    def voltar_calendar(self):
        self.calendar_screen.destroy()
        self.MainScreen()

    def reports(self):
        self.main_screen.destroy()
        self.ReportScreen()

    def voltar_create(self):
        self.create_screen.destroy()
        self.MainScreen()

    def voltar_report(self):
        self.report_screen.destroy()
        self.MainScreen()

    def voltar_escala(self):
            self.roster_screen.destroy()
            self.roster_manage.deiconify()

    def Atribuir_Escala(self, event):
        # print(self.text1.get())

        self.janela2 = tk.Toplevel()
        self.janela2.grab_set()
        self.janela2.title("Atribuir Escala")
        self.janela2.geometry("500x400")
        self.frm_janela2_c = tk.Frame(self.janela2, width=500, height=400)
        self.frm_janela2_c.grid(column=0, row=0)

        colunas = ["Nomes"]

        self.tvw = ttk.Treeview(self.janela2, columns=colunas, show="headings")
        self.tvw.place(x=290, y=10)

        self.tvw.heading(colunas[0], text=colunas[0])

        self.scr = ttk.Scrollbar(self.janela2, command=self.tvw.yview)
        self.tvw.configure(yscroll=self.scr.set)
        self.scr.place(x=474, y=10)

        query = 'SELECT usuario_id, nome_completo, nome_usuario FROM usuario;'
        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw.insert('', tk.END, values=(tupla[1],))

        self.lbl_Periodo = tk.Label(self.frm_janela2_c, text="Periodo:")
        self.lbl_Periodo.place(x=20, y=110)
        # Exemplos de Periodos

        self.cal_escolha = Calendar(self.frm_janela2_c, locale='pt_BR', date_pattern='dd/MM/yyyy')
        self.cal_escolha.place(x=40, y=150)

        self.btn_ok = tk.Button(self.frm_janela2_c, text='Atribuir', command=self.Atribuir)
        self.btn_ok.place(x=100, y=350)

    def RosterScreen(self):
        self.roster_screen = tk.Tk()
        self.roster_screen.title("Escalas")
        self.roster_screen.geometry('1253x588')
        self.roster_screen.configure(bg='#D9D9D9')
        self.roster_screen.resizable(False, False)
        self.roster_screen.protocol("WM_DELETE_WINDOW", self.voltar_roster)

        self.big_frame = tk.Frame(self.roster_screen, bg='#94939B')
        self.big_frame.pack(fill=tk.BOTH, expand=True, padx=20,pady=20)

        self.center_frame_02 = tk.Frame(self.big_frame, bg='#94939B')
        self.center_frame_02.pack(fill=tk.BOTH, expand=True, padx=10,pady=20,side=tk.LEFT)

        self.top_frame_02 = tk.Frame(self.center_frame_02, bg='#94939B')
        self.top_frame_02.pack(side=tk.TOP,fill=tk.BOTH)

        self.top_lbl_04 = tk.Label(self.top_frame_02, text='CALENDARIO DE ESCALAS', font=('Inter', 12, 'bold'),fg='#0B0B0B', bg='#94939B')
        self.top_lbl_04.pack(side=tk.TOP, pady=10, padx=10)

        self.middle_frame = tk.Frame(self.center_frame_02, bg='#94939B')
        self.middle_frame.pack(side=tk.TOP,fill=tk.Y,pady=10,padx=10)

        self.escalas_label = tk.Label(self.middle_frame, text='ESCALAS', font=('Inter', 10, 'bold'), fg='#FFF',
                                      bg='#94939B')
        self.escalas_label.pack(side=tk.LEFT, pady=1, padx=10, )

        self.string_Var_comb_tipo_p = tk.StringVar()

        query = 'SELECT nome_escala FROM escala;'
        dados = bd.consultar(query)
        self.Tipo_escala = []
        for tupla in dados:
            for escala in tupla:
                # print(escala)
                self.Tipo_escala.append(escala)

        combo_var = tk.StringVar()
        self.combo_box = ttk.Combobox(self.middle_frame, values=self.Tipo_escala, state="readonly", font="30", width=28,
                                      height=5, textvariable=self.string_Var_comb_tipo_p)
        self.combo_box.bind("<<ComboboxSelected>>", self.Aualizações_Atribuir)
        self.combo_box.pack(pady=20, padx=20, side=tk.LEFT)
        self.combo_box.current(0)

        self.entry_dias_var = tk.StringVar()

        self.middle_label = tk.Label(self.middle_frame, text='DIAS', font=('Inter', 10, 'bold'), fg='#FFF',bg='#94939B')
        self.middle_label.pack(side=tk.LEFT, pady=10, padx=10,)

        self.entry_dias = tk.Entry(self.middle_frame, textvariable=self.entry_dias_var, width=3, state="readonly")
        self.entry_dias.pack(side=tk.LEFT, pady=10, padx=10)

        self.bttn_edit = tk.Button(self.middle_frame, text='EDITAR', font=('Inter', 10, 'bold'), fg='#FFF',bg='#FF7F50',command='')
        self.bttn_edit.pack(side=tk.LEFT, pady=10, padx=10)

        self.calendar_frame_02 = tk.Frame(self.center_frame_02)
        self.calendar_frame_02.pack(side=tk.TOP,expand=True,fill=tk.BOTH)

        self.cal_atrib = Calendar(self.calendar_frame_02, locale='pt_BR', date_pattern='dd/MM/yyyy')
        self.cal_atrib.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.calendar_ferias(2)     

        self.bottom_frame_02 = tk.Frame(self.center_frame_02)
        self.bottom_frame_02.pack(side=tk.TOP,pady=10)

        self.bttn_voltar = tk.Button(self.bottom_frame_02, text='VOLTAR', font=('Inter', 10, 'bold'), fg='#605F5F', bg='#FFF',command=self.voltar_roster,borderwidth=0)
        self.bttn_voltar.pack(side=tk.LEFT)

        self.frame_right = tk.Frame(self.big_frame,bg='#94939B')
        self.frame_right.pack(fill=tk.BOTH, expand=True, padx=20, pady=20,side=tk.LEFT)

        self.top_lbl_05 = tk.Label(self.frame_right, text='ATRIBUIR FUNCIONARIO', font=('Inter', 12, 'bold'),fg='#0B0B0B', bg='#94939B')
        self.top_lbl_05.pack(side=tk.TOP, pady=3, padx=10)

        self.frame_pesquisa = tk.Frame(self.frame_right,bg='#94939B')
        self.frame_pesquisa.pack(fill=tk.Y, expand=True, padx=20, pady=10,side=tk.TOP)

        self.entry_pesquisa = tk.Entry(self.frame_pesquisa,width=49,font=('Inter', 10 , 'bold'), fg='#94939B')
        self.entry_pesquisa.pack(side=tk.LEFT,pady=10,fill=tk.X)
        self.entry_pesquisa.insert(0, "Pesquisar")

        self.entry_pesquisa.bind("<FocusIn>", self.limpar_entry_entry_pesquisa)
        self.entry_pesquisa.bind("<FocusOut>", self.restaurar_entry_pesquisa)

        self.none1 = tk.Label(self.frame_pesquisa, text="", width=1, bg="#94939B")
        self.none1.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.image_pesquisa = tk.PhotoImage(file="images/lupa.png")
        self.bttn_pesquisa = tk.Button(self.frame_pesquisa, text="O", image=self.image_pesquisa, width=16,
                                  command=self.pesquisar_tree_users)
        self.bttn_pesquisa.pack(side=tk.LEFT,pady=10,fill=tk.X)

        self.none = tk.Label(self.frame_pesquisa, text="", width=1, bg="#94939B")
        self.none.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.image_refresh = tk.PhotoImage(file="images/refresh.png")
        self.bttn_refresh = tk.Button(self.frame_pesquisa, text="O", image=self.image_refresh, width=16,
                                  command=self.atualizar_tree_users)
        self.bttn_refresh.pack(side=tk.LEFT,pady=10,fill=tk.X)

        self.frame_tvw_usuario_01 = tk.Frame(self.frame_right,bg='#94939B')
        self.frame_tvw_usuario_01.pack(side=tk.TOP, expand=True,fill=tk.Y)

        self.tree = ttk.Treeview(self.frame_tvw_usuario_01, columns=("Nome"), show="headings")
        self.tree.column('Nome', width=400)
        self.tree.heading("Nome", text="Nome Completo")
        self.tree.pack(side=tk.LEFT,fill=tk.BOTH,pady=10,expand=True)

        self.atualizar_tree_users()

        self.scrollbar = ttk.Scrollbar(self.frame_tvw_usuario_01, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side=tk.LEFT,fill=tk.BOTH,pady=10)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.frame_btn = tk.Frame(self.frame_right,bg='#94939B')
        self.frame_btn.pack(side=tk.TOP,expand=True,fill=tk.X,pady=10)

        self.btt_add = tk.Button(self.frame_btn,text='ATRIBUIR',font=('Inter', 10, 'bold'), fg='#070707',bg='#D9D9D9',command=self.Atribuir,borderwidth=0)
        self.btt_add.pack(side=tk.TOP)
        self.Aualizações_Atribuir(1)

    def pesquisar_tree_users(self):
        busca = self.entry_pesquisa.get()
        for i in self.tree.get_children():
            self.tree.delete(i)
        if busca == '' or busca == "Pesquisar":
            self.atualizar_tree_users()
        else:
            query = f"SELECT nome_completo FROM usuario WHERE nome_completo LIKE '{busca}%';"
            dados = bd.consultar(query)
            for tupla in dados:
                self.tree.insert('', tk.END, values=tupla)

    def atualizar_tree_users(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        query = 'SELECT nome_completo FROM usuario;'
        dados = bd.consultar(query)
        for tupla in dados:
            self.tree.insert('', tk.END, values=tupla)

    def Aualizações_Atribuir(self, event):
        self.cal_atrib.calevent_remove("all")
        query = f'SELECT dias_escala FROM escala Where nome_escala Like "{self.combo_box.get()}";'
        dados = bd.consultar(query)
        for dias_escala in dados:
            pass
        self.entry_dias_var.set(dias_escala[0])

        self.tree.delete(*self.tree.get_children())

        query = 'SELECT nome_completo FROM usuario;'
        dados = bd.consultar(query)
        for tupla in dados:
            self.tree.insert('', tk.END, values=tupla)

        query = f'SELECT escala_id FROM escala Where nome_escala Like "{self.combo_box.get()}";'
        dados = bd.consultar(query)
        dados = dados[0]
        id = dados[0]

        query = f'SELECT data_inicio FROM usuario_escala Where escala_id = {id};'
        datas = bd.consultar(query)
        self.calendar_ferias(2)

        query = f'SELECT tipo_escala_id FROM escala Where escala_id = {id};'
        dados = bd.consultar(query)
        dados = dados [0]
        id_tipo_escala = dados[0]
        query = f'SELECT finais_semana, feriados FROM tipo_escala Where tipo_escala_id = {id_tipo_escala};'
        dados = bd.consultar(query)
        dados = dados[0]

        finais_semana = dados[0]
        feriados = dados[1]
        
        for data in datas:
            data_evento = datetime.strptime(data[0], "%d/%m/%Y")
            # print(data_evento)
            começo = 1
            cont_dias = dias_escala[0]
            while cont_dias != 0:

                if começo == 1:
                    data_evento = data_evento + timedelta(days=0)
                else:
                    data_evento = data_evento + timedelta(days=1)
                self.cal_atrib.calevent_create(data_evento , f'Dias_Das_Escalas', f'Dias_Das_Escalas')
                # print(cont_dias)
                cont_dias -= 1
                começo = 0
                if finais_semana != 1:
                    data = date(data_evento.year, data_evento.month, data_evento.day)
                    indice_da_semana = data.weekday()
                    dia_da_semana = self.DIAS[indice_da_semana]
                    numero_do_dia_da_semana = data.isoweekday()
                    if(numero_do_dia_da_semana == 6 or numero_do_dia_da_semana == 7 ):
                        cont_dias += 1
                        self.cal_atrib.calevent_create(data_evento , 'Cor_padrão', 'Cor_padrão')
                        self.cal_atrib.tag_config("Cor_padrão", background="#cccccc", foreground='black')

            self.cal_atrib.tag_config('Dias_Das_Escalas', background="#FFFACD", foreground='black')
        
        if feriados != 1:
            self.calendar_ferias(2)


    def limpar_entry_entry_pesquisa(self, event):
        entry = event.widget
        if entry.get() == "Pesquisar":
            entry.delete(0, tk.END)

    def restaurar_entry_pesquisa(self, event):
        entry = event.widget
        if not entry.get():
            if entry == self.entry_pesquisa:
                entry.insert(0, "Pesquisar")

    def Atribuir(self):
        selecionado = self.tree.selection()
        lista = self.tree.item(selecionado, "values")
        for nome in lista:
            nome = nome
        # print(self.cbx_usuario.get())
        # print(self.cbx_tipo_escala.get())
        # print(self.cal_escolha.selection_get())
        query = f'''SELECT usuario_id, escala_id FROM escala, usuario 
        WHERE nome_escala LIKE "{self.combo_box.get()}" and nome_completo LIKE "{nome}";'''
        dados = bd.consultar(query)

        ids = []

        for tupla in dados:
            for id in tupla:
                ids.append(id)

        usuario_id = ids[0]
        escala_id = ids[1]
        data_inicio = self.cal_atrib.get_date()

        query = 'SELECT data_inicio_escala, data_fim_escala, dias_escala FROM escala;'
        dados = bd.consultar(query)

        query = f'INSERT INTO usuario_escala ("usuario_id", "escala_id", "data_inicio") VALUES ("{usuario_id}", {escala_id}, "{data_inicio}");'
        bd.inserir(query)
        self.voltar_roster()

    def CalendarScreen(self):
        self.calendar_screen = tk.Tk()
        self.calendar_screen.title("Calendario")
        self.calendar_screen.geometry('1253x688')
        self.calendar_screen.configure(bg='#D9D9D9')
        ##self.calendar_screen.resizable(False, False)
        self.calendar_screen.protocol("WM_DELETE_WINDOW", self.voltar_calendar)

        self.center_frame = tk.Frame(self.calendar_screen, bg='#94939B')
        self.center_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.config_frame = tk.Frame(self.center_frame,bg='#94939B')
        self.config_frame.pack(side=tk.TOP, padx=20,pady=10 ,fill=tk.X)

        self.lbl_text = tk.Label(self.config_frame, text='CALENDARIO GERAL DE ESCALAS', font=('Inter', 18, 'bold'),
                                fg='#0B0B0B', bg='#94939B')
        self.lbl_text.pack(side=tk.TOP, pady=5)

        self.lbl_nome = tk.Label(self.config_frame, text='Nome:', font=('Inter', 18, 'bold'),fg='#0B0B0B', bg='#94939B')
        self.lbl_nome.pack(side=tk.LEFT, pady=5)

        query = f'SELECT nome_completo FROM usuario;'
        dados = bd.consultar(query)

        usu = []

        for tupla in dados:
            for usuario in tupla:
                usu.append(usuario)
        # print(usu)

        self.cbx_nome = ttk.Combobox(self.config_frame, text='Nome', values=usu, state="readonly")
        self.cbx_nome.pack(side=tk.LEFT,expand=True,fill=tk.X,padx=(5,40),pady=2)
        self.cbx_nome.current(0)

        self.lbl_escala = tk.Label(self.config_frame, text='Escala:', font=('Inter', 18, 'bold'), fg='#0B0B0B',bg='#94939B')
        self.lbl_escala.pack(side=tk.LEFT, pady=5)

        query = f'SELECT nome_escala FROM escala;'
        dados = bd.consultar(query)

        escala = []

        for tupla in dados:
            for usuario in tupla:
                escala.append(usuario)
        # print(escala)

        self.cbx_cargo = ttk.Combobox(self.config_frame,text='Escalas', values=escala, state="readonly")
        self.cbx_cargo.pack(side=tk.LEFT,expand=True,fill=tk.X,padx=(5.40),pady=2)
        self.cbx_cargo.current(0)

        self.calendar_frame = tk.Frame(self.center_frame,bg='#94939B')  ## Usem esse frame para colocar o calendario principal
        self.calendar_frame.pack(side=tk.TOP, padx=20, fill=tk.BOTH, expand=True)

        self.cal_show = Calendar(self.calendar_frame, locale='pt_BR', date_pattern='dd/MM/yyyy')
        self.cal_show.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.buttons_frame = tk.Frame(self.center_frame, bg='#94939B')
        self.buttons_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.bttn_back = tk.Button(self.buttons_frame, text='VOLTAR', font=("Arial", 10, "bold"), bg="#FFF", fg="#000",command=self.voltar_calendar, borderwidth=0)
        self.bttn_back.pack(side=tk.LEFT, pady=10, padx=15)

        self.bttn_verificar = tk.Button(self.buttons_frame,text='VERIFICAR', font=("Arial", 10, "bold"), bg="#3CB371",fg="white",command=self.Aplica_Calendario,borderwidth=0)
        self.bttn_verificar.pack(side=tk.LEFT, pady=10, padx=15)
        self.calendar_ferias(1)


    def calendar_ferias(self, numb):
        if numb == 1:
            cor_escolhida_ferias = "#FF7F50"
            date = self.cal_show.datetime.today()
            # print(date)
            feriados= holidays.Brazil()
            ano_feriado = str(date).split("-")[0]
            vetor_feriados = []
            for feriado in feriados[f"{ano_feriado}-01-01": f'{ano_feriado}-12-31']:
                dia = str(feriado).split("-")[2]
                mes = str(feriado).split("-")[1]
                ano = str(feriado).split("-")[0]
                feriados = self.cal_show.datetime(year=int(ano), month=int(mes), day=int(dia))
                #print(feriados)
                vetor_feriados.append(feriados)
            for feriados1 in vetor_feriados:
                self.cal_show.calevent_create(feriados1 , 'Ferias', 'Ferias')
            self.cal_show.tag_config('Ferias', background=cor_escolhida_ferias, foreground='white')

        elif numb == 2:
                cor_escolhida_ferias = "#FF7F50"
                date = self.cal_atrib.datetime.today()
                # print(date)
                feriados= holidays.Brazil()
                ano_feriado = str(date).split("-")[0]
                vetor_feriados = []
                for feriado in feriados[f"{ano_feriado}-01-01": f'{ano_feriado}-12-31']:
                    dia = str(feriado).split("-")[2]
                    mes = str(feriado).split("-")[1]
                    ano = str(feriado).split("-")[0]
                    feriados = self.cal_atrib.datetime(year=int(ano), month=int(mes), day=int(dia))
                    #print(feriados)
                    vetor_feriados.append(feriados)
                for feriados1 in vetor_feriados:
                    self.cal_atrib.calevent_create(feriados1 , 'Ferias', 'Ferias')
                self.cal_atrib.tag_config('Ferias', background=cor_escolhida_ferias, foreground='white')
    


    def Aplica_Calendario(self):
        self.cal_show.calevent_remove("all")
        query = f'''SELECT eu.escala_usuario_id
        FROM escala_usuario eu
        JOIN usuario u ON u.usuario_id = eu.usuario_id
        JOIN escala e ON e.escala_id = eu.escala_id
        WHERE u.nome_completo LIKE "{self.cbx_nome.get()}"
        AND e.nome_escala LIKE  "{self.cbx_cargo.get()}";'''

        # query = f"SELECT escala_usuario_id FROM escala_usuario_id WHERE  "

        dados = bd.consultar(query)
        # print(dados)
        self.escala_usuario_id = 0

        self.escala_usuario_id = dados[0][0]

        query = f"SELECT data_inicio, data_fim FROM escala_usuario WHERE escala_usuario_id = {self.escala_usuario_id}"
        dados = bd.consultar(query)
        # print(dados)

        if dados != [('', '')]:
            data_inicio_escala = datetime.strptime(str(dados[0][0]), '%d/%m/%Y')
            data_fim_escala = datetime.strptime(str(dados[0][1]), '%d/%m/%Y')

            # # Calcule o número de dias totais na escala
            dias_totais = (data_fim_escala - data_inicio_escala).days + 1
            data_evento = datetime.strptime(dados[0][0], "%d/%m/%Y").date()

            dias_totais_variavel = dias_totais

            while dias_totais_variavel != 0:

                data_evento = data_evento + timedelta(days=1)

                print(data_evento)
                self.cal_show.calevent_create(data_evento, f'Dias_Das_Escalas', f'Dias_Das_Escalas')
                
                dias_totais_variavel -= 1
            self.cal_show.tag_config('Dias_Das_Escalas', background="#FFFACD", foreground='black')

        #     data_evento = datetime.strptime(data[0], "%d/%m/%Y")
        #     # print(data_evento)
        #     começo = 1
        #     cont_dias = dias_escala[0]
        #     while cont_dias != 0:

        #         if começo == 1:
        #             data_evento = data_evento + timedelta(days=0)
        #         else:
        #             data_evento = data_evento + timedelta(days=1)
        #         self.cal_show.calevent_create(data_evento , f'Dias_Das_Escalas', f'Dias_Das_Escalas')
        #         # print(cont_dias)
        #         cont_dias -= 1
        #         começo = 0
        #         if finais_semana != 1:
        #             data = date(data_evento.year, data_evento.month, data_evento.day)
        #             indice_da_semana = data.weekday()
        #             dia_da_semana = self.DIAS[indice_da_semana]
        #             numero_do_dia_da_semana = data.isoweekday()
        #             if(numero_do_dia_da_semana == 6 or numero_do_dia_da_semana == 7 ):
        #                 cont_dias += 1
        #                 self.cal_show.calevent_create(data_evento , 'Cor_padrão', 'Cor_padrão')
        #                 self.cal_show.tag_config("Cor_padrão", background="#cccccc", foreground='black')

        #     self.cal_show.tag_config('Dias_Das_Escalas', background="#FFFACD", foreground='black')
        
        # if feriados != 1:
        #     self.calendar_ferias(2)




        # # print(self.id_usu_escala)
        # self.calendar_ferias(1)
        # if self.id_usu_escala != 0:
        #     # print(self.id_usu_escala)
        #     query = f'SELECT data_inicio FROM usuario_escala WHERE usuario_escala_id = {self.id_usu_escala};'
        #     dados = bd.consultar(query)
        #     dados = dados[0]

        #     for data_escala in dados:
        #         pass
        #     data_escala = str(data_escala)
        #     data_escala = data_escala.split("/")

        #     query = f'''SELECT e.dias_escala
        #     FROM usuario_escala ue
        #     JOIN escala e ON ue.escala_id = e.escala_id
        #     WHERE ue.usuario_escala_id = {self.id_usu_escala}'''
        #     dados = bd.consultar(query)
        #     dados = dados[0]
        #     for dias_de_escala in dados:
        #         pass
        #     # print(dias_de_escala)

        #     query = f''' 
                    
        #             '''

        #     query = f'''SELECT ts.feriados, ts.finais_semana
        #     FROM usuario_escala AS ue
        #     JOIN escala AS e ON ue.escala_id = e.escala_id
        #     JOIN tipo_escala AS ts ON e.tipo_escala_id = ts.tipo_escala_id
        #     WHERE ue.usuario_escala_id = {self.id_usu_escala}'''
        #     dados = bd.consultar(query)
        #     for contar_finais_semana, conta_feriados in dados:
        #         pass
        #     print(conta_feriados)
        #     print(contar_finais_semana)

        #     mes_escolha = int(data_escala[1])
        #     ano_escolha = int(data_escala[2])
        #     dia_escolha = int(data_escala[0])
        #     cor_escolhida_escala = "#FFFACD"
        #     vetor_dias_corridos_na_escala = []
        #     vetor_finais_semana = []
        #     dia_cont = dia_escolha

        #     procura_final_semana = dias_de_escala
            
        #     year = ano_escolha
        #     month = mes_escolha

        #     if contar_finais_semana == 0:
        #         while procura_final_semana > 0:
        #             day = dia_cont
        #             # print(dia_cont)

        #             # print(year, month, day)
        #             data_ = datetime(year, month, day)
        #             # monthrange retorna o último dia do mês, basta setá-lo na data e pronto
        #             Ultimo_dia_mes = data_.replace(day=monthrange(data_.year, data_.month)[1])

        #             data_ = datetime(year, 12, day)
        #             # monthrange retorna o último dia do mês, basta setá-lo na data e pronto
        #             Ultimo_dia_ano = data_.replace(day=monthrange(data_.year, data_.month)[1])


        #             data = datetime(year, month, day)
        #             # print(data)   


        #             indice_da_semana = data.weekday()
        #             # print(indice_da_semana)


        #             dia_da_semana = self.DIAS[indice_da_semana]
        #             # print(dia_da_semana)

        #             numero_do_dia_da_semana = data.isoweekday()
        #             # print(numero_do_dia_da_semana)
                
        #             if(numero_do_dia_da_semana == 6 or numero_do_dia_da_semana == 7 ):
        #                 # print("Final de semana")
        #                 vetor_finais_semana.append(data)
        #                 dias_de_escala += 1
        #                 procura_final_semana +=1
        #                 # print(data)

        #             if dia_cont == 28 or dia_cont == 29 or dia_cont == 30 or dia_cont == 31 or dia_cont == 32:
        #                 if dia_cont == Ultimo_dia_mes.day:
        #                     month += 1
        #                     dia_cont = 0
        #                 if Ultimo_dia_ano.day > year:
        #                     year +=1
                        

        #             dia_cont += 1
        #             procura_final_semana -=1


        #     #data atual =  date = cal.datetime.today()

        #     escala_ecolha_dia = self.cal_show.datetime(ano_escolha, mes_escolha, dia_escolha)
        #     #print(escala_ecolha_dia)

        #     #pegando todos os dias escolhidos na escala para comparar depois com as ferias
        #     dias = 0
        #     aux_dias_de_escala = dias_de_escala
        #     while dias < aux_dias_de_escala:
        #         # print(dia_escolha + dias)
        #         data_ = datetime(ano_escolha, mes_escolha, dia_escolha + dias)
        #         # monthrange retorna o último dia do mês, basta setá-lo na data e pronto
        #         Ultimo_dia_mes = data_.replace(day=monthrange(data_.year, data_.month)[1])
        #         if dia_escolha + dias == Ultimo_dia_mes.day:
        #             mes_escolha += 1
        #             dia_escolha = 1

        #         dias_corridos_na_escala = self.cal_show.datetime(ano_escolha, mes_escolha, dia_escolha + dias)
        #         #print(dias_corridos_na_escala)
        #         vetor_dias_corridos_na_escala.append(dias_corridos_na_escala)

        #         aux_dias_de_escala -=1
        #         dias +=1

        #     for i in range(0, dias_de_escala):
        #         self.cal_show.calevent_create(escala_ecolha_dia + self.cal_show.timedelta(days=i), 'escalas', 'escala')

        #     if conta_feriados == 0:
        #         self.calendar_ferias(1)

        #     for final_semana in vetor_finais_semana:
        #         self.cal_show.calevent_create(final_semana, "final_semana", "final_semana")
            
            
        #     self.cal_show.tag_config('escala', background=cor_escolhida_escala, foreground='black')
        #     self.cal_show.tag_config("final_semana", background="#cccccc", foreground='black')
            
            
        #     # print(dia_escolha, ano_escolha, mes_escolha, dias_de_escala)

    def UserScreen(self):
        self.user_screen = tk.Tk()
        self.user_screen.title("Usuarios")
        self.user_screen.geometry('800x620')
        self.user_screen.configure(bg='#D9D9D9')
        self.user_screen.resizable(False, False)
        self.user_screen.protocol("WM_DELETE_WINDOW", self.voltar_user)

        self.frame_top = tk.Frame(self.user_screen, bg='#94939B')
        self.frame_top.pack(side=tk.TOP, padx=10, fill=tk.X, pady=(10, 0))

        self.lbl_name = tk.Label(self.frame_top, text='GERENCIAR USUÁRIOS', font=('Inter', 18, 'bold'), fg='#0B0B0B',
                                 bg='#94939B')
        self.lbl_name.pack(side=tk.TOP, pady=(20, 10))

        self.lbl_filtro = tk.Label(self.frame_top, text='Filtro:', font=('Inter', 12, 'bold'), fg='#0B0B0B',
                                   bg='#94939B')
        self.lbl_filtro.pack(side=tk.LEFT, pady=5, padx=(20, 5))

        self.cbx_cargo = ttk.Combobox(self.frame_top, text='ID', values=("Nome", "Nome de Usuário", "Super usuário",), state="readonly")
        self.cbx_cargo.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 10), pady=2)

        self.image_pesquisa_filtro = tk.PhotoImage(file="images/lupa.png")
        self.bttn_pesquisa_filtro = tk.Button(self.frame_top, text="O", image=self.image_pesquisa_filtro, width=16,
                                       command=self.filtro_tvw_users)
        self.bttn_pesquisa_filtro.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.none = tk.Label(self.frame_top, text="", width=1, bg="#94939B")
        self.none.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.image_refresh_filtro = tk.PhotoImage(file="images/refresh.png")
        self.bttn_refresh_filtro = tk.Button(self.frame_top, text="O", image=self.image_refresh_filtro, width=16,
                                      command=self.update_tvw_user)
        self.bttn_refresh_filtro.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.lbl_opt = tk.Label(self.frame_top, text='Pesquisar:', font=('Inter', 12, 'bold'), fg='#0B0B0B',
                                bg='#94939B')
        self.lbl_opt.pack(side=tk.LEFT, pady=5, padx=(10, 5))

        self.entry_search = tk.Entry(self.frame_top)
        self.entry_search.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 10), pady=5)

        self.image_pesquisa = tk.PhotoImage(file="images/lupa.png")
        self.bttn_pesquisa = tk.Button(self.frame_top, text="O", image=self.image_pesquisa, width=16,
                                       command=self.pesquisar_tvw_users)
        self.bttn_pesquisa.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.none = tk.Label(self.frame_top, text="", width=1, bg="#94939B")
        self.none.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.image_refresh = tk.PhotoImage(file="images/refresh.png")
        self.bttn_refresh = tk.Button(self.frame_top, text="O", image=self.image_refresh, width=16,
                                      command=self.update_tvw_user)
        self.bttn_refresh.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.none2 = tk.Label(self.frame_top, text="", width=1, bg="#94939B")
        self.none2.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.frm = tk.Frame(self.user_screen, bg='#94939B')
        self.frm.pack(side=tk.TOP, pady=(0, 10), padx=10, expand=True, fill=tk.BOTH)

        self.frame_tvw_usuario = tk.Frame(self.frm, bg='#94939B')
        self.frame_tvw_usuario.pack(pady=20, padx=20, expand=True, fill=tk.BOTH)

        self.tvw_usuario = ttk.Treeview(self.frame_tvw_usuario, columns=('id', 'nome', 'nome de usuario', 'tipo'),
                                        show='headings')
        self.tvw_usuario.column('id', width=40)
        self.tvw_usuario.column('nome', width=250)
        self.tvw_usuario.column('nome de usuario', width=150)
        self.tvw_usuario.column('tipo', width=100)
        self.tvw_usuario.heading('id', text='Id')
        self.tvw_usuario.heading('nome', text='Nome')
        self.tvw_usuario.heading('nome de usuario', text='Nome de Usuário')
        self.tvw_usuario.heading('tipo', text='Super usuário')
        self.tvw_usuario.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.update_tvw_user()

        self.scr_usuario = ttk.Scrollbar(self.frame_tvw_usuario, command=self.tvw_usuario.yview)
        self.scr_usuario.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw_usuario.configure(yscroll=self.scr_usuario.set)

        self.frame_tvw_button = tk.Frame(self.frm, bg='#94939B')
        self.frame_tvw_button.pack(side=tk.BOTTOM)

        self.btn_cadastrar_usuario = tk.Button(self.frame_tvw_button, text="Criar Usuário", font=("Arial", 10, "bold"),
                                               bg="#3CB371", fg="white", width=20, height=1, borderwidth=0,
                                               command=self.open_create_user)
        self.btn_cadastrar_usuario.grid(row=0, column=0, padx=10, pady=10)

        self.btn_editar_usuario = tk.Button(self.frame_tvw_button, text="Editar Usuário", font=("Arial", 10, "bold"),
                                            bg="Orange", fg="white", width=20, height=1, borderwidth=0,
                                            command=self.open_edit_user)
        self.btn_editar_usuario.grid(row=0, column=1, padx=10, pady=10)

        self.btn_excluir_usuario = tk.Button(self.frame_tvw_button, text="Excluir Usuário", font=("Arial", 10, "bold"),
                                             bg="#E1523F", fg="white", width=20, height=1, borderwidth=0,
                                             command=self.delete_user)
        self.btn_excluir_usuario.grid(row=0, column=2, padx=10, pady=10)

        self.btn_excluir_usuario = tk.Button(self.frame_tvw_button, text="Voltar", font=("Arial", 10, "bold"),
                                             bg="#FFF", fg="#000", width=20, height=1, borderwidth=0,
                                             command=self.voltar_user)
        self.btn_excluir_usuario.grid(row=0, column=3, padx=10, pady=10)

    def filtro_tvw_users(self):
        busca = self.cbx_cargo.get()
        for i in self.tvw_usuario.get_children():
            self.tvw_usuario.delete(i)
        if busca == '':
            self.update_tvw_user()
        elif busca == "Super usuário":
            query = f"SELECT usuario_id, nome_completo, nome_usuario, CASE WHEN super_usuario = 0 THEN 'Não' WHEN super_usuario = 1 THEN 'Sim' END AS super_usuario FROM usuario ORDER BY super_usuario"
            dados = bd.consultar(query)
            for tupla in dados:
                self.tvw_usuario.insert('', tk.END, values=tupla)
        elif busca == "Nome":
            query = f"SELECT usuario_id, nome_completo, nome_usuario, CASE WHEN super_usuario = 0 THEN 'Não' WHEN super_usuario = 1 THEN 'Sim' END AS super_usuario FROM usuario ORDER BY nome_completo"
            dados = bd.consultar(query)
            for tupla in dados:
                self.tvw_usuario.insert('', tk.END, values=tupla)
        else:
            query = f"SELECT usuario_id, nome_completo, nome_usuario, CASE WHEN super_usuario = 0 THEN 'Não' WHEN super_usuario = 1 THEN 'Sim' END AS super_usuario FROM usuario ORDER BY nome_usuario"
            dados = bd.consultar(query)
            for tupla in dados:
                self.tvw_usuario.insert('', tk.END, values=tupla)

    def pesquisar_tvw_users(self):
        busca = self.entry_search.get()
        for i in self.tvw_usuario.get_children():
            self.tvw_usuario.delete(i)
        if busca == '':
            self.update_tvw_user()
        else:
            query = f"SELECT usuario_id, nome_completo, nome_usuario, CASE WHEN super_usuario = 0 THEN 'Não' WHEN super_usuario = 1 THEN 'Sim' END AS super_usuario FROM usuario WHERE nome_completo LIKE '{busca}%';"
            dados = bd.consultar(query)
            for tupla in dados:
                self.tvw_usuario.insert('', tk.END, values=tupla)

    def update_tvw_user(self):
        for i in self.tvw_usuario.get_children():
            self.tvw_usuario.delete(i)
        query = f"SELECT usuario_id, nome_completo, nome_usuario, CASE WHEN super_usuario = 0 THEN 'Não' WHEN super_usuario = 1 THEN 'Sim' END AS super_usuario FROM usuario;"
        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw_usuario.insert('', tk.END, values=tupla)
        self.cbx_cargo.set("")
        self.entry_search.delete(0, "end")

    def CreateUserScreen(self):
        self.create_user = tk.Tk()
        self.create_user.title("Cadastrar usuario")
        self.create_user.geometry('462x676')
        self.create_user.configure(bg='#D9D9D9')
        self.create_user.resizable(False, False)

        self.lbl_name = tk.Label(self.create_user, text='CADASTRAR NOVO USUÁRIO', font=('Inter', 18, 'bold'), fg='#0B0B0B',bg='#D9D9D9')
        self.lbl_name.pack(side=tk.TOP,pady=(20,5))

        self.center_frame_04 = tk.Frame(self.create_user,bg='#94939B')
        self.center_frame_04.pack(pady=20,padx=20,expand=True,fill=tk.BOTH)

        tk.Label(self.center_frame_04, text="Nome Completo:", bg='#94939B',font=('Inter', 18, 'bold')).pack(side=tk.TOP,pady=10,padx=20)

        self.full_name_entry = tk.Entry(self.center_frame_04)
        self.full_name_entry.pack(side=tk.TOP,pady=10,padx=40,fill=tk.BOTH)

        tk.Label(self.center_frame_04, text="Nome de usuário:", bg='#94939B',font=('Inter', 18, 'bold')).pack(side=tk.TOP,pady=10,padx=20)

        self.username_entry = tk.Entry(self.center_frame_04)
        self.username_entry.pack(side=tk.TOP,pady=10,padx=40,fill=tk.BOTH)

        tk.Label(self.center_frame_04, text="Senha:", bg='#94939B',font=('Inter', 18, 'bold')).pack(side=tk.TOP,pady=10,padx=20)

        self.password_entry = tk.Entry(self.center_frame_04, show='*')
        self.password_entry.pack(side=tk.TOP,pady=10,padx=40,fill=tk.BOTH)

        tk.Label(self.center_frame_04, text="Confirmar senha:", bg='#94939B',font=('Inter', 18, 'bold')).pack(side=tk.TOP,pady=10,padx=20)
        self.confirm_password_entry = tk.Entry(self.center_frame_04, show='*')
        self.confirm_password_entry.pack(side=tk.TOP,pady=10,padx=40,fill=tk.BOTH)

        tk.Label(self.center_frame_04, text="Tipo de usuário:", bg='#94939B',font=('Inter', 18, 'bold')).pack(side=tk.TOP,pady=10,padx=20)

        self.user_type_var = tk.StringVar()
        self.user_type_combobox = ttk.Combobox(self.center_frame_04, textvariable=self.user_type_var,values=["Super Usuário", "Usuário Comum"])
        self.user_type_combobox.pack(side=tk.TOP,pady=10,padx=40,fill=tk.BOTH)
        self.user_type_combobox["state"] = "readonly"

        self.frm_bttn_03 = tk.Frame(self.center_frame_04, bg='#94939B')
        self.frm_bttn_03.pack(side=tk.BOTTOM, expand=True, padx=10, pady=10)

        self.btn_conf  = tk.Button(self.frm_bttn_03, text="Confirmar", command=self.confirm_create_user,font=("Arial", 10, "bold"), bg="#3CB371",fg="white", width=10, height=1,borderwidth=0).pack(side='left', padx=15,pady=10)
        self.btn_limp = tk.Button(self.frm_bttn_03, text="Limpar", command=self.clear_create_user, font=("Arial", 10, "bold"), bg="Orange", fg="white",width=10, height=1,borderwidth=0).pack(side='left', padx=15,pady=10)
        self.btn_cancel = tk.Button(self.frm_bttn_03, text="Cancelar", command=self.voltar_create_user, font=("Arial", 10, "bold"), bg="#E1523F",fg="white", width=10, height=1,borderwidth=0).pack(side='left', padx=15, pady=10)

    def clear_create_user(self):
        self.full_name_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.confirm_password_entry.delete(0, tk.END)
        self.user_type_combobox.set("")

    def confirm_create_user(self):
        full_name = self.full_name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get().encode('utf-8')
        conf_password = self.confirm_password_entry.get().encode('utf-8')
        type = self.user_type_combobox.get()

        # Criptografando a senha
        salt = bcrypt.gensalt(8)
        senha = bcrypt.hashpw(password, salt)
        conf_password = bcrypt.hashpw(conf_password, salt)

        uper_case = False
        for char in username:
            if char.isupper():
                uper_case = True

        if full_name == "":
            messagebox.showinfo("Insira um nome completo", "O campo nome completo está incorreto!")
            self.create_user.deiconify()
        elif username == "":
            messagebox.showinfo("Insira o nome de usuario", "O campo nome de usuário está incorreto!")
            self.create_user.deiconify()
        elif uper_case:
            messagebox.showinfo("Insira o nome de usuario minusculo", "O campo nome de usuário deve ser totalmente minusculo!")
            self.create_user.deiconify()
        elif password == "":
            messagebox.showinfo("Insira uma senha", "O campo senha está vazio!")
            self.create_user.deiconify()
        elif conf_password == "":
            messagebox.showinfo("Confirme a senha", "O campo de confirmação da senha está vazio!")
            self.create_user.deiconify()
        elif senha != conf_password:
            messagebox.showinfo("Senhas divergentes", "As senhas não correspondem")
            self.create_user.deiconify()
        elif type == "":
            messagebox.showinfo("Selecione um tipo", "Nenhum Tipo foi selecionado!")
            self.create_user.deiconify()
        else:
            query = 'SELECT nome_usuario FROM usuario;'
            valores = bd.consultar(query)
            confirmar = False
            for i in valores:
                if username == i[0]:
                    confirmar = True
                    break
            if not confirmar:
                if type == "Usuário Comum":
                    type = 0
                else:
                    type = 1
                query = f'INSERT INTO usuario ("nome_completo", "nome_usuario", "senha", "super_usuario") VALUES ("{full_name}", "{username}", "{password}", {type});'
                bd.inserir(query)
                messagebox.showinfo("SUCESSO!", "Usuário criado com sucesso!")
                self.update_tvw_user()
                self.create_user.destroy()
                self.user_screen.deiconify()
            else:
                messagebox.showinfo("Nome de usuário já cadastrado", "O Nome de usuário já cadastrado")
                self.create_user.deiconify()

    def EditUserScreen(self):
        self.selecionado = self.tvw_usuario.selection()
        self.lista = self.tvw_usuario.item(self.selecionado, "values")
        query = f"SELECT usuario_id, nome_completo, nome_usuario, senha, super_usuario FROM usuario WHERE usuario_id = {self.lista[0]};"
        self.lista = bd.consultar_usuarios(query)
        if self.selecionado != ():
            self.edit_user = tk.Toplevel()
            self.edit_user.title("Editar usuario")
            self.edit_user.geometry('462x676')
            self.edit_user.configure(bg='#D9D9D9')
            self.edit_user.resizable(False, False)

            self.lbl_name_02 = tk.Label(self.edit_user, text='EDITAR USUÁRIO', font=('Inter', 18, 'bold'), fg='#0B0B0B',bg='#D9D9D9')
            self.lbl_name_02.pack(side=tk.TOP,pady=(20,5))

            self.center_frame_05 = tk.Frame(self.edit_user,bg='#94939B')
            self.center_frame_05.pack(pady=20,padx=20,expand=True,fill=tk.BOTH)

            tk.Label(self.center_frame_05, text="Nome Completo:", bg='#94939B',font=('Inter', 18, 'bold')).pack(side=tk.TOP,pady=10,padx=20)

            self.full_name_entry = tk.Entry(self.center_frame_05)
            self.full_name_entry.pack(side=tk.TOP,pady=10,padx=40,fill=tk.BOTH)
            self.full_name_entry.insert(0, self.lista[1])

            tk.Label(self.center_frame_05, text="Nome de usuário:", bg='#94939B', font=('Inter', 18, 'bold')).pack(side=tk.TOP,pady=10,padx=20)
            self.username_entry = tk.Entry(self.center_frame_05)
            self.username_entry.pack(side=tk.TOP,pady=10,padx=40,fill=tk.BOTH)
            self.username_entry.insert(0, self.lista[2])

            tk.Label(self.center_frame_05, text="Tipo de usuário:", bg='#94939B', font=('Inter', 18, 'bold')).pack(side=tk.TOP,pady=10,padx=20)
            self.user_type_var = tk.StringVar()
            self.user_type_combobox = ttk.Combobox(self.center_frame_05, textvariable=self.user_type_var,values=["Usuário Comum", "Super Usuário"])
            self.user_type_combobox.pack(side=tk.TOP, pady=10, padx=40, fill=tk.BOTH)
            self.user_type_combobox["state"] = "readonly"
            self.user_type_combobox.current(self.lista[4])

            self.frm_bttn_02 = tk.Frame(self.center_frame_05,bg='#94939B')
            self.frm_bttn_02.pack(side=tk.BOTTOM,expand=True,padx=10,pady=10)

            self.btn_conf  = tk.Button(self.frm_bttn_02, text="Confirmar", command=self.confirm_edit_user,font=("Arial", 10, "bold"), bg="#3CB371",fg="white", width=10, height=1,borderwidth=0).pack(side='left', padx=15,pady=10)
            self.btn_limp = tk.Button(self.frm_bttn_02, text="Refazer", command=self.clear_edit_user, font=("Arial", 10, "bold"), bg="Orange", fg="white",width=10, height=1,borderwidth=0).pack(side='left', padx=15,pady=10)
            self.btn_cancel = tk.Button(self.frm_bttn_02, text="Cancelar", command=self.voltar_edit_user, font=("Arial", 10, "bold"), bg="#E1523F",fg="white", width=10, height=1,borderwidth=0).pack(side='left', padx=15, pady=10)

    def clear_edit_user(self):
        self.full_name_entry.delete(0, tk.END)
        self.full_name_entry.insert(0, self.lista[1])
        self.username_entry.delete(0, tk.END)
        self.username_entry.insert(0, self.lista[2])
        self.user_type_combobox.current(self.lista[4])

    def confirm_edit_user(self):
        self.selecionado = self.tvw_usuario.selection()
        self.lista = self.tvw_usuario.item(self.selecionado, "values")

        nome_completo = self.full_name_entry.get()
        nome_usuario = self.username_entry.get()
        # senha = self.entry_senha.get().encode('utf-8')
        # conf_senha = self.entry_confirmar_senha.get().encode('utf-8')
        tipo = self.user_type_combobox.get()
        uper_case = False
        for char in nome_usuario:
            if char.isupper():
                uper_case = True

        if nome_completo == "":
            messagebox.showinfo("Insira um nome completo", "O campo nome completo está incorreto!")
            self.edit_user.deiconify()
        elif nome_usuario == "":
            messagebox.showinfo("Insira o nome de usuario", "O campo nome de usuário está incorreto!")
            self.edit_user.deiconify()
        elif uper_case:
            messagebox.showinfo("Insira o nome de usuario minusculo",
                                "O campo nome de usuário deve ser totalmente minusculo!")
            self.edit_user.deiconify()
        elif tipo == "":
            messagebox.showinfo("Selecione um tipo", "Nenhum Tipo foi selecionado!")
            self.edit_user.deiconify()
        else:
            query = 'SELECT nome_usuario FROM usuario;'
            valores = bd.consultar(query)
            confirmar = False
            for i in valores:
                if nome_usuario == i[0] and i[0] != self.lista[2]:
                    confirmar = True
                    break
            if not confirmar:
                if tipo == "Usuário Comum":
                    tipo = 0
                else:
                    tipo = 1
                query = f'UPDATE usuario SET nome_completo="{nome_completo}", nome_usuario="{nome_usuario}", super_usuario="{tipo}" WHERE usuario_id={self.lista[0]};'
                bd.atualizar(query)
                messagebox.showinfo("SUCESSO!", "Usuário editado com sucesso!")
                self.update_tvw_user()
                self.edit_user.destroy()
                self.user_screen.deiconify()
            else:
                messagebox.showinfo("Nome de usuário já cadastrado", "O Nome de usuário já cadastrado")
                self.edit_user.deiconify()

    def delete_user(self):
        selecionado = self.tvw_usuario.selection()
        lista = self.tvw_usuario.item(selecionado, "values")
        mensagem = messagebox.askyesno(f'Excluir', f'Você tem certeza que deseja excluir o usuario: {lista[2]}?')
        if mensagem:
            sql = f'DELETE FROM usuario WHERE usuario_id={lista[0]};'
            bd.deletar(sql)
            self.update_tvw_user()
            messagebox.showinfo("Excluído", "usuário excluído com sucesso")
        self.user_screen.deiconify()

    def TypeManage(self):
        self.type_manage_screen = tk.Tk()
        self.type_manage_screen.title("Tipo de Escala")
        self.type_manage_screen.geometry('800x620')
        self.type_manage_screen.configure(bg='#D9D9D9')
        self.type_manage_screen.resizable(False, False)
        self.type_manage_screen.protocol("WM_DELETE_WINDOW", self.voltar_type_manage)

        self.frame_top_01 = tk.Frame(self.type_manage_screen, bg='#94939B')
        self.frame_top_01.pack(side=tk.TOP, padx=10, fill=tk.X, pady=(10, 0))

        self.lbl_manage_name = tk.Label(self.frame_top_01, text='TIPO DE ESCALAS', font=('Inter', 18, 'bold'),
                                        fg='#0B0B0B', bg='#94939B')
        self.lbl_manage_name.pack(side=tk.TOP, pady=(20, 5))

        self.lbl_filtro_type = tk.Label(self.frame_top_01, text='Filtro:', font=('Inter', 12, 'bold'), fg='#0B0B0B',
                                        bg='#94939B')
        self.lbl_filtro_type.pack(side=tk.LEFT, pady=5, padx=(20, 5))

        self.cbx_cargo_type = ttk.Combobox(self.frame_top_01, text='ID', values=("Nome do Tipo de Escala", "Finais de Semana", "Feriados", "Escala mútua"), state="readonly")
        self.cbx_cargo_type.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 10), pady=2)

        self.image_pesquisa_filtro = tk.PhotoImage(file="images/lupa.png")
        self.bttn_pesquisa_filtro = tk.Button(self.frame_top_01, text="O", image=self.image_pesquisa_filtro, width=16,
                                              command=self.filtro_tvw_type_manage)
        self.bttn_pesquisa_filtro.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.none = tk.Label(self.frame_top_01, text="", width=1, bg="#94939B")
        self.none.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.image_refresh_filtro = tk.PhotoImage(file="images/refresh.png")
        self.bttn_refresh_filtro = tk.Button(self.frame_top_01, text="O", image=self.image_refresh_filtro, width=16,
                                             command=self.update_tvw_type_manage)
        self.bttn_refresh_filtro.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.lbl_opt_type = tk.Label(self.frame_top_01, text='Pesquisar:', font=('Inter', 12, 'bold'), fg='#0B0B0B',
                                     bg='#94939B')
        self.lbl_opt_type.pack(side=tk.LEFT, pady=5, padx=(10, 5))

        self.entry_search_type = tk.Entry(self.frame_top_01)
        self.entry_search_type.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 10), pady=5)

        self.image_pesquisa = tk.PhotoImage(file="images/lupa.png")
        self.bttn_pesquisa = tk.Button(self.frame_top_01, text="O", image=self.image_pesquisa, width=16,
                                       command=self.pesquisar_type_manage)
        self.bttn_pesquisa.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.none = tk.Label(self.frame_top_01, text="", width=1, bg="#94939B")
        self.none.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.image_refresh = tk.PhotoImage(file="images/refresh.png")
        self.bttn_refresh = tk.Button(self.frame_top_01, text="O", image=self.image_refresh, width=16,
                                      command=self.update_tvw_type_manage)
        self.bttn_refresh.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.none2 = tk.Label(self.frame_top_01, text="", width=1, bg="#94939B")
        self.none2.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.frm_type_manage = tk.Frame(self.type_manage_screen, bg='#94939B')
        self.frm_type_manage.pack(pady=(0, 10), padx=10, expand=True, fill=tk.BOTH)

        self.frame_tvw_type_manage = tk.Frame(self.frm_type_manage, bg='#94939B')
        self.frame_tvw_type_manage.pack(pady=20, padx=20, expand=True, fill=tk.BOTH)

        self.tvw_type_manage = ttk.Treeview(self.frame_tvw_type_manage, columns=(
            'tipo_id', 'nome_tipo_escala', 'finais_semana', 'feriados', 'escala_mutua'),
                                            show='headings')
        self.tvw_type_manage.column('tipo_id', width=40)
        self.tvw_type_manage.column('nome_tipo_escala', width=250)
        self.tvw_type_manage.column('finais_semana', width=125)
        self.tvw_type_manage.column('feriados', width=125)
        self.tvw_type_manage.column('escala_mutua', width=125)
        self.tvw_type_manage.heading('tipo_id', text='Id')
        self.tvw_type_manage.heading('nome_tipo_escala', text='Nome do Tipo de Escala')
        self.tvw_type_manage.heading('finais_semana', text='Finais de Semana')
        self.tvw_type_manage.heading('feriados', text='Feriados')
        self.tvw_type_manage.heading('escala_mutua', text='Escala Mútua')
        self.tvw_type_manage.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.update_tvw_type_manage()

        self.scr_tvw_type_manage = ttk.Scrollbar(self.frame_tvw_type_manage, command=self.tvw_type_manage.yview)
        self.scr_tvw_type_manage.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw_type_manage.configure(yscroll=self.scr_tvw_type_manage.set)

        self.frame_tvw_type_button = tk.Frame(self.frm_type_manage, bg='#94939B')
        self.frame_tvw_type_button.pack(side=tk.BOTTOM)

        self.btn_create_type_manage = tk.Button(self.frame_tvw_type_button, text="Criar Tipo de Escala",
                                                font=("Arial", 10, "bold"),
                                                bg="#3CB371", fg="white", width=20, height=1, borderwidth=0,
                                                command=self.create_type)
        self.btn_create_type_manage.grid(row=0, column=0, padx=10, pady=10)

        self.btn_edit_type_manage = tk.Button(self.frame_tvw_type_button, text="Editar Tipo de Escala",
                                              font=("Arial", 10, "bold"),
                                              bg="Orange", fg="white", width=20, height=1, borderwidth=0,
                                              command=self.edit_type)
        self.btn_edit_type_manage.grid(row=0, column=1, padx=10, pady=10)

        self.btn_delete_type_manage = tk.Button(self.frame_tvw_type_button, text="Excluir Tipo de Escala",
                                                font=("Arial", 10, "bold"),
                                                bg="#E1523F", fg="white", width=20, height=1, borderwidth=0,
                                                command=self.delete_type_manage)
        self.btn_delete_type_manage.grid(row=0, column=2, padx=10, pady=10)

        self.btn_back_type_manage = tk.Button(self.frame_tvw_type_button, text="Voltar", font=("Arial", 10, "bold"),
                                              bg="#FFF",
                                              fg="#000", width=20, height=1, borderwidth=0,
                                              command=self.type_manage_close)
        self.btn_back_type_manage.grid(row=0, column=3, padx=10, pady=10)

    def update_tvw_type_manage(self):
        for i in self.tvw_type_manage.get_children():
            self.tvw_type_manage.delete(i)
        query = "SELECT tipo_escala_id, nome_tipo_escala, CASE WHEN finais_semana = 0 THEN 'Não' WHEN finais_semana = 1 THEN 'Sim' END AS finais_semana, CASE WHEN feriados = 0 THEN 'Não' WHEN feriados = 1 THEN 'Sim' END AS feriados, CASE WHEN escala_mutua = 0 THEN 'Não' WHEN escala_mutua = 1 THEN 'Sim' END AS escala_mutua FROM tipo_escala;"
        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw_type_manage.insert('', tk.END, values=tupla)
        self.cbx_cargo_type.set("")
        self.entry_search_type.delete(0, "end")

    def pesquisar_type_manage(self):
        busca = self.entry_search_type.get()
        for i in self.tvw_type_manage.get_children():
            self.tvw_type_manage.delete(i)
        if busca == '':
            self.update_tvw_type_manage()
        else:
            query = f"SELECT tipo_escala_id, nome_tipo_escala, CASE WHEN finais_semana = 0 THEN 'Não' WHEN finais_semana = 1 THEN 'Sim' END AS finais_semana, CASE WHEN feriados = 0 THEN 'Não' WHEN feriados = 1 THEN 'Sim' END AS feriados, CASE WHEN escala_mutua = 0 THEN 'Não' WHEN escala_mutua = 1 THEN 'Sim' END AS escala_mutua FROM tipo_escala WHERE nome_tipo_escala LIKE '{busca}%';"
            dados = bd.consultar(query)
            for tupla in dados:
                self.tvw_type_manage.insert('', tk.END, values=tupla)

    def filtro_tvw_type_manage(self):
        busca = self.cbx_cargo_type.get()
        for i in self.tvw_type_manage.get_children():
            self.tvw_type_manage.delete(i)
        if busca == '':
            self.update_tvw_type_manage()
        elif busca == "Nome do Tipo de Escala":
            query = f"SELECT tipo_escala_id, nome_tipo_escala, CASE WHEN finais_semana = 0 THEN 'Não' WHEN finais_semana = 1 THEN 'Sim' END AS finais_semana, CASE WHEN feriados = 0 THEN 'Não' WHEN feriados = 1 THEN 'Sim' END AS feriados, CASE WHEN escala_mutua = 0 THEN 'Não' WHEN escala_mutua = 1 THEN 'Sim' END AS escala_mutua FROM tipo_escala ORDER BY nome_tipo_escala"
            dados = bd.consultar(query)
            for tupla in dados:
                self.tvw_type_manage.insert('', tk.END, values=tupla)
        elif busca == "Finais de Semana":
            query = f"SELECT tipo_escala_id, nome_tipo_escala, CASE WHEN finais_semana = 0 THEN 'Não' WHEN finais_semana = 1 THEN 'Sim' END AS finais_semana, CASE WHEN feriados = 0 THEN 'Não' WHEN feriados = 1 THEN 'Sim' END AS feriados, CASE WHEN escala_mutua = 0 THEN 'Não' WHEN escala_mutua = 1 THEN 'Sim' END AS escala_mutua FROM tipo_escala ORDER BY finais_semana"
            dados = bd.consultar(query)
            for tupla in dados:
                self.tvw_type_manage.insert('', tk.END, values=tupla)
        elif busca == "Feriados":
            query = f"SELECT tipo_escala_id, nome_tipo_escala, CASE WHEN finais_semana = 0 THEN 'Não' WHEN finais_semana = 1 THEN 'Sim' END AS finais_semana, CASE WHEN feriados = 0 THEN 'Não' WHEN feriados = 1 THEN 'Sim' END AS feriados, CASE WHEN escala_mutua = 0 THEN 'Não' WHEN escala_mutua = 1 THEN 'Sim' END AS escala_mutua FROM tipo_escala ORDER BY feriados"
            dados = bd.consultar(query)
            for tupla in dados:
                self.tvw_type_manage.insert('', tk.END, values=tupla)
        else:
            query = f"SELECT tipo_escala_id, nome_tipo_escala, CASE WHEN finais_semana = 0 THEN 'Não' WHEN finais_semana = 1 THEN 'Sim' END AS finais_semana, CASE WHEN feriados = 0 THEN 'Não' WHEN feriados = 1 THEN 'Sim' END AS feriados, CASE WHEN escala_mutua = 0 THEN 'Não' WHEN escala_mutua = 1 THEN 'Sim' END AS escala_mutua FROM tipo_escala ORDER BY escala_mutua"
            dados = bd.consultar(query)
            for tupla in dados:
                self.tvw_type_manage.insert('', tk.END, values=tupla)

    def CreateTypeScreen(self):
        self.create_screen = tk.Toplevel()
        self.create_screen.title("Criar Tipo de Escala")
        self.create_screen.grab_set()
        self.create_screen.geometry("462x550")
        self.create_screen.configure(bg='#D9D9D9')
        self.create_screen.resizable(False, False)
        self.create_screen.protocol("WM_DELETE_WINDOW", self.type_close)

        self.center_frame = tk.Frame(self.create_screen, bg='#94939B')
        self.center_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.lbl_create = tk.Label(self.center_frame, text='CRIAR TIPO DE ESCALA', font=('Inter', 20, 'bold'),
                                   fg='#0B0B0B', bg='#94939B')
        self.lbl_create.pack(side=tk.TOP, padx=5, pady=10)

        self.lbl_nome_escala = tk.Label(self.center_frame, text="NOME DO TIPO DE ESCALA:", font=('Inter', 10, 'bold'),
                                        fg='#FFF', bg='#94939B')
        self.lbl_nome_escala.pack(side=tk.TOP, pady=5, padx=10)

        self.entry_nome_escala = tk.Entry(self.center_frame, width=59)
        self.entry_nome_escala.pack(side=tk.TOP, padx=5, pady=10)

        self.frame_escolhas = tk.Frame(self.center_frame, bg='#94939B')
        self.frame_escolhas.pack(fill=tk.Y, expand=True, padx=10, pady=10, side=tk.TOP)

        self.int_var_finais_semana = tk.IntVar()
        self.int_var_feriados = tk.IntVar()
        self.int_var_escala_mutua = tk.IntVar()

        style = ttk.Style()
        style.configure("Custom.TRadiobutton", background="#94939B", foreground="white", font=("Inter", 10, "bold"))

        self.lbl_cont_final_semana = tk.Label(self.frame_escolhas, text="CONTAR FINAIS DE SEMANA?", font=('Inter', 10),
                                              fg='#FFF', bg='#94939B')
        self.lbl_cont_final_semana.grid(row=0, column=0, columnspan=3, sticky='n', pady=10)

        self.rbtn_cont_final_semanas = ttk.Radiobutton(self.frame_escolhas, text="Sim",
                                                       variable=self.int_var_finais_semana,
                                                       value=1, style="Custom.TRadiobutton")
        self.rbtn_cont_final_semanas.grid(row=2, column=0, padx=10, pady=10, sticky='n')

        self.rbtn_cont_final_semanan = ttk.Radiobutton(self.frame_escolhas, text="Não",
                                                       variable=self.int_var_finais_semana,
                                                       value=0, style="Custom.TRadiobutton")
        self.rbtn_cont_final_semanan.grid(row=2, column=1, padx=10, pady=10, sticky='n')

        self.lbl_cont_ferias = tk.Label(self.frame_escolhas, text="CONTAR FERIADOS?", font=('Inter', 10, 'bold'),
                                        fg='#FFF', bg='#94939B')
        self.lbl_cont_ferias.grid(row=3, column=0, columnspan=2, sticky='nsew', pady=20)

        self.rbtn_cont_feriass = ttk.Radiobutton(self.frame_escolhas, text="Sim", variable=self.int_var_feriados,
                                                 value=1, style="Custom.TRadiobutton")
        self.rbtn_cont_feriass.grid(row=4, column=0, padx=10, pady=10, sticky='n')

        self.rbtn_cont_feriasn = ttk.Radiobutton(self.frame_escolhas, text="Não", variable=self.int_var_feriados,
                                                 value=0, style="Custom.TRadiobutton")
        self.rbtn_cont_feriasn.grid(row=4, column=1, padx=10, pady=10, sticky='n')

        self.lbl_cont_escala_mutua = tk.Label(self.frame_escolhas, text="ESCALA MUTUA?",
                                              font=('Inter', 10, 'bold'), fg='#FFF', bg='#94939B')
        self.lbl_cont_escala_mutua.grid(row=5, column=0, columnspan=2, sticky='nsew', pady=20)

        self.rbtn_cont_escala_mutuas = ttk.Radiobutton(self.frame_escolhas, text="Sim",
                                                       variable=self.int_var_escala_mutua,
                                                       value=1, style="Custom.TRadiobutton")
        self.rbtn_cont_escala_mutuas.grid(row=6, column=0, padx=10, pady=10, sticky='n')

        self.rbtn_cont_escala_mutuan = ttk.Radiobutton(self.frame_escolhas, text="Não",
                                                       variable=self.int_var_escala_mutua,
                                                       value=0, style="Custom.TRadiobutton")
        self.rbtn_cont_escala_mutuan.grid(row=6, column=1, padx=10, pady=10, sticky='n')

        self.frame_button = tk.Frame(self.center_frame, bg='#94939B')
        self.frame_button.pack(fill=tk.Y, padx=10, pady=10, side=tk.TOP)

        self.bttn_criar = tk.Button(self.frame_button, text='Criar', font=('Inter', 10, 'bold'), fg='#FFF',
                                    bg='#3CB371', command=self.confirm_create_type_manage, borderwidth=0, width=10)
        self.bttn_criar.pack(side=tk.LEFT, pady=5, padx=10)

        self.bttn_clean = tk.Button(self.frame_button, text='Limpar', font=('Inter', 10, 'bold'), fg='#FFF',
                                    bg='Orange', command=self.clear_create_type_screen, borderwidth=0, width=10)
        self.bttn_clean.pack(side=tk.LEFT, pady=5, padx=10)

        self.bttn_voltar = tk.Button(self.frame_button, text='Voltar', font=("Arial", 10, "bold"), bg="#E1523F",
                                     fg="white", borderwidth=0, command=self.type_close, width=10)
        self.bttn_voltar.pack(side=tk.LEFT, pady=5, padx=10)

    def clear_create_type_screen(self):
        self.entry_nome_escala.delete(0, "end")
        self.int_var_finais_semana.set(0)
        self.int_var_feriados.set(0)
        self.int_var_escala_mutua.set(0)

    def confirm_create_type_manage(self):
        nome_escala = self.entry_nome_escala.get()
        finais_semana = self.int_var_finais_semana.get()
        feriados = self.int_var_feriados.get()
        escala_mutua = self.int_var_escala_mutua.get()

        if nome_escala == "":
            messagebox.showinfo("Insira um nome completo", "O campo nome da escala está incorreto!")
            self.create_screen.deiconify()
        elif escala_mutua == "":
            messagebox.showinfo("Selecione um tipo", "Nenhuma seleção no escala mútua!")
            self.create_screen.deiconify()
        elif finais_semana == "":
            messagebox.showinfo("Selecione um tipo", "Nenhuma seleção no finais de semana!")
            self.create_screen.deiconify()
        elif feriados == "":
            messagebox.showinfo("Selecione um tipo", "Nenhuma seleção no feriados!")
            self.create_screen.deiconify()
        else:
            query = 'SELECT nome_tipo_escala FROM tipo_escala;'
            valores = bd.consultar_usuarios(query)
            confirmar = False
            for i in valores:
                if nome_escala == i:
                    confirmar = True
                    break
            if not confirmar:
                query = f'INSERT INTO tipo_escala ("nome_tipo_escala", "feriados", "finais_semana", "escala_mutua") VALUES ("{nome_escala}", {feriados}, {finais_semana}, {escala_mutua});'
                bd.inserir(query)
                self.update_tvw_type_manage()
                messagebox.showinfo("SUCESSO!", "Escala criada com sucesso!")
                self.create_screen.destroy()
                self.type_manage_screen.deiconify()
            else:
                messagebox.showinfo("Nome do tipo de escala já cadastrado",
                                    "O Nome do tipo de escala já está cadastrado")
                self.create_screen.deiconify()

    def EditeTypeScreen(self):
        selecionado = self.tvw_type_manage.selection()
        tupla = self.tvw_type_manage.item(selecionado, "values")

        if selecionado != ():
            self.edite_type = tk.Toplevel()
            self.edite_type.title("Editar Tipo de Escala")
            self.edite_type.grab_set()
            self.edite_type.geometry("462x550")
            self.edite_type.configure(bg='#D9D9D9')
            self.edite_type.resizable(False, False)
            self.edite_type.protocol("WM_DELETE_WINDOW", self.type_edit_close)

            self.lista = list(tupla)
            for i in range(len(self.lista)):
                if self.lista[i] == "Não":
                    self.lista[i] = 0
                elif self.lista[i] == "Sim":
                    self.lista[i] = 1

            self.center_frame = tk.Frame(self.edite_type, bg='#94939B')
            self.center_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

            self.lbl_create = tk.Label(self.center_frame, text='EDITAR TIPO DE ESCALA', font=('Inter', 20, 'bold'),
                                       fg='#0B0B0B', bg='#94939B')
            self.lbl_create.pack(side=tk.TOP, padx=5, pady=10)

            self.lbl_nome_escala = tk.Label(self.center_frame, text="NOME DO TIPO DE ESCALA:",
                                            font=('Inter', 10, 'bold'), fg='#FFF', bg='#94939B')
            self.lbl_nome_escala.pack(side=tk.TOP, pady=5, padx=10)

            self.entry_nome_escala = tk.Entry(self.center_frame, width=59)
            self.entry_nome_escala.pack(side=tk.TOP, padx=5, pady=10)
            self.entry_nome_escala.insert(0, self.lista[1])

            self.frame_escolhas = tk.Frame(self.center_frame, bg='#94939B')
            self.frame_escolhas.pack(fill=tk.Y, expand=True, padx=10, pady=10, side=tk.TOP)

            self.int_var_finais_semana = tk.IntVar()
            self.int_var_feriados = tk.IntVar()
            self.int_var_escala_mutua = tk.IntVar()

            style = ttk.Style()
            style.configure("Custom.TRadiobutton", background="#94939B", foreground="white", font=("Inter", 10, "bold"))

            self.lbl_cont_final_semana = tk.Label(self.frame_escolhas, text="CONTAR FINAIS DE SEMANA?",
                                                  font=('Inter', 10), fg='#FFF', bg='#94939B')
            self.lbl_cont_final_semana.grid(row=0, column=0, columnspan=3, sticky='n', pady=10)

            self.rbtn_cont_final_semanas = ttk.Radiobutton(self.frame_escolhas, text="Sim",
                                                           variable=self.int_var_finais_semana,
                                                           value=1, style="Custom.TRadiobutton")
            self.rbtn_cont_final_semanas.grid(row=2, column=0, padx=10, pady=10, sticky='n')

            self.rbtn_cont_final_semanan = ttk.Radiobutton(self.frame_escolhas, text="Não",
                                                           variable=self.int_var_finais_semana,
                                                           value=0, style="Custom.TRadiobutton")
            self.rbtn_cont_final_semanan.grid(row=2, column=1, padx=10, pady=10, sticky='n')

            if self.lista[2] == 1:
                self.int_var_finais_semana.set(1)
            else:
                self.int_var_finais_semana.set(0)

            self.lbl_cont_ferias = tk.Label(self.frame_escolhas, text="CONTAR FERIADOS?", font=('Inter', 10, 'bold'),
                                            fg='#FFF', bg='#94939B')
            self.lbl_cont_ferias.grid(row=3, column=0, columnspan=2, sticky='nsew', pady=20)

            self.rbtn_cont_feriass = ttk.Radiobutton(self.frame_escolhas, text="Sim", variable=self.int_var_feriados,
                                                     value=1, style="Custom.TRadiobutton")
            self.rbtn_cont_feriass.grid(row=4, column=0, padx=10, pady=10, sticky='n')

            self.rbtn_cont_feriasn = ttk.Radiobutton(self.frame_escolhas, text="Não", variable=self.int_var_feriados,
                                                     value=0, style="Custom.TRadiobutton")
            self.rbtn_cont_feriasn.grid(row=4, column=1, padx=10, pady=10, sticky='n')

            if self.lista[3] == 1:
                self.int_var_feriados.set(1)
            else:
                self.int_var_feriados.set(0)

            self.lbl_cont_escala_mutua = tk.Label(self.frame_escolhas, text="ESCALA MUTUA?",
                                                  font=('Inter', 10, 'bold'), fg='#FFF', bg='#94939B')
            self.lbl_cont_escala_mutua.grid(row=5, column=0, columnspan=2, sticky='nsew', pady=20)

            self.rbtn_cont_escala_mutuas = ttk.Radiobutton(self.frame_escolhas, text="Sim",
                                                           variable=self.int_var_escala_mutua,
                                                           value=1, style="Custom.TRadiobutton")
            self.rbtn_cont_escala_mutuas.grid(row=6, column=0, padx=10, pady=10, sticky='n')

            self.rbtn_cont_escala_mutuan = ttk.Radiobutton(self.frame_escolhas, text="Não",
                                                           variable=self.int_var_escala_mutua,
                                                           value=0, style="Custom.TRadiobutton")
            self.rbtn_cont_escala_mutuan.grid(row=6, column=1, padx=10, pady=10, sticky='n')

            if self.lista[4] == 1:
                self.int_var_escala_mutua.set(1)
            else:
                self.int_var_escala_mutua.set(0)

            self.frame_button = tk.Frame(self.center_frame, bg='#94939B')
            self.frame_button.pack(fill=tk.Y, padx=10, pady=10, side=tk.TOP)

            self.bttn_criar = tk.Button(self.frame_button, text='Editar', font=('Inter', 10, 'bold'), fg='#FFF',
                                        bg='#3CB371', command=self.confirm_edit_type_manage, borderwidth=0, width=10)
            self.bttn_criar.pack(side=tk.LEFT, pady=5, padx=10)

            self.bttn_clean = tk.Button(self.frame_button, text='Refazer', font=('Inter', 10, 'bold'), fg='#FFF',
                                        bg='Orange', command=self.clear_edit_type_screen, borderwidth=0, width=10)
            self.bttn_clean.pack(side=tk.LEFT, pady=5, padx=10)

            self.bttn_voltar = tk.Button(self.frame_button, text='Voltar', font=("Arial", 10, "bold"), bg="#E1523F",
                                         fg="white", borderwidth=0, command=self.type_edit_close, width=10)
            self.bttn_voltar.pack(side=tk.LEFT, pady=5, padx=10)

    def clear_edit_type_screen(self):
        self.entry_nome_escala.delete(0, "end")
        self.entry_nome_escala.insert(0, self.lista[1])

        if self.lista[2] == 1:
            self.int_var_finais_semana.set(1)
        else:
            self.int_var_finais_semana.set(0)

        if self.lista[3] == 1:
            self.int_var_feriados.set(1)
        else:
            self.int_var_feriados.set(0)

        if self.lista[4] == 1:
            self.int_var_escala_mutua.set(1)
        else:
            self.int_var_escala_mutua.set(0)

    def confirm_edit_type_manage(self):
        selecionado = self.tvw_type_manage.selection()
        lista = self.tvw_type_manage.item(selecionado, "values")

        nome_tipo_escala = self.entry_nome_escala.get()
        finais_semana = self.int_var_finais_semana.get()
        feriados = self.int_var_feriados.get()
        escala_mutua = self.int_var_escala_mutua.get()

        if nome_tipo_escala == "":
            messagebox.showinfo("Insira um nome completo", "O campo nome da escala está incorreto!")
            self.edite_type.deiconify()
        elif escala_mutua == "":
            messagebox.showinfo("Insira os dias", "Nenhuma seleção em escala mútua!")
            self.edite_type.deiconify()
        elif finais_semana == "":
            messagebox.showinfo("Selecione um tipo", "Nenhuma seleção no finais de semana!")
            self.edite_type.deiconify()
        elif feriados == "":
            messagebox.showinfo("Selecione um tipo", "Nenhuma seleção no feriados!")
            self.edite_type.deiconify()
        else:
            query = 'SELECT nome_tipo_escala FROM tipo_escala;'
            valores = bd.consultar_usuarios(query)
            confirmar = False
            for i in valores:
                if nome_tipo_escala == i and i != lista[1]:
                    confirmar = True
                    break
            if not confirmar:
                query = f'UPDATE tipo_escala SET nome_tipo_escala="{nome_tipo_escala}", feriados={feriados}, finais_semana={finais_semana}, escala_mutua={escala_mutua} WHERE tipo_escala_id={lista[0]};'
                bd.atualizar(query)
                messagebox.showinfo("SUCESSO!", "Escala editada com sucesso!")
                self.update_tvw_type_manage()
                self.edite_type.destroy()
                self.type_manage_screen.deiconify()
            else:
                messagebox.showinfo("Nome do tipo de escala já cadastrado",
                                    "O Nome do tipo de escala já está cadastrado")
                self.edite_type.deiconify()

    def delete_type_manage(self):
        selecionado = self.tvw_type_manage.selection()
        lista = self.tvw_type_manage.item(selecionado, "values")
        mensagem = messagebox.askyesno(f'Excluir', f'Você tem certeza que deseja excluir o tipo de escala: {lista[1]}?')
        if mensagem:
            sql = f'DELETE FROM tipo_escala WHERE tipo_escala_id={lista[0]};'
            bd.deletar(sql)
            messagebox.showinfo("Excluído", "Tipo de escala excluída com sucesso")
            self.update_tvw_type_manage()
        self.type_manage_screen.deiconify()

    def RosterManage(self):
        self.roster_manage = tk.Tk()
        self.roster_manage.title("Gerenciar Escalas")
        self.roster_manage.geometry('1000x600')
        self.roster_manage.configure(bg='#D9D9D9')
        self.roster_manage.resizable(False, False)
        self.roster_manage.protocol("WM_DELETE_WINDOW", self.voltar_manage)

        self.frame_top_02 = tk.Frame(self.roster_manage, bg='#94939B')
        self.frame_top_02.pack(side=tk.TOP, padx=10, fill=tk.X, pady=(10, 0))

        self.lbl_01 = tk.Label(self.frame_top_02, text='GERENCIAR ESCALAS', font=('Inter', 18, 'bold'), fg='#0B0B0B',
                               bg='#94939B')
        self.lbl_01.pack(side=tk.TOP, pady=(20))

        self.lbl_filtro_type = tk.Label(self.frame_top_02, text='Filtro:', font=('Inter', 12, 'bold'), fg='#0B0B0B',
                                        bg='#94939B')
        self.lbl_filtro_type.pack(side=tk.LEFT, pady=5, padx=(10, 5))

        self.cbx_cargo_type = ttk.Combobox(self.frame_top_02, text='ID', values=("Nome da Escala", "Tipo de Escala", "Data de início", "Data de fim"), state="readonly")
        self.cbx_cargo_type.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 10), pady=2)

        self.image_pesquisa_filtro = tk.PhotoImage(file="images/lupa.png")
        self.bttn_pesquisa_filtro = tk.Button(self.frame_top_02, text="O", image=self.image_pesquisa_filtro, width=16,
                                              command=self.filtro_tvw_roster_manage)
        self.bttn_pesquisa_filtro.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.none = tk.Label(self.frame_top_02, text="", width=1, bg="#94939B")
        self.none.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.image_refresh_filtro = tk.PhotoImage(file="images/refresh.png")
        self.bttn_refresh_filtro = tk.Button(self.frame_top_02, text="O", image=self.image_refresh_filtro, width=16,
                                             command=self.update_tvw_roster)
        self.bttn_refresh_filtro.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.lbl_opt_type = tk.Label(self.frame_top_02, text='Pesquisar:', font=('Inter', 12, 'bold'), fg='#0B0B0B',
                                     bg='#94939B')
        self.lbl_opt_type.pack(side=tk.LEFT, pady=5, padx=(10, 5))

        self.entry_search_roster = tk.Entry(self.frame_top_02)
        self.entry_search_roster.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 10), pady=5)

        self.image_pesquisa = tk.PhotoImage(file="images/lupa.png")
        self.bttn_pesquisa = tk.Button(self.frame_top_02, text="O", image=self.image_pesquisa, width=16,
                                       command=self.pesquisar_roster_manage)
        self.bttn_pesquisa.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.none = tk.Label(self.frame_top_02, text="", width=1, bg="#94939B")
        self.none.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.image_refresh = tk.PhotoImage(file="images/refresh.png")
        self.bttn_refresh = tk.Button(self.frame_top_02, text="O", image=self.image_refresh, width=16,
                                      command=self.update_tvw_roster)
        self.bttn_refresh.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.none2 = tk.Label(self.frame_top_02, text="", width=1, bg="#94939B")
        self.none2.pack(side=tk.LEFT, pady=5, fill=tk.X)

        self.frm_01 = tk.Frame(self.roster_manage, bg='#94939B')
        self.frm_01.pack(pady=(0, 10), padx=10, expand=True, fill=tk.BOTH)

        self.frame_tvw_roster = tk.Frame(self.frm_01, bg='#94939B')
        self.frame_tvw_roster.pack(expand=True, fill=tk.BOTH, padx=8, pady=(10, 8))

        self.tvw_escala = ttk.Treeview(self.frame_tvw_roster, columns=(
            'id', 'nome escala', 'tipo de escala', 'data inicio', 'data fim'), show='headings')
        self.tvw_escala.column('id', width=40)
        self.tvw_escala.column('nome escala', width=350)
        self.tvw_escala.column('tipo de escala', width=250)
        self.tvw_escala.column('data inicio', width=100)
        self.tvw_escala.column('data fim', width=100)
        self.tvw_escala.heading('id', text='Id')
        self.tvw_escala.heading('nome escala', text='Nome da Escala')
        self.tvw_escala.heading('tipo de escala', text='Tipo de Escala')
        self.tvw_escala.heading('data inicio', text='Data de início')
        self.tvw_escala.heading('data fim', text='Data de fim')
        self.tvw_escala.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.update_tvw_roster()

        self.scr_escala = ttk.Scrollbar(self.frame_tvw_roster, command=self.tvw_escala.yview)
        self.scr_escala.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw_escala.configure(yscroll=self.scr_escala.set)

        self.frame_button = tk.Frame(self.frm_01, bg='#94939B')
        self.frame_button.pack(side=tk.BOTTOM)

        self.btn_create = tk.Button(self.frame_button, text="Criar Escala", font=("Arial", 10, "bold"), bg="#3CB371",
                                    fg="white", width=20, height=1, borderwidth=0, command=self.create_roster)
        self.btn_create.grid(row=0, column=0, padx=10, pady=10)

        self.btn_edit = tk.Button(self.frame_button, text="Editar Escala", font=("Arial", 10, "bold"), bg="Orange",
                                  fg="white", width=20, height=1, borderwidth=0, command=self.edit_roster)
        self.btn_edit.grid(row=0, column=1, padx=10, pady=10)

        self.btn_exclude = tk.Button(self.frame_button, text="Excluir Escala", font=("Arial", 10, "bold"), bg="#E1523F",
                                     fg="white", width=20, height=1, borderwidth=0, command=self.delete_roster)
        self.btn_exclude.grid(row=0, column=2, padx=10, pady=10)

        self.bttn_atribuir = tk.Button(self.frame_button, text="Atribuir", font=("Arial", 10, "bold"), bg="#000", fg="#FFF",
                                     width=20, height=1, borderwidth=0, command=self.Escalas)
        self.bttn_atribuir.grid(row=0, column=3, padx=10, pady=10)

        self.bttn_return = tk.Button(self.frame_button, text="Voltar", font=("Arial", 10, "bold"), bg="#FFF", fg="#000",
                                     width=20, height=1, borderwidth=0, command=self.voltar_manage)
        self.bttn_return.grid(row=0, column=4, padx=10, pady=10)

    def update_tvw_roster(self):
        for i in self.tvw_escala.get_children():
            self.tvw_escala.delete(i)
        query = 'SELECT escala_id, nome_escala, nome_tipo_escala, data_inicio_escala, data_fim_escala FROM tipo_escala as te, escala as e WHERE te.tipo_escala_id = e.tipo_escala_id;'
        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw_escala.insert('', tk.END, values=tupla)
        self.entry_search_roster.delete(0, "end")
        self.cbx_cargo_type.set("")

    def pesquisar_roster_manage(self):
        busca = self.entry_search_roster.get()
        for i in self.tvw_escala.get_children():
            self.tvw_escala.delete(i)
        if busca == '':
            self.update_tvw_roster()
        else:
            query = f"SELECT escala_id, nome_escala, nome_tipo_escala, data_inicio_escala, data_fim_escala FROM tipo_escala as te, escala as e WHERE te.tipo_escala_id = e.tipo_escala_id AND nome_escala LIKE '{busca}%';"
            dados = bd.consultar(query)
            for tupla in dados:
                self.tvw_escala.insert('', tk.END, values=tupla)

    def filtro_tvw_roster_manage(self):
        busca = self.cbx_cargo_type.get()
        for i in self.tvw_escala.get_children():
            self.tvw_escala.delete(i)
        if busca == '':
            self.update_tvw_type_manage()
        elif busca == "Nome da Escala":
            query = f"SELECT escala_id, nome_escala, nome_tipo_escala, data_inicio_escala, data_fim_escala FROM tipo_escala as te, escala as e WHERE te.tipo_escala_id = e.tipo_escala_id ORDER BY nome_escala"
            dados = bd.consultar(query)
            for tupla in dados:
                self.tvw_escala.insert('', tk.END, values=tupla)
        elif busca == "Nome do Tipo de Escala":
            query = f"SELECT escala_id, nome_escala, nome_tipo_escala, data_inicio_escala, data_fim_escala FROM tipo_escala as te, escala as e WHERE te.tipo_escala_id = e.tipo_escala_id ORDER BY nome_tipo_escala"
            dados = bd.consultar(query)
            for tupla in dados:
                self.tvw_escala.insert('', tk.END, values=tupla)
        elif busca == "Data de início":
            query = f"SELECT escala_id, nome_escala, nome_tipo_escala, data_inicio_escala, data_fim_escala FROM tipo_escala as te, escala as e WHERE te.tipo_escala_id = e.tipo_escala_id ORDER BY data_inicio_escala"
            dados = bd.consultar(query)
            for tupla in dados:
                self.tvw_escala.insert('', tk.END, values=tupla)
        elif busca == "Data de fim":
            query = f"SELECT escala_id, nome_escala, nome_tipo_escala, data_inicio_escala, data_fim_escala FROM tipo_escala as te, escala as e WHERE te.tipo_escala_id = e.tipo_escala_id ORDER BY data_fim_escala"
            dados = bd.consultar(query)
            for tupla in dados:
                self.tvw_escala.insert('', tk.END, values=tupla)

    def CreateRoster(self):
        self.create_roster_screen = tk.Tk()
        self.create_roster_screen.title("Criar Escala")
        self.create_roster_screen.geometry('462x676')
        self.create_roster_screen.configure(bg='#D9D9D9')
        self.create_roster_screen.resizable(False, False)

        self.lbl_name_03 = tk.Label(self.create_roster_screen,text= "CRIAR ESCALA",font=('Inter', 18, 'bold'), fg='#0B0B0B',bg='#D9D9D9')
        self.lbl_name_03.pack(side=tk.TOP,pady=(20,5))

        self.center_frame_06 = tk.Frame(self.create_roster_screen, bg='#94939B')
        self.center_frame_06.pack(pady=20, padx=20, expand=True, fill=tk.BOTH)

        self.lbl_name_04 = tk.Label(self.center_frame_06,text='Nome da escala',bg='#94939B',font=('Inter', 18, 'bold'))
        self.lbl_name_04.pack(side=tk.TOP,pady=10,padx=20)

        self.roster_name_entry = tk.Entry(self.center_frame_06)
        self.roster_name_entry.pack(side=tk.TOP,pady=10,padx=40,fill=tk.BOTH)

        self.lbl_type = tk.Label(self.center_frame_06,text='Tipo da Escala',bg='#94939B',font=('Inter', 18, 'bold'))
        self.lbl_type.pack(side=tk.TOP,pady=10,padx=20)

        query = 'SELECT nome_tipo_escala FROM tipo_escala;'
        dados = bd.consultar(query)

        self.tipo_escala = []
        for tupla in dados:
            for tipo_escala in tupla:
                self.tipo_escala.append(tipo_escala)

        self.roster_type_var = tk.StringVar()
        self.roster_type_combobox = ttk.Combobox(self.center_frame_06, textvariable=self.roster_type_var,values=self.tipo_escala)
        self.roster_type_combobox.pack(side=tk.TOP, pady=10, padx=40, fill=tk.BOTH)
        self.roster_type_combobox["state"] = "readonly"

        self.lbl_data_inicio = tk.Label(self.center_frame_06, text="Data de início da escala",bg='#94939B',font=('Inter', 18, 'bold'))
        self.lbl_data_inicio.pack(side=tk.TOP,pady=10,padx=20)

        self.cal_data_inicio = DateEntry(self.center_frame_06, locale='pt_BR', date_pattern='dd/MM/yyyy')
        self.cal_data_inicio.pack(side=tk.TOP, pady=10, padx=40, fill=tk.BOTH)
        #self.cal_data_inicio["state"] = "readonly"


        self.lbl_data_final = tk.Label(self.center_frame_06, text="Data de Termino da escala", bg='#94939B',font=('Inter', 18, 'bold'))
        self.lbl_data_final.pack(side=tk.TOP, pady=10, padx=20)

        self.cal_data_final = DateEntry(self.center_frame_06, locale='pt_BR', date_pattern='dd/MM/yyyy')
        self.cal_data_final.pack(side=tk.TOP, pady=10, padx=40, fill=tk.BOTH)
        #self.cal_data_final["state"] = "readonly"

        self.frm_bttn = tk.Frame(self.center_frame_06,bg='#94939B')
        self.frm_bttn.pack(side=tk.BOTTOM,pady=10,padx=10,expand=True)

        self.bttn_confirmar = tk.Button(self.frm_bttn,text="Confirmar", command=self.cofirm_create_roster,font=("Arial", 10, "bold"), bg="#3CB371",fg="white", width=10, height=1,borderwidth=0)
        self.bttn_confirmar.pack(side=tk.LEFT,padx=15,pady=10)

        self.bttn_limpar = tk.Button(self.frm_bttn, text="Limpar", command=self.clear_create_roster, font=("Arial", 10, "bold"), bg="Orange", fg="white",width=10, height=1,borderwidth=0)
        self.bttn_limpar.pack(side=tk.LEFT,padx=15,pady=10)

        self.btn_cancelar = tk.Button(self.frm_bttn, text="Cancelar", command=self.voltar_create_roster, font=("Arial", 10, "bold"),bg="#E1523F", fg="white", width=10, height=1, borderwidth=0)
        self.btn_cancelar.pack(side=tk.LEFT,padx=15,pady=10)

    def clear_create_roster(self):
        self.roster_name_entry.delete(0, "end")
        self.cal_data_inicio.set_date(date.today())
        self.cal_data_final.set_date(date.today())
        self.roster_type_combobox.set("")

    def cofirm_create_roster(self):
        nome_escala = self.roster_name_entry.get()
        tipo_escala = self.roster_type_combobox.get()
        data_inicio = self.cal_data_inicio.get_date().strftime('%d/%m/%Y')
        data_fim = self.cal_data_final.get_date().strftime('%d/%m/%Y')

        if nome_escala == "":
            messagebox.showinfo("Insira um nome completo", "O campo nome da escala está incorreto!")
            self.create_roster_screen.deiconify()
        elif tipo_escala == "":
            messagebox.showinfo("Insira os dias", "O campo tipo escala está vazio!")
            self.create_roster_screen.deiconify()
        elif data_inicio == "":
            messagebox.showinfo("Selecione um tipo", "Nenhuma seleção na data de inicio!")
            self.create_roster_screen.deiconify()
        elif data_fim == "":
            messagebox.showinfo("Selecione um tipo", "Nenhuma seleção na data de fim!")
            self.create_roster_screen.deiconify()
        else:
            query = 'SELECT nome_escala FROM escala;'
            valores = bd.consultar_usuarios(query)
            confirmar = False
            for i in valores:
                if nome_escala == i:
                    confirmar = True
                    break
            if not confirmar:
                query = f"SELECT tipo_escala_id FROM tipo_escala WHERE '{tipo_escala}' LIKE nome_tipo_escala;"
                dados = bd.consultar_usuarios(query)
                query = f'INSERT INTO escala ("nome_escala", "tipo_escala_id", "data_inicio_escala", "data_fim_escala") VALUES ("{nome_escala}", {dados[0]}, "{data_inicio}", "{data_fim}", {dias});'
                bd.inserir(query)
                self.update_tvw_roster()
                messagebox.showinfo("SUCESSO!", "Escala criada com sucesso!")
                self.create_roster_screen.destroy()
                self.roster_manage.deiconify()
            else:
                messagebox.showinfo("Nome de escala já cadastrado", "O Nome da escala já está cadastrado")
                self.create_roster_screen.deiconify()

    def RosterEdit(self):
        selecionado = self.tvw_escala.selection()
        self.lista = self.tvw_escala.item(selecionado, "values")
        if selecionado != ():
            self.edit_roster_screen = tk.Tk()
            self.edit_roster_screen.title("Editar Escala")
            self.edit_roster_screen.geometry('462x676')
            self.edit_roster_screen.configure(bg='#D9D9D9')
            self.edit_roster_screen.resizable(False, False)

            self.lbl_text= tk.Label(self.edit_roster_screen, text="EDITAR ESCALA", font=('Inter', 18, 'bold'),fg='#0B0B0B', bg='#D9D9D9')
            self.lbl_text.pack(side=tk.TOP, pady=(20, 5))

            self.center_frame_07 = tk.Frame(self.edit_roster_screen, bg='#94939B')
            self.center_frame_07.pack(pady=20, padx=20, expand=True, fill=tk.BOTH)

            self.lbl_name_06 = tk.Label(self.center_frame_07, text='Nome da escala', bg='#94939B',font=('Inter', 18, 'bold'))
            self.lbl_name_06.pack(side=tk.TOP, pady=10, padx=20)

            self.roster_name_entry_edit = tk.Entry(self.center_frame_07)
            self.roster_name_entry_edit.pack(side=tk.TOP, pady=10, padx=40, fill=tk.BOTH)
            self.roster_name_entry_edit.insert(0, self.lista[1])

            self.lbl_type_edit = tk.Label(self.center_frame_07, text='Tipo da Escala', bg='#94939B', font=('Inter', 18, 'bold'))
            self.lbl_type_edit.pack(side=tk.TOP, pady=10, padx=20)

            query = 'SELECT nome_tipo_escala FROM tipo_escala;'
            dados = bd.consultar(query)

            self.roster_type_var_edit = tk.StringVar()
            self.tipo_escala = []

            self.tipo_escala.clear()
            for tupla in dados:
                for tipo_escala in tupla:
                    self.tipo_escala.append(tipo_escala)

            self.roster_type_combobox_edit = ttk.Combobox(self.center_frame_07, values=self.tipo_escala,
                                                          textvariable=self.roster_type_var_edit,
                                                          state="readonly")
            self.roster_type_combobox_edit.pack(side=tk.TOP, pady=10, padx=40, fill=tk.BOTH)

            self.roster_type_var_edit.set(self.lista[2])
            self.roster_type_combobox_edit.current(self.tipo_escala.index(self.roster_type_var_edit.get()))

            self.lbl_data_inicio_edit = tk.Label(self.center_frame_07, text="Data de início da escala", bg='#94939B',font=('Inter', 18, 'bold'))
            self.lbl_data_inicio_edit.pack(side=tk.TOP, pady=10, padx=20)

            self.cal_data_inicio_edit = DateEntry(self.center_frame_07, locale='pt_BR', date_pattern='dd/MM/yyyy')
            self.cal_data_inicio_edit.pack(side=tk.TOP, pady=10, padx=40, fill=tk.BOTH)
            self.cal_data_inicio_edit.delete(0, tk.END)
            self.cal_data_inicio_edit.insert(0, self.lista[3])

            self.lbl_data_final_edit = tk.Label(self.center_frame_07, text="Data de Termino da escala", bg='#94939B',font=('Inter', 18, 'bold'))
            self.lbl_data_final_edit.pack(side=tk.TOP, pady=10, padx=20)

            self.cal_data_final_edit = DateEntry(self.center_frame_07, locale='pt_BR', date_pattern='dd/MM/yyyy')
            self.cal_data_final_edit.pack(side=tk.TOP, pady=10, padx=40, fill=tk.BOTH)
            self.cal_data_final_edit.delete(0, tk.END)
            self.cal_data_final_edit.insert(0, self.lista[4])

            self.frm_bttn_04 = tk.Frame(self.center_frame_07, bg='#94939B')
            self.frm_bttn_04.pack(side=tk.BOTTOM, pady=10, padx=10, expand=True)

            self.bttn_confirmar_edit = tk.Button(self.frm_bttn_04, text="Confirmar", command=self.confirm_roster_edit, font=("Arial", 10, "bold"), bg="#3CB371",fg="white", width=10, height=1, borderwidth=0)
            self.bttn_confirmar_edit.pack(side=tk.LEFT, padx=15, pady=10)

            self.bttn_limpar_edit = tk.Button(self.frm_bttn_04, text="Refazer", command=self.clear_edit_roster, font=("Arial", 10, "bold"), bg="Orange",fg="white", width=10, height=1, borderwidth=0)
            self.bttn_limpar_edit.pack(side=tk.LEFT, padx=15, pady=10)

            self.btn_cancelar_edit = tk.Button(self.frm_bttn_04, text="Cancelar", command=self.voltar_edit_roster, font=("Arial", 10, "bold"),bg="#E1523F", fg="white", width=10, height=1, borderwidth=0)
            self.btn_cancelar_edit.pack(side=tk.LEFT, padx=15, pady=10)

    def clear_edit_roster(self):
        self.roster_name_entry_edit.delete(0, "end")
        self.roster_name_entry_edit.insert(0, self.lista[1])

        self.cal_data_inicio_edit.delete(0, tk.END)
        self.cal_data_inicio_edit.insert(0, self.lista[3])

        self.cal_data_final_edit.delete(0, tk.END)
        self.cal_data_final_edit.insert(0, self.lista[4])

        self.roster_type_var_edit.set(self.lista[2])
        self.roster_type_combobox_edit.current(self.tipo_escala.index(self.roster_type_var_edit.get()))

    def confirm_roster_edit(self):
        selecionado = self.tvw_escala.selection()
        lista = self.tvw_escala.item(selecionado, "values")
        if selecionado != ():
            nome_escala = self.roster_name_entry_edit.get()
            tipo_escala = self.roster_type_combobox_edit.get()
            data_inicio = self.cal_data_inicio_edit.get_date().strftime('%d/%m/%Y')
            data_fim = self.cal_data_final_edit.get_date().strftime('%d/%m/%Y')

            if nome_escala == "":
                messagebox.showinfo("Insira um nome completo", "O campo nome da escala está incorreto!")
                self.edit_roster_screen.deiconify()
            elif tipo_escala == "":
                messagebox.showinfo("Insira os dias", "O campo tipo escala está vazio!")
                self.edit_roster_screen.deiconify()
            elif data_inicio == "":
                messagebox.showinfo("Selecione um tipo", "Nenhuma seleção na data de inicio!")
                self.edit_roster_screen.deiconify()
            elif data_fim == "":
                messagebox.showinfo("Selecione um tipo", "Nenhuma seleção na data de fim!")
                self.edit_roster_screen.deiconify()
            else:
                query = 'SELECT nome_escala FROM escala;'
                valores = bd.consultar_usuarios(query)
                confirmar = False
                for i in valores:
                    if nome_escala == i and i != lista[1]:
                        confirmar = True
                        break
                if not confirmar:
                    query = f"SELECT tipo_escala_id FROM tipo_escala WHERE '{tipo_escala}' LIKE nome_tipo_escala;"
                    dados = bd.consultar_usuarios(query)
                    query = f'UPDATE escala SET nome_escala="{nome_escala}", tipo_escala_id={dados[0]}, data_inicio_escala="{data_inicio}", data_fim_escala="{data_fim}" WHERE escala_id={lista[0]};'
                    bd.atualizar(query)
                    messagebox.showinfo("SUCESSO!", "Escala editada com sucesso!")
                    self.update_tvw_roster()
                    self.edit_roster_screen.destroy()
                    self.roster_manage.deiconify()
                else:
                    messagebox.showinfo("Nome de escala já cadastrado", "O Nome da escala já está cadastrado")
                    self.edit_roster_screen.deiconify()

    def delete_roster(self):
        selecionado = self.tvw_escala.selection()
        lista = self.tvw_escala.item(selecionado, "values")
        if selecionado != ():
            mensagem = messagebox.askyesno(f'Excluir', f'Você tem certeza que deseja excluir a escala: {lista[1]}?')
            if mensagem:
                sql = f'DELETE FROM escala WHERE escala_id={lista[0]};'
                bd.deletar(sql)
                self.update_tvw_roster()
                messagebox.showinfo("Excluído", "Escala excluída com sucesso")
            self.roster_manage.deiconify()

    def ReportScreen(self):
        self.report_screen = tk.Tk()
        self.report_screen.title("Gerenciar Relatorios")
        self.report_screen.geometry('1000x600')
        self.report_screen.configure(bg='#D9D9D9')
        self.report_screen.resizable(False, False)
        self.report_screen.protocol("WM_DELETE_WINDOW", self.voltar_report)

    def Escalas(self):
        selecionado = self.tvw_escala.selection()
        tupla = self.tvw_escala.item(selecionado, "values")
        if selecionado != ():
            query = f"SELECT escala_id FROM escala WHERE nome_escala = '{tupla[1]}';"
            dados = bd.consultar_usuarios(query)
            self.id_escala = dados[0]

            query = f"SELECT * FROM escala_usuario WHERE escala_id = {self.id_escala};"
            dados = bd.consultar_usuarios(query)

            if not dados:
                query = f"SELECT usuario_id FROM usuario;"
                dados = bd.consultar_usuarios(query)

                for usuario in dados:
                    query = f"INSERT INTO escala_usuario (escala_id, usuario_id, atribuido) VALUES ({self.id_escala}, {usuario}, 0);"
                    bd.inserir(query)

            self.roster_manage.iconify()
            self.roster_screen = tk.Tk()
            self.roster_screen.title("Escalas")
            self.roster_screen.geometry('900x700')
            self.roster_screen.configure(bg='#D9D9D9')
            self.roster_screen.resizable(False, False)
            self.roster_screen.protocol("WM_DELETE_WINDOW", self.voltar_escala)

            self.top_frame = tk.Frame(self.roster_screen, bg='#94939B')
            self.top_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

            self.top_top_frame = tk.Frame(self.top_frame, bg='#94939B')
            self.top_top_frame.pack(side=tk.TOP, fill=tk.BOTH)

            self.top_lbl_04 = tk.Label(self.top_top_frame, text='ESCALA', font=('Inter', 12, 'bold'),
                                       fg='#0B0B0B', bg='#94939B')
            self.top_lbl_04.pack(side=tk.TOP, pady=10, padx=10)

            self.frame_left = tk.Frame(self.top_frame, bg='#94939B')
            self.frame_left.pack(fill=tk.BOTH, expand=True, padx=20, pady=20, side=tk.LEFT)

            self.frame_right = tk.Frame(self.top_frame, bg='#94939B')
            self.frame_right.pack(fill=tk.BOTH, expand=True, padx=20, pady=20, side=tk.RIGHT)

            self.label_atribuir = tk.Label(self.frame_left, text='Atribuir usuário', font=('Inter', 18, 'bold'),
                                           fg='#0B0B0B', bg='#94939B')
            self.label_atribuir.pack(side=tk.TOP, pady=10, padx=10)

            self.label_atribuido = tk.Label(self.frame_right, text='Usuários atribuídos', font=('Inter', 18, 'bold'),
                                           fg='#0B0B0B', bg='#94939B')
            self.label_atribuido.pack(side=tk.TOP, pady=10, padx=10)

            self.frame_tvw_usuario_01 = tk.Frame(self.frame_left, bg='#94939B')
            self.frame_tvw_usuario_01.pack(side=tk.TOP, expand=True, fill=tk.Y)

            self.tvw_tree = ttk.Treeview(self.frame_tvw_usuario_01, columns=("Nome"), show="headings")
            self.tvw_tree.column('Nome', width=400)
            self.tvw_tree.heading("Nome", text="Nome Completo")
            self.tvw_tree.pack(side=tk.LEFT, fill=tk.BOTH, pady=10, expand=True)

            self.atualizar_tree()

            self.scrollbar = ttk.Scrollbar(self.frame_tvw_usuario_01, orient="vertical", command=self.tvw_tree.yview)
            self.scrollbar.pack(side=tk.LEFT, fill=tk.BOTH, pady=10)
            self.tvw_tree.configure(yscrollcommand=self.scrollbar.set)

            self.btn_atribuir = tk.Button(self.frame_left, text="Atribuir", font=('Inter', 10, 'bold'), fg='#070707',bg='#D9D9D9',
                                        command=self.atribuir_escala, borderwidth=0, height=2, width=10)
            self.btn_atribuir.pack(side=tk.LEFT, padx=175)


            self.frame_tvw_usuario_02 = tk.Frame(self.frame_right, bg='#94939B')
            self.frame_tvw_usuario_02.pack(side=tk.TOP, expand=True, fill=tk.Y)

            self.tvw_tree_02 = ttk.Treeview(self.frame_tvw_usuario_02, columns=("Prioridade","Nome"), show="headings")
            self.tvw_tree_02.column('Prioridade', width=65)
            self.tvw_tree_02.column('Nome', width=300)
            self.tvw_tree_02.heading("Nome", text="Nome completo")
            self.tvw_tree_02.heading("Prioridade", text="Prioridade")
            self.tvw_tree_02.pack(side=tk.LEFT, fill=tk.BOTH, pady=10, expand=True)

            self.scrollbar_02 = ttk.Scrollbar(self.frame_tvw_usuario_02, orient="vertical", command=self.tvw_tree.yview)
            self.scrollbar_02.pack(side=tk.LEFT, fill=tk.BOTH, pady=10)
            self.tvw_tree_02.configure(yscrollcommand=self.scrollbar_02.set)

            self.atualizar_tree_02()

            self.btn_remover = tk.Button(self.frame_right, text="Remover", font=('Inter', 10, 'bold'), fg='#070707',
                                          bg='#D9D9D9',
                                          command=self.remover_escala, borderwidth=0, height=2, width=10)
            self.btn_remover.pack(side=tk.LEFT, padx=10)

            # self.btn_up = tk.Button(self.frame_right, text=f"/\\", font=('Inter', 10, 'bold'), fg='#070707',
            #                               bg='#D9D9D9',
            #                               command="", borderwidth=0, width=15, height=2)
            # self.btn_up.pack(side=tk.LEFT, padx=10)
            #
            # self.btn_down = tk.Button(self.frame_right, text=f"\\/", font=('Inter', 10, 'bold'), fg='#070707',
            #                         bg='#D9D9D9',
            #                         command=self.down_prioridade, borderwidth=0, width=15, height=2)
            # self.btn_down.pack(side=tk.LEFT)

            self.top_center_frame = tk.Frame(self.top_frame, bg='#94939B')
            self.top_center_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=20, side=tk.LEFT)

            self.bottom_frame = tk.Frame(self.roster_screen, bg='#94939B')
            self.bottom_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

            self.btn_escalar = tk.Button(self.bottom_frame, text="ESCALAR", font=('Inter', 10, 'bold'), fg='#070707',
                                        bg='#D9D9D9',
                                        command=self.Escalar_Usuarios, borderwidth=0)
            self.btn_escalar.pack(side=tk.TOP, pady=10)

            self.calendar_frame_02 = tk.Frame(self.bottom_frame, bg='#94939B')
            self.calendar_frame_02.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

            self.cal_atrib = Calendar(self.calendar_frame_02, locale='pt_BR', date_pattern='dd/MM/yyyy')
            self.cal_atrib.pack(side=tk.TOP, expand=True)

            self.btn_voltar = tk.Button(self.calendar_frame_02, text="Voltar", font=('Inter', 10, 'bold'), fg='#000',bg='#FFF',
                                        command=self.voltar_escala, borderwidth=0, width=20)
            self.btn_voltar.pack(side=tk.LEFT, pady=5, padx=5)
            self.atuliza_calendario_atribuir()

    def atuliza_calendario_atribuir(self):
        for item_id in self.tvw_tree_02.get_children():
            item_values = self.tvw_tree_02.item(item_id, "values")
            print(item_values)

            query = f'''SELECT eu.escala_usuario_id
            FROM escala_usuario eu
            JOIN usuario u ON u.usuario_id = eu.usuario_id
            WHERE u.nome_completo LIKE "{item_values[1]}"
            AND eu.escala_id = {self.id_escala};'''

        # # # query = f"SELECT escala_usuario_id FROM escala_usuario_id WHERE  "

            dados = bd.consultar(query)
            print(dados)
            self.escala_usuario_id = 0

            self.escala_usuario_id = dados[0][0]

            query = f"SELECT data_inicio, data_fim FROM escala_usuario WHERE escala_usuario_id = {self.escala_usuario_id}"
            dados = bd.consultar(query)
            # print(dados)

            if dados != [('', '')]:
                data_inicio_escala = datetime.strptime(str(dados[0][0]), '%d/%m/%Y')
                data_fim_escala = datetime.strptime(str(dados[0][1]), '%d/%m/%Y')

                # # Calcule o número de dias totais na escala
                dias_totais = (data_fim_escala - data_inicio_escala).days + 1
                data_evento = datetime.strptime(dados[0][0], "%d/%m/%Y").date()

                dias_totais_variavel = dias_totais

                while dias_totais_variavel != 0:

                    data_evento = data_evento + timedelta(days=1)

                    print(data_evento)
                    self.cal_atrib.calevent_create(data_evento, f'Dias_Das_Escalas', f'Dias_Das_Escalas')
                    
                    dias_totais_variavel -= 1
                self.cal_atrib.tag_config('Dias_Das_Escalas', background="#FFFACD", foreground='black')


    def Escalar_Usuarios(self):
        query = f"SELECT data_inicio_escala, data_fim_escala FROM escala Where escala_id = {self.id_escala};"
        dados = bd.consultar(query)
        datas = dados[0]
        # print(datas[0], datas[1])

        data_inicio_escala = datetime.strptime(str(datas[0]), '%d/%m/%Y')
        data_fim_escala = datetime.strptime(str(datas[1]), '%d/%m/%Y')

        # # Calcule o número de dias totais na escala
        dias_totais = (data_fim_escala - data_inicio_escala).days + 1
        # print(f"Dias totais da escala: {dias_totais}")
        all_items = []
        for item_id in self.tvw_tree_02.get_children():
            item_values = self.tvw_tree_02.item(item_id, "values")
            all_items.append(item_values)
        
        funcionarios = all_items

        # print(len(funcionarios))
        # Calcule a quantidade de dias que cada funcionário deve ter inicialmente
        dias_por_funcionario = dias_totais // len(funcionarios)

        print(f"Dias por funcionario: {dias_por_funcionario}")

        # Distribua os dias da escala entre os funcionários
        dias_restantes = dias_totais

        for funcionario in funcionarios:
            if dias_restantes > 0:
                dias_atribuidos = min(dias_por_funcionario, dias_restantes)
                data_inicio = data_inicio_escala + timedelta(days=dias_totais - dias_restantes)
                data_fim = data_inicio + timedelta(days=dias_atribuidos - 1)
                # print(funcionario[1])
                # print(f"\nData inicio: {data_inicio}")
                # print(f"\nData fim: {data_fim}")
                print("-----------------------------------------------------")
                data_inicio = data_inicio.strftime('%d/%m/%Y')
                data_fim = data_fim.strftime('%d/%m/%Y')
                print(data_inicio, data_fim)
                query = f"SELECT usuario_id FROM usuario Where nome_completo LIKE '{funcionario[1]}';"
                dados = bd.consultar(query)
                query = f"UPDATE escala_usuario SET data_inicio = '{data_inicio}', data_fim = '{data_fim}' WHERE usuario_id = {dados[0][0]} and escala_id = {self.id_escala}"
                bd.atualizar(query)
                # self.cal_atrib

                
                dias_restantes -= dias_atribuidos

        print(f"Dias que sobraram: {dias_restantes}")



        # for data in datas:
        #     data_evento = datetime.strptime(data[0], "%d/%m/%Y")
        #     # print(data_evento)
        #     começo = 1
        #     cont_dias = dias_escala[0]
        #     while cont_dias != 0:

        #         if começo == 1:
        #             data_evento = data_evento + timedelta(days=0)
        #         else:
        #             data_evento = data_evento + timedelta(days=1)
        #         self.cal_atrib.calevent_create(data_evento , f'Dias_Das_Escalas', f'Dias_Das_Escalas')
        #         # print(cont_dias)
        #         cont_dias -= 1
        #         começo = 0
        #         if finais_semana != 1:
        #             data = date(data_evento.year, data_evento.month, data_evento.day)
        #             indice_da_semana = data.weekday()
        #             dia_da_semana = self.DIAS[indice_da_semana]
        #             numero_do_dia_da_semana = data.isoweekday()
        #             if(numero_do_dia_da_semana == 6 or numero_do_dia_da_semana == 7 ):
        #                 cont_dias += 1
        #                 self.cal_atrib.calevent_create(data_evento , 'Cor_padrão', 'Cor_padrão')
        #                 self.cal_atrib.tag_config("Cor_padrão", background="#cccccc", foreground='black')

        #     self.cal_atrib.tag_config('Dias_Das_Escalas', background="#FFFACD", foreground='black')
        
        # if feriados != 1:
        #     self.calendar_ferias(2)




    def atualizar_tree(self):
        for i in self.tvw_tree.get_children():
            self.tvw_tree.delete(i)
        query = f"SELECT u.nome_completo FROM usuario AS u INNER JOIN escala_usuario AS eu ON u.usuario_id = eu.usuario_id WHERE eu.atribuido = 0 AND eu.escala_id = {self.id_escala};"

        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw_tree.insert('', tk.END, values=tupla)

    def atualizar_tree_02(self):
        for i in self.tvw_tree_02.get_children():
            self.tvw_tree_02.delete(i)
        query = f"SELECT eu.prioridade, u.nome_completo FROM usuario AS u INNER JOIN escala_usuario AS eu ON u.usuario_id = eu.usuario_id WHERE eu.atribuido = 1 AND eu.escala_id = {self.id_escala} ORDER BY eu.prioridade;"
        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw_tree_02.insert('', tk.END, values=tupla)

    def get_all_items(self, tree):
        items = []
        for item in tree.get_children():
            items.append(tree.item(item)["values"])
        return items

    def atribuir_escala(self):
        selecionado = self.tvw_tree.selection()
        tupla = self.tvw_tree.item(selecionado, "values")

        valores_arvore_02 = self.get_all_items(self.tvw_tree_02)

        if not valores_arvore_02:
            prioridade = 1
        else:
            prioridade = len(valores_arvore_02) + 1

        if selecionado != ():
            query = f"UPDATE escala_usuario SET atribuido = '1', prioridade = {prioridade} WHERE escala_id = {self.id_escala} AND usuario_id = (SELECT usuario_id FROM usuario WHERE nome_completo = '{tupla[0]}');"
            bd.atualizar(query)
        self.atualizar_tree()
        self.atualizar_tree_02()

    def remover_escala(self):
        selecionado = self.tvw_tree_02.selection()
        tupla = self.tvw_tree_02.item(selecionado, "values")

        if selecionado != ():
            query = f"UPDATE escala_usuario SET atribuido = '0', prioridade='0' WHERE escala_id = {self.id_escala} AND usuario_id = (SELECT usuario_id FROM usuario WHERE nome_completo = '{tupla[1]}');"
            bd.atualizar(query)

            query = f"SELECT * FROM escala_usuario AS eu WHERE atribuido = 1 AND escala_id = {self.id_escala} ORDER BY eu.prioridade;"
            dados = bd.consultar(query)
            prioridade = 0
            for dado in dados:
                prioridade += 1
                query = f"UPDATE escala_usuario SET atribuido = '1', prioridade='{prioridade}' WHERE escala_id = {self.id_escala} AND usuario_id = {dado[2]} ;"
                bd.atualizar(query)

        self.atualizar_tree()
        self.atualizar_tree_02()

    def down_prioridade(self):
        selecionado = self.tvw_tree_02.selection()
        tupla = self.tvw_tree_02.item(selecionado, "values")
        #query = f"SELECT COUNT(*) FROM escala_usuario WHERE escala_id = {self.id_escala};"
        #dados = bd.consultar_usuarios(query)

        valores_arvore_02 = self.get_all_items(self.tvw_tree_02)

        num_usuarios = len(valores_arvore_02)

        if selecionado != () and int(tupla[0]) != num_usuarios:
            query = f"UPDATE escala_usuario SET prioridade = '{tupla[0]}' WHERE usuario_id = (SELECT usuario_id FROM usuario WHERE nome_completo = '{tupla[1]}');"

    # def verifica_termino_escalas(self):
    #     chave_mes = 0
    #     chave_ano = 0 #OUTRO DIA FAÇO ESSE PQP
    #     data_atual = datetime.now()
    #     data_completa = data_atual.strftime("%d/%m/%Y")#%H:%M:%S
    #
    #     # print("O dia atual é:", data_completa)
    #
    #     query = f"SELECT escala_id, data_inicio FROM usuario_escala;"
    #     dados = bd.consultar_usuarios(query)
    #
    #     if dados != []:
    #
    #         #pares = [(dados[i], dados[i + 1]) for i in range(0, len(dados), 2)]
    #         #print(pares)
    #         #for dados in pares:
    #             id = dados[0]
    #
    #             data = dados[1]
    #
    #             data = datetime.strptime(data, "%d/%m/%Y")
    #
    #             Ultimo_dia_mes = data.replace(day=monthrange(data.year, data.month)[1])
    #
    #             data = str(dados[1])
    #             data = data.split("/")
    #             # print(data)



janela = tk.Tk()
Screens(janela)
janela.mainloop()