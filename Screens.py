import tkinter as tk
from tkinter import ttk
##from tkcalendar import Calendar, DateEntry
##import holidays

class Screens:
    def __init__(self, master):
        self.login_screen = master
        self.login_screen.title("Login")
        self.login_screen.geometry('961x573')
        self.login_screen.configure(bg='#D9D9D9')

        self.top_frm = tk.Frame(self.login_screen, height=100, width=100)
        self.top_frm.pack(fill=tk.X,padx=20, pady=20)

        self.top_lbl = tk.Label(self.top_frm, text = "BEM VINDO", font=('Inter',32,'bold'), fg='#0B0B0B')
        self.top_lbl.pack(side=tk.LEFT, pady=10, padx=50,)

janela = tk.Tk()
Screens(janela)
janela.mainloop()