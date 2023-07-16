import tkinter as tk
from tkinter import PhotoImage, ttk, messagebox,RAISED, RIDGE
from tkinter import ttk
from PIL import Image, ImageTk

from tkcalendar import Calendar, DateEntry
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

        self.bttn_help = tk.Button(self.right_lbl, font=('Inter', 20, 'bold'), fg='#6A6666', text=" Problemas de Login? ", bg='#94939B', borderwidth=0)
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


        self.top_frame = tk.Frame(self.right_frm_2,bg='#D9D9D9')
        self.top_frame.pack(side=tk.TOP,padx=10,pady=10,fill=tk.BOTH,expand=True)

        self.bottom_frame = tk.Frame(self.right_frm_2, bg='#D9D9D9')
        self.bottom_frame.pack(side=tk.BOTTOM,padx=10,pady=10,fill=tk.BOTH,expand=True)

        self.bttn_calendar = tk.Button(self.top_frame, bg='#6E716E', command=self.calendar,image=self.img_calendar)
        self.bttn_calendar.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.bttn_raltorio = tk.Button(self.top_frame, bg='#6E716E')
        self.bttn_raltorio.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.bttn_usuario = tk.Button(self.top_frame, bg='#6E716E', command=self.user, image=self.img_user)
        self.bttn_usuario.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.bttn_escalas = tk.Button(self.bottom_frame, bg='#6E716E', command=self.roster, image=self.img_roster)
        self.bttn_escalas.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.bttn_criar = tk.Button(self.bottom_frame, bg='#6E716E')
        self.bttn_criar.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill=tk.BOTH)

        self.bttn_hist = tk.Button(self.bottom_frame, bg='#6E716E')
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

        self.top_frame_02 = tk.Frame(self.center_frame_02)
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

        self.bttn_edit = tk.Button(self.middle_frame, text='EDITAR', font=('Inter', 10, 'bold'), fg='#FFF',bg='#FF7F50')
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

        self.bttn_pesquisa = tk.Button(self.frame_right,width=3,height=0)
        self.bttn_pesquisa.grid(row=0, column=0,padx=5,sticky='NE',pady=10)

        self.tree = ttk.Treeview(self.frame_right, columns=("ID", "Nome"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.grid(row=1, column=0,sticky='NSEW', padx=5, pady=10,columnspan=True)

        self.scrollbar = ttk.Scrollbar(self.frame_right, orient="vertical", command=self.tree.yview)
        self.scrollbar.grid(row=1, column=0,sticky='NSE',padx=5, pady=10)

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.btt_add = tk.Button(self.frame_right,text='ADICIONAR',font=('Inter', 10, 'bold'), fg='#070707',bg='#D9D9D9',width=19,height=5)
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
        self.user_screen.geometry('560x591')
        self.user_screen.configure(bg='#D9D9D9')
        self.user_screen.resizable(False, False)
        self.user_screen.protocol("WM_DELETE_WINDOW", self.voltar_user)


    def CrudScreen(self):
        self.crud_user = tk.Tk()
        self.crud_user.title("Cadastrar usuario")
        self.crud_user.geometry('462x676')
        self.crud_user.configure(bg='#D9D9D9')
        self.crud_user.resizable(False, False)

janela = tk.Tk()
Screens(janela)
janela.mainloop()