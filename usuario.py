import tkinter as tk
from tkinter import ttk, messagebox
import bd_sistemas_de_escala as bd
import bcrypt
import os


class Usuario:
    def __init__(self, master):
        self.janelaprincipal = master
        self.janelaprincipal.title("Usuários")
        self.janelaprincipal.geometry("600x620")

        self.frm = tk.Frame(self.janelaprincipal, width=600, height=620)
        self.frm.grid(column=0, row=0, pady=25)

        self.frame_tvw_usuario = tk.Frame(self.frm)
        self.frame_tvw_usuario.place(x=10, y=10)
        self.tvw_usuario = ttk.Treeview(self.frame_tvw_usuario, columns=('id', 'nome', 'nome de usuario'), show='headings')
        self.tvw_usuario.column('id', width=40)
        self.tvw_usuario.column('nome', width=250)
        self.tvw_usuario.column('nome de usuario', width=250)
        self.tvw_usuario.heading('id', text='Id')
        self.tvw_usuario.heading('nome', text='Nome')
        self.tvw_usuario.heading('nome de usuario', text='Nome de Usuário')
        self.tvw_usuario.pack(side=tk.LEFT)
        self.atualizar_tvw_usuario()

        self.scr_usuario = ttk.Scrollbar(self.frame_tvw_usuario, command=self.tvw_usuario.yview)
        self.scr_usuario.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw_usuario.configure(yscroll=self.scr_usuario.set)

        self.lbl_cadastrar_usuario = tk.Label(self.frm, text="Criar Usuário", font=("Arial", 14), bg="#3CB371",
                                         fg="white", width=20, height=1)
        self.lbl_cadastrar_usuario.place(x=10, y=250)
        self.lbl_cadastrar_usuario.bind("<Button-1>", self.cadastrar_usuario)

        self.lbl_editar_usuario = tk.Label(self.frm, text="Editar Usuário", font=("Arial", 14), bg="Orange",
                                              fg="white", width=20, height=1)
        self.lbl_editar_usuario.place(x=10, y=300)
        self.lbl_editar_usuario.bind("<Button-1>", self.editar_usuario)

    def atualizar_tvw_usuario(self):
        for i in self.tvw_usuario.get_children():
            self.tvw_usuario.delete(i)
        query = 'SELECT usuario_id, nome_completo, nome_usuario FROM usuario;'
        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw_usuario.insert('', tk.END, values=tupla)

    def cadastrar_usuario(self, event):
        self.janela_cadastrar_usuario = tk.Toplevel()
        self.janela_cadastrar_usuario.title("Cadastrar Usuário")
        self.janela_cadastrar_usuario.grab_set()
        self.janela_cadastrar_usuario.geometry("600x400")

        self.lbl_nome_completo = tk.Label(self.janela_cadastrar_usuario, text="Nome completo:")
        self.lbl_nome_completo.place(x=10, y=10)

        self.entry_nome_completo = tk.Entry(self.janela_cadastrar_usuario, borderwidth=2)
        self.entry_nome_completo.place(x=10, y=30)

        self.lbl_nome_usuario = tk.Label(self.janela_cadastrar_usuario, text="Nome usuario:")
        self.lbl_nome_usuario.place(x=10, y=50)

        self.entry_nome_usuario = tk.Entry(self.janela_cadastrar_usuario, borderwidth=2)
        self.entry_nome_usuario.place(x=10, y=70)

        self.lbl_senha = tk.Label(self.janela_cadastrar_usuario, text="Senha:")
        self.lbl_senha.place(x=10, y=90)

        self.entry_senha = tk.Entry(self.janela_cadastrar_usuario, borderwidth=2, show="*")
        self.entry_senha.place(x=10, y=110)

        self.lbl_confirmar_senha = tk.Label(self.janela_cadastrar_usuario, text="Confirmar senha:")
        self.lbl_confirmar_senha.place(x=10, y=130)

        self.entry_confirmar_senha = tk.Entry(self.janela_cadastrar_usuario, borderwidth=2, show="*")
        self.entry_confirmar_senha.place(x=10, y=150)

        self.lbl_tipo_usuario = tk.Label(self.janela_cadastrar_usuario, text="Tipo:")
        self.lbl_tipo_usuario.place(x=10, y=170)

        self.cbx_tipo_usuario = ttk.Combobox(self.janela_cadastrar_usuario, width=17)
        self.cbx_tipo_usuario['values'] = ('Usuário', 'Super Usuário')
        self.cbx_tipo_usuario.place(x=10, y=190)

        self.btn_con_cadastro = tk.Button(self.janela_cadastrar_usuario, text="Confirmar", command=self.confirmar_cadastrar_usuario)
        self.btn_con_cadastro.place(x=10, y=220)

        self.btn_canc_cadastro = tk.Button(self.janela_cadastrar_usuario, text="Cancelar")
        self.btn_canc_cadastro.place(x=80, y=220)


    def confirmar_cadastrar_usuario(self):
        nome_completo = self.entry_nome_completo.get()
        nome_usuario = self.entry_nome_usuario.get()
        senha = self.entry_senha.get().encode('utf-8')
        conf_senha = self.entry_confirmar_senha.get().encode('utf-8')
        tipo = self.cbx_tipo_usuario.get()

        # Criptografando a senha
        salt = bcrypt.gensalt(8)
        senha = bcrypt.hashpw(senha, salt)
        conf_senha = bcrypt.hashpw(conf_senha, salt)

        if nome_completo == "":
            messagebox.showinfo("Insira um nome completo", "O campo nome completo está incorreto!")
            self.janela_cadastrar_usuario.deiconify()
        elif nome_usuario == "":
            messagebox.showinfo("Insira o nome de usuario", "O campo nome de usuário está incorreto!")
            self.janela_cadastrar_usuario.deiconify()
        elif senha == "":
            messagebox.showinfo("Insira uma senha", "O campo senha está vazio!")
            self.janela_cadastrar_usuario.deiconify()
        elif conf_senha == "":
            messagebox.showinfo("Confirme a senha", "O campo de confirmação da senha está vazio!")
            self.janela_cadastrar_usuario.deiconify()
        elif senha != conf_senha:
            messagebox.showinfo("Senhas divergentes", "As senhas não correspondem")
            self.janela_cadastrar_usuario.deiconify()
        elif tipo == "":
            messagebox.showinfo("Selecione um tipo", "Nenhum Tipo foi selecionado!")
            self.janela_cadastrar_usuario.deiconify()
        else:
            query = 'SELECT nome_usuario FROM usuario;'
            valores = bd.consultar(query)
            confirmar = False
            for i in valores:
                if nome_usuario == i[0]:
                    confirmar = True
                    break
            if not confirmar:
                if tipo == "Usuário":
                    tipo = 0
                else:
                    tipo = 1
                query = f'INSERT INTO usuario ("nome_completo", "nome_usuario", "senha", "super_usuario") VALUES ("{nome_completo}", "{nome_usuario}", "{senha}", {tipo});'
                bd.inserir(query)
                messagebox.showinfo("SUCESSO!", "Usuário criado com sucesso!")
                self.janela_cadastrar_usuario.destroy()
            else:
                messagebox.showinfo("Nome de usuário já cadastrado", "O Nome de usuário já cadastrado")
                self.janela_cadastrar_usuario.deiconify()

    def editar_usuario(self, event):
        selecionado = self.tvw_usuario.selection()
        lista = self.tvw_usuario.item(selecionado, "values")
        if selecionado != ():
            self.edit_usuario = tk.Toplevel()
            self.edit_usuario.title("Editar candidato")
            self.edit_usuario.geometry("600x400")
            self.edit_usuario.resizable(False, False)

            self.nome = tk.Label(self.edit_usuario, text="Editar candidato", font=32)
            self.nome.pack()

            self.frm_edit = tk.Frame(self.edit_usuario)
            self.frm_edit.pack()

            self.lbl_nome_completo = tk.Label(self.frm_edit, text="Nome:")
            self.lbl_nome_completo.grid(column=0, row=0, pady=10)
            self.ent_nome_completo = tk.Entry(self.frm_edit, width=30)
            self.ent_nome_completo.grid(column=1, row=0)
            self.ent_nome_completo.insert(0, lista[1])

            self.lbl_nome_usuario = tk.Label(self.frm_edit, text="Nome de usuário:")
            self.lbl_nome_usuario.grid(column=0, row=1, pady=10)
            self.ent_nome_usuario = tk.Entry(self.frm_edit, width=30)
            self.ent_nome_usuario.grid(column=1, row=1 )
            self.ent_nome_usuario.insert(0, lista[2])

            self.lbl_nome_usuario = tk.Label(self.frm_edit, text="Nome de usuário:")
            self.lbl_nome_usuario.grid(column=0, row=1, pady=10)
            self.ent_nome_usuario = tk.Entry(self.frm_edit, width=30)
            self.ent_nome_usuario.grid(column=1, row=1)
            self.ent_nome_usuario.insert(0, lista[2])

            # CBX COMBOBOX

            self.btn_conf_edit = tk.Button(self.frm_edit, text="Confirmar", command=self.confirmar_editar_usuario)
            self.btn_conf_edit.grid(column=0, row=2, columnspan=2, pady=10)

app = tk.Tk()
Usuario(app)
app.mainloop()
