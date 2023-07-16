import tkinter as tk
from tkinter import ttk, messagebox
import bd_sistemas_de_escala as bd

class Usuario:
    def __init__(self, master):
        self.janelaprincipal = master
        self.janelaprincipal.title("Usuários")
        self.janelaprincipal.geometry("600x620")

        self.frm = tk.Frame(self.janelaprincipal, width=600, height=620)
        self.frm.grid(column=0, row=0, pady=25)

        self.lbl_botao = tk.Label(self.frm, text="Botão", font=("Arial", 14), bg="#3CB371",
                                              fg="white", width=20, height=1)
        self.lbl_botao.place(x=10, y=10)
        self.lbl_botao.bind("<Button-1>", self.nome_funcao)

    def nome_funcao(self, event):
        self.janela_botao = tk.Toplevel()
        self.janela_botao.title("Nova Janela")
        self.janela_botao.grab_set()
        self.janela_botao.geometry("600x400")

app = tk.Tk()
Usuario(app)
app.mainloop()