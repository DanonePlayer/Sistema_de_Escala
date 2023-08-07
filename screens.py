import tkinter as tk
##from tkinter import PhotoImage, ttk, messagebox,RAISED, RIDGE
from tkinter import ttk
from PIL import Image, ImageTk

##from tkcalendar import Calendar, DateEntry
##import holidays

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
        self.top_lbl.pack(side=tk.LEFT, pady=10, padx=50)

        self.left_frm = tk.Frame(self.login_screen,bg='#D9D9D9')
        self.left_frm.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        #self.img_pf = tk.PhotoImage(file="images/image 1.png", height=425, width=336)
        self.img_pf = ImageTk.PhotoImage(Image.open(f"images/image 1.png"))

        self.left_lbl = tk.Label(self.left_frm, image=self.img_pf, height=425, width=336, bg='#D9D9D9')
        self.left_lbl.pack(side=tk.LEFT, pady=10, padx=50)

        self.left_lbl.configure(image=self.img_pf)
        self.left_lbl.image=self.img_pf

        self.right_frm = tk.Frame(self.login_screen, width=421, height=542)
        self.right_frm.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.right_lbl = tk.Label(self.right_frm, bg='#94939B')
        self.right_lbl.pack(side=tk.LEFT, fill=tk.BOTH)

        self.text_lbl = tk.Label(self.right_lbl, bg='#94939B', text='LOGIN', font=('Inter', 24, 'bold'), fg='#0B0B0B')
        self.text_lbl.pack(side=tk.TOP, pady=30, padx=20)

        self.entry_nome = tk.Entry(self.right_lbl, width=200, bg='#D9D9D9', justify="center", font=('Inter', 24 , 'bold'), fg='#94939B')
        self.entry_nome.insert(0, "Nome de Usuario")
        self.entry_nome.pack(side=tk.TOP, pady=20, padx=20)

        self.entry_senha = tk.Entry(self.right_lbl, width=200, bg='#D9D9D9', justify="center",font=('Inter', 24, 'bold'), fg='#94939B')
        self.entry_senha.insert(0, "Senha")
        self.entry_senha.pack(side=tk.TOP, pady=20, padx=20)

        self.bttn_login = tk.Button(self.right_lbl, font=('Inter', 24, 'bold'), fg='#FFFFFF', text="ENTRAR", bg='#6A6666',command=self.enter)
        self.bttn_login.pack(side=tk.BOTTOM, pady=20, padx=100)

        self.bttn_help = tk.Button(self.right_lbl, font=('Inter', 20, 'bold'), fg='#6A6666', text=" Problemas de Login? ", bg='#94939B', borderwidth=0,command='')
        self.bttn_help.pack(fill=tk.BOTH)
        self.bttn_help.config()

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


        self.img_pf_02 = ImageTk.PhotoImage(Image.open(f"images/image 1.png"))

        self.left_lbl_02 = tk.Label(self.left_frm_2, image=self.img_pf_02, height=425, width=336, bg='#94939B')
        self.left_lbl_02.pack(side=tk.TOP,padx=10,pady=10)

        self.img_calendar = ImageTk.PhotoImage(Image.open((f'Images/calendar_icon.png')))
        self.img_user = ImageTk.PhotoImage(Image.open((f'Images/user_icon.png')))
        self.img_roster = ImageTk.PhotoImage(Image.open((f'Images/roster_icon.png')))
        self.img_roster_02 = ImageTk.PhotoImage(Image.open(f'Images/roster_icon_02.png'))
        self.img_reports = ImageTk.PhotoImage(Image.open((f'Images/chart-bar.png')))
        self.img_edit = ImageTk.PhotoImage(Image.open((f'Images/calendar-minus.png')))


        self.top_frame = tk.Frame(self.right_frm_2,bg='#565656')
        self.top_frame.pack(side=tk.TOP,padx=10,pady=10,fill=tk.BOTH,expand=True)

        self.bottom_frame = tk.Frame(self.right_frm_2, bg='#565656')
        self.bottom_frame.pack(side=tk.BOTTOM,padx=10,pady=10,fill=tk.BOTH,expand=True)

        self.bttn_calendar = tk.Button(self.top_frame, bg='#6E716E', command=self.calendar,image=self.img_calendar)
        self.bttn_calendar.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.bttn_raltorio = tk.Button(self.top_frame, bg='#6E716E', image=self.img_reports)
        self.bttn_raltorio.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.bttn_usuario = tk.Button(self.top_frame, bg='#6E716E', command=self.user, image=self.img_user)
        self.bttn_usuario.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.bttn_escalas = tk.Button(self.bottom_frame, bg='#6E716E', command=self.roster, image=self.img_roster)
        self.bttn_escalas.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.bttn_criar = tk.Button(self.bottom_frame, bg='#6E716E',command=self.create,image=self.img_roster_02)
        self.bttn_criar.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.bttn_hist = tk.Button(self.bottom_frame, bg='#6E716E', image=self.img_edit)
        self.bttn_hist.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

    def roster(self):
        self.main_screen.destroy()
        self.RosterScreen()

    def calendar(self):
        self.main_screen.destroy()
        self.CalendarScreen()

    def user(self):
        self.main_screen.destroy()
        self.UserScreen()
    def crud_user(self):
        self.user_screen.destroy()
        self.CrudScreen()
    def voltar_calendar(self):
        self.calendar_screen.destroy()
        self.MainScreen()
    def voltar_roster(self):
        self.roster_screen.destroy()
        self.MainScreen()
    def voltar_user(self):
        self.user_screen.destroy()
        self.MainScreen()
    def voltar_crud(self):
        self.crud_user.destroy()
        self.UserScreen()

    def voltar_create(self):
        self.create_screen.destroy()
        self.MainScreen()
    def create(self):
        self.main_screen.destroy()
        self.CreateScreen()

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
        self.top_frame_02.grid(row=0, column=0, pady=20, padx=10)

        self.top_lbl_04 = tk.Label(self.top_frame_02, text='CALENDARIO DE ESCALAS', font=('Inter', 12, 'bold'),fg='#0B0B0B', bg='#94939B')
        self.top_lbl_04.pack(side=tk.LEFT, pady=20, padx=20)

        self.middle_frame = tk.Frame(self.center_frame_02, bg='#D9D9D9')
        self.middle_frame.grid(row=1, column=0, pady=20, padx=10)

        combo_var = tk.StringVar()
        self.combo_box = ttk.Combobox(self.middle_frame, textvariable=combo_var,values=["Opção 1", "Opção 2", "Opção 3"])
        self.combo_box.pack(pady=20, padx=20, side=tk.LEFT)

        self.middle_label = tk.Label(self.middle_frame, text='DIAS', font=('Inter', 10, 'bold'), fg='#FFF',bg='#94939B')
        self.middle_label.pack(side=tk.LEFT, pady=10, padx=10)

        self.entry_dias = tk.Entry(self.middle_frame)
        self.entry_dias.pack(side=tk.LEFT, pady=10, padx=10)

        self.bttn_edit = tk.Button(self.middle_frame, text='EDITAR', font=('Inter', 10, 'bold'), fg='#FFF',bg='#FF7F50',command='')
        self.bttn_edit.pack(side=tk.LEFT, pady=10, padx=10)

        self.calendar_frame_02 = tk.Frame(self.center_frame_02)
        self.calendar_frame_02.grid(row=2, column=0, pady=10, padx=10)

        self.calendar_lbl = tk.Label(self.calendar_frame_02, bg='#94939B', width=70, height=15) ##Coloque o calendario aqui, pode aumentar a resolução da tela se achar que precisa de mais espaço
        self.calendar_lbl.pack(pady=10, padx=40)

        self.bottom_frame_02 = tk.Frame(self.center_frame_02)
        self.bottom_frame_02.grid(row=3, column=0)

        self.bttn_voltar = tk.Button(self.bottom_frame_02, text='VOLTAR', font=('Inter', 10, 'bold'), fg='#605F5F',bg='#FFF',command=self.voltar_roster)
        self.bttn_voltar.pack(side=tk.LEFT)

        self.frame_right = tk.Frame(self.big_frame,bg='#94939B')
        self.frame_right.pack(fill=tk.BOTH, expand=True, padx=20, pady=20,side=tk.RIGHT)

        self.entry_pesquisa = tk.Entry(self.frame_right,width=60,font=('Inter', 10 , 'bold'), fg='#94939B')
        self.entry_pesquisa.grid(row=0,column=0,sticky='NW',padx=5,pady=10)
        self.entry_pesquisa.insert(0, "Pesquisar")

        self.frame_right.grid_columnconfigure(1, minsize=20)

        self.bttn_pesquisa = tk.Button(self.frame_right,width=3,height=0,command='')
        self.bttn_pesquisa.grid(row=0, column=0,padx=5,sticky='NE',pady=10)

        self.tree = ttk.Treeview(self.frame_right, columns=("ID", "Nome"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.grid(row=1, column=0,sticky='NSEW', padx=5, pady=10,columnspan=True)

        self.scrollbar = ttk.Scrollbar(self.frame_right, orient="vertical", command=self.tree.yview)
        self.scrollbar.grid(row=1, column=0,sticky='NSE',padx=5, pady=10)

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.btt_add = tk.Button(self.frame_right,text='ADICIONAR',font=('Inter', 10, 'bold'), fg='#070707',bg='#D9D9D9',width=19,height=5,command='')
        self.btt_add.grid(row=2,column=0,sticky='NSEW',pady=50,padx=50)


    def CalendarScreen(self):
        self.calendar_screen = tk.Tk()
        self.calendar_screen.title("Calendario")
        self.calendar_screen.geometry('1253x588')
        self.calendar_screen.configure(bg='#D9D9D9')
        self.calendar_screen.resizable(False, False)
        self.calendar_screen.protocol("WM_DELETE_WINDOW", self.voltar_calendar)

        self.center_frame = tk.Frame(self.calendar_screen, width=1253, height=588, bg='#94939B')
        self.center_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.calendar_frame = tk.Frame(self.center_frame,bg='#D9D9D9',width=906,height=449) ## Usem esse frame para colocar o calendario principal
        self.calendar_frame.pack(side=tk.TOP,padx=20, pady=20,fill=tk.BOTH)

        self.lbl_text = tk.Label(self.calendar_frame,text='CALENDARIO GERAL DE ESCALAS', font=('Inter',18,'bold'), fg='#0B0B0B', bg='#94939B')
        self.lbl_text.pack(side=tk.TOP)

        self.buttons_frame= tk.Frame(self.center_frame)
        self.buttons_frame.pack(side=tk.BOTTOM,padx=20, pady=20)

        self.bttn_back = tk.Button(self.buttons_frame,text='VOLTAR',font=('Inter',10,'bold'), fg='#605F5F', bg='#FFF', command=self.voltar_calendar)
        self.bttn_back.pack(side=tk.BOTTOM,pady=20,padx=20)

    def UserScreen(self):
        self.user_screen = tk.Tk()
        self.user_screen.title("Usuarios")
        self.user_screen.geometry('800x620')
        self.user_screen.configure(bg='#D9D9D9')
        self.user_screen.resizable(False, False)
        self.user_screen.protocol("WM_DELETE_WINDOW", self.voltar_user)

        self.lbl_name = tk.Label(self.user_screen, text='GERENCIAR USUÁRIOS', font=('Inter', 18, 'bold'), fg='#0B0B0B',bg='#D9D9D9')
        self.lbl_name.pack(side=tk.TOP, pady=(20, 5))

        self.frm = tk.Frame(self.user_screen, bg='#94939B')
        self.frm.pack(pady=10, padx=10,expand=True,fill=tk.BOTH)

        self.frame_tvw_usuario = tk.Frame(self.frm, bg='#94939B')
        self.frame_tvw_usuario.pack(pady=20, padx=20,expand=True, fill=tk.BOTH)

        self.tvw_usuario = ttk.Treeview(self.frame_tvw_usuario, columns=('id', 'nome', 'nome de usuario', 'tipo'),show='headings')
        self.tvw_usuario.column('id', width=40)
        self.tvw_usuario.column('nome', width=250)
        self.tvw_usuario.column('nome de usuario', width=150)
        self.tvw_usuario.column('tipo', width=100)
        self.tvw_usuario.heading('id', text='Id')
        self.tvw_usuario.heading('nome', text='Nome')
        self.tvw_usuario.heading('nome de usuario', text='Nome de Usuário')
        self.tvw_usuario.heading('tipo', text='Super usuário')
        self.tvw_usuario.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

        self.scr_usuario = ttk.Scrollbar(self.frame_tvw_usuario, command=self.tvw_usuario.yview)
        self.scr_usuario.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw_usuario.configure(yscroll=self.scr_usuario.set)

        self.frame_tvw_button = tk.Frame(self.frm, bg='#94939B')
        self.frame_tvw_button.pack(side=tk.BOTTOM)

        self.btn_cadastrar_usuario = tk.Button(self.frame_tvw_button, text="Criar Usuário", font=("Arial", 10), bg="#3CB371",fg="white", width=20, height=1,borderwidth=0,command=self.crud_user)
        self.btn_cadastrar_usuario.grid(row=0,column=0,padx=10,pady=10)

        self.btn_editar_usuario = tk.Button(self.frame_tvw_button, text="Editar Usuário", font=("Arial", 10), bg="Orange", fg="white",width=20, height=1,borderwidth=0,command='')
        self.btn_editar_usuario.grid(row=0,column=1,padx=10,pady=10)

        self.btn_excluir_usuario = tk.Button(self.frame_tvw_button, text="Excluir Usuário", font=("Arial", 10), bg="#E1523F",fg="white", width=20, height=1,borderwidth=0,command='')
        self.btn_excluir_usuario.grid(row=0,column=2,padx=10,pady=10)

        self.btn_excluir_usuario = tk.Button(self.frame_tvw_button, text="Voltar", font=("Arial", 10),bg="#E1523F", fg="white", width=20, height=1, borderwidth=0, command=self.voltar_user)
        self.btn_excluir_usuario.grid(row=0, column=3, padx=10, pady=10)

    def CrudScreen(self):
        self.crud_user = tk.Tk()
        self.crud_user.title("Cadastrar usuario")
        self.crud_user.geometry('462x676')
        self.crud_user.configure(bg='#D9D9D9')
        self.crud_user.resizable(False, False)

        self.lbl_name = tk.Label(self.crud_user, text='CRIAR USUÁRIO', font=('Inter', 18, 'bold'), fg='#0B0B0B',bg='#D9D9D9')
        self.lbl_name.pack(side=tk.TOP,pady=(20,5))

        self.center_frame_04 = tk.Frame(self.crud_user,bg='#94939B')
        self.center_frame_04.pack(pady=20,padx=20,expand=True,fill=tk.BOTH)

        tk.Label(self.center_frame_04, text="Nome Completo:", bg='#94939B',font=('Inter', 18, 'bold')).grid(row=0, column=0, padx=110, pady=(20,5),sticky='nsew')

        self.full_name_entry = tk.Entry(self.center_frame_04)
        self.full_name_entry.grid(row=1, column=0, padx=110, pady=(20,5),sticky='nswe')

        tk.Label(self.center_frame_04, text="Nome de usuário:", bg='#94939B',font=('Inter', 18, 'bold')).grid(row=2, column=0, padx=110, pady=(20,5),sticky='nswe')

        self.username_entry = tk.Entry(self.center_frame_04)
        self.username_entry.grid(row=3, column=0, padx=110, pady=(20,5),sticky='nswe')

        tk.Label(self.center_frame_04, text="Senha:", bg='#94939B',font=('Inter', 18, 'bold')).grid(row=4, column=0, padx=110, pady=(20,5), sticky='nswe')

        self.password_entry = tk.Entry(self.center_frame_04, show='*')
        self.password_entry.grid(row=5, column=0, padx=110, pady=(20,5),sticky='nswe')

        tk.Label(self.center_frame_04, text="Confirmar senha:", bg='#94939B',font=('Inter', 18, 'bold')).grid(row=6, column=0, padx=110, pady=(20,5),sticky='nswe')

        self.confirm_password_entry = tk.Entry(self.center_frame_04, show='*')
        self.confirm_password_entry.grid(row=7, column=0, padx=110, pady=(20,5),sticky='nswe')

        tk.Label(self.center_frame_04, text="Tipo de usuário:", bg='#94939B',font=('Inter', 18, 'bold')).grid(row=8, column=0, padx=110, pady=(20,5),sticky='nswe')

        self.user_type_var = tk.StringVar()
        self.user_type_combobox = ttk.Combobox(self.center_frame_04, textvariable=self.user_type_var,values=["Administrador", "Usuário Comum"])
        self.user_type_combobox.grid(row=9, column=0, padx=110, pady=(20,5),sticky='nswe')
        self.user_type_combobox.set("Usuário Comum")

        self.btn_conf  = tk.Button(self.crud_user, text="Confirmar", command="",font=("Arial", 10), bg="#3CB371",fg="white", width=10, height=1,borderwidth=0).pack(side='left', padx=35,pady=10)
        self.btn_limp = tk.Button(self.crud_user, text="Limpar", command="", font=("Arial", 10), bg="Orange", fg="white",width=10, height=1,borderwidth=0).pack(side='left', padx=37,pady=10)
        self.btn_cancel = tk.Button(self.crud_user, text="Cancelar", command=self.voltar_crud, font=("Arial", 10), bg="#E1523F",fg="white", width=10, height=1,borderwidth=0).pack(side='left', padx=35, pady=10)

    def CreateScreen(self):
        self.create_screen = tk.Tk()
        self.create_screen.title('Criar Escalas')
        self.create_screen.geometry('517x877')
        self.create_screen.configure(bg='#D9D9D9')
        self.create_screen.resizable(False, False)
        self.create_screen.protocol("WM_DELETE_WINDOW", self.voltar_create)

        self.center_frame_03 = tk.Frame(self.create_screen,bg='#94939B')
        self.center_frame_03.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.lbl_create = tk.Label(self.center_frame_03,text='CRIAR ESCALA',font=('Inter', 18, 'bold'),fg='#0B0B0B', bg='#94939B' )
        self.lbl_create.pack(side=tk.TOP,padx=5,pady=10)

        self.lbl_name = tk.Label(self.center_frame_03, text="NOME DA ESCALA",font=('Inter', 18, 'bold'),fg='#FFF',bg='#94939B')
        self.lbl_name.pack(side=tk.TOP,pady=5,padx=10)

        self.entry_nome_e = tk.Entry(self.center_frame_03, width=59)
        self.entry_nome_e.pack(side=tk.TOP, padx=5, pady=10)

        self.lbl_dias = tk.Label(self.center_frame_03,text='QUANTOS DIAS?',font=('Inter', 18, 'bold'),fg='#FFF',bg='#94939B')
        self.lbl_dias.pack(side=tk.TOP, padx=5, pady=10, fill=tk.BOTH)

        self.entry_dias_02 = tk.Entry(self.center_frame_03, width=59)
        self.entry_dias_02.pack(side=tk.TOP, padx=5, pady=10,)

        self.frame_escolhas = tk.Frame(self.center_frame_03,bg='#94939B')
        self.frame_escolhas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10,side=tk.TOP)

        self.lbl_03 = tk.Label(self.frame_escolhas, text='CONTAR FINAIS DE SEMANA?', font=('Inter', 18, 'bold'),fg='#FFF', bg='#94939B')
        self.lbl_03.grid(row=0, column=0, columnspan=3, sticky='nsew', pady=20)

        radio_var_01 = tk.StringVar()
        radio_var_02 = tk.StringVar()
        radio_var_03 = tk.StringVar()

        style = ttk.Style()
        style.configure("Custom.TRadiobutton", background="#94939B", foreground="white", font=("Inter", 12, "bold"))

        self.radio_01 = ttk.Radiobutton(self.frame_escolhas, text="SIM", variable=radio_var_01, value="SIM_1",style="Custom.TRadiobutton")
        self.radio_01.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
        self.radio_02 = ttk.Radiobutton(self.frame_escolhas, text="NÃO", variable=radio_var_01, value="NÃO_1",style="Custom.TRadiobutton")
        self.radio_02.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')

        self.lbl_04 = tk.Label(self.frame_escolhas, text='CONTAR FERIADOS?', font=('Inter', 18, 'bold'), fg='#FFF',bg='#94939B')
        self.lbl_04.grid(row=3, column=0, columnspan=2, sticky='nsew', pady=20)

        self.radio_03 = ttk.Radiobutton(self.frame_escolhas, text="SIM", variable=radio_var_02, value="SIM_2",style="Custom.TRadiobutton")
        self.radio_03.grid(row=4, column=0, padx=10, pady=10, sticky='nsew')
        self.radio_04 = ttk.Radiobutton(self.frame_escolhas, text="NÃO", variable=radio_var_02, value="NÃO_2",style="Custom.TRadiobutton")
        self.radio_04.grid(row=4, column=1, padx=10, pady=10, sticky='nsew')

        self.lbl_05 = tk.Label(self.frame_escolhas, text='ESCALA MUTUA?', font=('Inter', 18, 'bold'), fg='#FFF',bg='#94939B')
        self.lbl_05.grid(row=5, column=0, columnspan=2, sticky='nsew', pady=20)

        self.radio_06 = ttk.Radiobutton(self.frame_escolhas, text="SIM", variable=radio_var_03, value="SIM_2",style="Custom.TRadiobutton")
        self.radio_06.grid(row=6, column=0, padx=10, pady=10, sticky='nsew')
        self.radio_07 = ttk.Radiobutton(self.frame_escolhas, text="NÃO", variable=radio_var_03, value="NÃO_2",style="Custom.TRadiobutton")
        self.radio_07.grid(row=6, column=1, padx=10, pady=10, sticky='nsew')

        self.frame_button = tk.Frame(self.center_frame_03,bg='#94939B')
        self.frame_button.pack(fill=tk.BOTH, expand=True, padx=10, pady=10,side=tk.BOTTOM)

        self.bttn_criar_02 = tk.Button(self.frame_button, text='CRIAR', font=('Inter', 18, 'bold'), fg='#FFF',bg='#1B731A',command='')
        self.bttn_criar_02.pack(side=tk.LEFT,pady=5,padx=10)

        self.bttn_clean = tk.Button(self.frame_button, text='LIMPAR', font=('Inter', 18, 'bold'), fg='#605F5F',bg='#FFFFFF',command='')
        self.bttn_clean.pack(side=tk.RIGHT,pady=5,padx=10)


janela = tk.Tk()
Screens(janela)
janela.mainloop()