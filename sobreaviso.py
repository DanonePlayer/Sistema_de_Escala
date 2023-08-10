import tkinter as tk
from calendar import monthrange
from datetime import datetime
from tkinter import messagebox, ttk

import holidays
from tkcalendar import Calendar, DateEntry

import bd_sistemas_de_escala as bd


class Tela:
    def __init__(self, master):
        self.janelaprincipal = master
        self.janelaprincipal.title("Sobreaviso")
        self.janelaprincipal.geometry("400x200")

        self.frm_cima = tk.Frame(self.janelaprincipal, width=400, height=400)
        self.frm_cima.grid(column=0, row=0, pady=25)

        self.lbl_escalas = tk.Label(self.frm_cima, text="Sobreaviso", font=("Arial", 14), bg="#3CB371", fg="white",
                                    width=20, height=1)
        self.lbl_escalas.place(x=10, y=10)
        self.lbl_escalas.bind("<Button-1>", self.sobreaviso)

    def sobreaviso(self, event):
        self.janela_sobreaviso = tk.Toplevel()
        self.janela_sobreaviso.title("Sobreaviso")
        self.janela_sobreaviso.grab_set()
        self.janela_sobreaviso.geometry("1000x400")
        self.janela_sobreaviso