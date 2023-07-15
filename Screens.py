import tkinter as tk
from tkinter import PhotoImage, ttk, messagebox,RAISED, RIDGE
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

        self.top_frm = tk.Frame(self.login_screen, height=100, width=100)
        self.top_frm.pack(fill=tk.X, padx=20, pady=20)

        self.top_lbl = tk.Label(self.top_frm, text = "BEM VINDO", font=('Inter',28,'bold'), fg='#0B0B0B')
        self.top_lbl.pack(side=tk.LEFT, pady=10, padx=50,)

        self.left_frm = tk.Frame(self.login_screen)
        self.left_frm.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

        #self.img_pf = tk.PhotoImage(file="images/image 1.png", height=425, width=336)
        self.img_pf = ImageTk.PhotoImage(Image.open(f"images/image 1.png"))

        self.left_lbl = tk.Label(self.left_frm, image=self.img_pf, height=425, width=336)
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

        self.bttn_login = tk.Button(self.right_lbl, font=('Inter', 24, 'bold'), fg='#FFFFFF', text="ENTRAR", bg='#6A6666')
        self.bttn_login.pack(side=tk.BOTTOM, pady=20, padx=100)

        self.bttn_help = tk.Button(self.right_lbl, font=('Inter', 20, 'bold'), fg='#6A6666', text=" Problemas de Login? ", bg='#94939B', borderwidth=0)
        self.bttn_help.pack(fill=tk.BOTH)
        self.bttn_help.config()






janela = tk.Tk()
Screens(janela)
janela.mainloop()