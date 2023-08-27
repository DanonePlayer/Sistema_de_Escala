import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import holidays
import bd_sistemas_de_escala as bd
from datetime import datetime
from calendar import monthrange


class Tela:
    def __init__(self, master):
        self.janelaprincipal = master
        self.janelaprincipal.title("Controle de Escalas")
        self.janelaprincipal.geometry("400x200")
        # self.janelaprincipal["bg"] = "gray"

        self.frm_cima = tk.Frame(self.janelaprincipal, width=400, height=400)
        self.frm_cima.grid(column=0, row=0, pady=25)

        self.lbl_escalas = tk.Label(self.frm_cima, text="Tipo de Escala", font=("Arial", 14), bg="#3CB371", fg="white",
                                    width=20, height=1)
        self.lbl_escalas.place(x=10, y=10)
        self.lbl_escalas.bind("<Button-1>", self.Cria_tipo_escalas)

        self.imgicon = tk.PhotoImage(file="Images/a.png", height=222)
        self.janelaprincipal.iconphoto(False, self.imgicon)

        self.lbl_verifica_escala = tk.Label(self.frm_cima, text="Verificar Escalas", font=("Arial", 14), bg="#3CB371",
                                            fg="white", width=20, height=1)

        self.Tipo_escala = []

    def Cria_tipo_escalas(self, event):
        self.janela_escala = tk.Toplevel()
        self.janela_escala.title("Tipo de Escala")
        self.janela_escala.grab_set()
        self.janela_escala.geometry("800x400")
        self.frm = tk.Frame(self.janela_escala, width=800, height=620)
        self.frm.grid(column=0, row=0, pady=25)

        self.frame_tvw_usuario = tk.Frame(self.frm)
        self.frame_tvw_usuario.place(x=10, y=10)
        self.tvw_tipo_escala = ttk.Treeview(self.frame_tvw_usuario,
                                       columns=('id', 'nome tipo de escala', 'finais de semana', 'feriados', 'escala mutua'),
                                       show='headings')
        self.tvw_tipo_escala.column('id', width=40)
        self.tvw_tipo_escala.column('nome tipo de escala', width=250)
        self.tvw_tipo_escala.column('finais de semana', width=125)
        self.tvw_tipo_escala.column('feriados', width=125)
        self.tvw_tipo_escala.column('escala mutua', width=125)
        self.tvw_tipo_escala.heading('id', text='Id')
        self.tvw_tipo_escala.heading('nome tipo de escala', text='Nome da Escala')
        self.tvw_tipo_escala.heading('finais de semana', text='Finais de Semana')
        self.tvw_tipo_escala.heading('feriados', text='Feriados')
        self.tvw_tipo_escala.heading('escala mutua', text='Escala Mútua')
        self.tvw_tipo_escala.pack(side=tk.LEFT)
        self.atualizar_tvw_tipo_escala()

        self.scr_escala = ttk.Scrollbar(self.frame_tvw_usuario, command=self.tvw_tipo_escala.yview)
        self.scr_escala.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw_tipo_escala.configure(yscroll=self.scr_escala.set)

        self.lbl_cadastrar_usuario = tk.Label(self.frm, text="Criar Escala", font=("Arial", 14), bg="#3CB371",
                                              fg="white", width=17, height=1)
        self.lbl_cadastrar_usuario.place(x=10, y=250)
        self.lbl_cadastrar_usuario.bind("<Button-1>", self.criar_tipo_escala)

        self.lbl_editar_usuario = tk.Label(self.frm, text="Editar Usuário", font=("Arial", 14), bg="Orange",
                                           fg="white", width=17, height=1)
        self.lbl_editar_usuario.place(x=220, y=250)
        self.lbl_editar_usuario.bind("<Button-1>", self.editar_tipo_escala)

        self.lbl_excluir_usuario = tk.Label(self.frm, text="Excluir Usuário", font=("Arial", 14), bg="Red",
                                            fg="white", width=17, height=1)
        self.lbl_excluir_usuario.place(x=440, y=250)
        self.lbl_excluir_usuario.bind("<Button-1>", self.excluir_tipo_escala)

    def atualizar_tvw_tipo_escala(self):
        for i in self.tvw_tipo_escala.get_children():
            self.tvw_tipo_escala.delete(i)
        query = "SELECT tipo_escala_id, nome_tipo_escala, CASE WHEN finais_semana = 0 THEN 'Não' WHEN finais_semana = 1 THEN 'Sim' END AS finais_semana, CASE WHEN feriados = 0 THEN 'Não' WHEN feriados = 1 THEN 'Sim' END AS feriados, CASE WHEN escala_mutua = 0 THEN 'Não' WHEN escala_mutua = 1 THEN 'Sim' END AS escala_mutua FROM tipo_escala;"
        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw_tipo_escala.insert('', tk.END, values=tupla)

    def criar_tipo_escala(self, event):
        self.janela_criar_escala = tk.Toplevel()
        self.janela_criar_escala.title("Criar Tipo de Escala")
        self.janela_criar_escala.grab_set()
        self.janela_criar_escala.geometry("600x400")

        self.lbl_nome_escala = tk.Label(self.janela_criar_escala, text="Nome do tipo de Escala:")
        self.lbl_nome_escala.place(x=10, y=10)
        self.entry_nome_escala = tk.Entry(self.janela_criar_escala, borderwidth=2)
        self.entry_nome_escala.place(x=10, y=30)

        self.int_var_finais_semana = tk.IntVar()
        self.int_var_feriados = tk.IntVar()
        self.int_var_escala_mutua = tk.IntVar()

        self.lbl_cont_final_semana = tk.Label(self.janela_criar_escala, text="Contará os finais de semana?")
        self.lbl_cont_final_semana.place(x=10, y=60)

        self.rbtn_cont_final_semanas = tk.Radiobutton(self.janela_criar_escala, text="Sim", variable=self.int_var_finais_semana,
                                                      value=1)
        self.rbtn_cont_final_semanas.place(x=10, y=80)

        self.rbtn_cont_final_semanan = tk.Radiobutton(self.janela_criar_escala, text="Não", variable=self.int_var_finais_semana,
                                                      value=0)
        self.rbtn_cont_final_semanan.place(x=90, y=80)

        self.lbl_cont_ferias = tk.Label(self.janela_criar_escala, text="Contará os feriados?")
        self.lbl_cont_ferias.place(x=10, y=100)

        self.rbtn_cont_feriass = tk.Radiobutton(self.janela_criar_escala, text="Sim", variable=self.int_var_feriados,
                                                value=1)
        self.rbtn_cont_feriass.place(x=10, y=120)

        self.rbtn_cont_feriasn = tk.Radiobutton(self.janela_criar_escala, text="Não", variable=self.int_var_feriados,
                                                value=0)
        self.rbtn_cont_feriasn.place(x=90, y=120)

        self.lbl_cont_escala_mutua = tk.Label(self.janela_criar_escala, text="A Escala será mútua?")
        self.lbl_cont_escala_mutua.place(x=10, y=140)

        self.rbtn_cont_escala_mutuas = tk.Radiobutton(self.janela_criar_escala, text="Sim", variable=self.int_var_escala_mutua,
                                                value=1)
        self.rbtn_cont_escala_mutuas.place(x=10, y=160)

        self.rbtn_cont_escala_mutuan = tk.Radiobutton(self.janela_criar_escala, text="Não", variable=self.int_var_escala_mutua,
                                                value=0)
        self.rbtn_cont_escala_mutuan.place(x=90, y=160)

        self.btn_ok = tk.Button(self.janela_criar_escala, text='Criar', width=15, command=self.button_criar_tipo_escala)
        self.btn_ok.place(x=10, y=190)

    def button_criar_tipo_escala(self):
        nome_escala = self.entry_nome_escala.get()
        finais_semana = self.int_var_finais_semana.get()
        feriados = self.int_var_feriados.get()
        escala_mutua = self.int_var_escala_mutua.get()

        if nome_escala == "":
            messagebox.showinfo("Insira um nome completo", "O campo nome da escala está incorreto!")
            self.edit_escala.deiconify()
        elif escala_mutua == "":
            messagebox.showinfo("Selecione um tipo", "Nenhuma seleção no escala mútua!")
            self.edit_escala.deiconify()
        elif finais_semana == "":
            messagebox.showinfo("Selecione um tipo", "Nenhuma seleção no finais de semana!")
            self.edit_escala.deiconify()
        elif feriados == "":
            messagebox.showinfo("Selecione um tipo", "Nenhuma seleção no feriados!")
            self.edit_escala.deiconify()
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
                self.atualizar_tvw_tipo_escala()
                messagebox.showinfo("SUCESSO!", "Escala criada com sucesso!")
                self.janela_criar_escala.destroy()
                self.janela_escala.deiconify()
            else:
                messagebox.showinfo("Nome do tipo de escala já cadastrado", "O Nome do tipo de escala já está cadastrado")
                self.janela_criar_escala.deiconify()

    def editar_tipo_escala(self, event):
        selecionado = self.tvw_tipo_escala.selection()
        lista = self.tvw_tipo_escala.item(selecionado, "values")
        # query = f"SELECT * FROM escala WHERE escala_id = {lista[0]};"
        # lista = bd.consultar_usuarios(query)
        if selecionado != ():
            self.edit_escala = tk.Toplevel()
            self.edit_escala.title("Editar Tipo de Escala")
            self.edit_escala.grab_set()
            self.edit_escala.geometry("600x400")

            self.lbl_nome_escala = tk.Label(self.edit_escala, text="Nome do Tipo de Escala:")
            self.lbl_nome_escala.place(x=10, y=10)
            self.entry_nome_escala = tk.Entry(self.edit_escala, borderwidth=2)
            self.entry_nome_escala.place(x=10, y=30)
            self.entry_nome_escala.insert(0, lista[1])

            self.int_var_finais_semana = tk.IntVar()
            self.int_var_feriados = tk.IntVar()
            self.int_var_escala_mutua = tk.IntVar()

            self.lbl_cont_final_semana = tk.Label(self.edit_escala, text="Contará os finais de semana?")
            self.lbl_cont_final_semana.place(x=10, y=70)

            self.rbtn_cont_final_semanas = tk.Radiobutton(self.edit_escala, text="Sim",
                                                          variable=self.int_var_finais_semana, value=1)
            self.rbtn_cont_final_semanas.place(x=10, y=90)

            self.rbtn_cont_final_semanan = tk.Radiobutton(self.edit_escala, text="Não",
                                                          variable=self.int_var_finais_semana, value=0)
            self.rbtn_cont_final_semanan.place(x=90, y=90)

            if lista[2] == "1":
                self.int_var_finais_semana.set(1)
            else:
                self.int_var_finais_semana.set(0)

            self.lbl_cont_ferias = tk.Label(self.edit_escala, text="Contará os feriados?")
            self.lbl_cont_ferias.place(x=10, y=130)

            self.rbtn_cont_feriass = tk.Radiobutton(self.edit_escala, text="Sim", variable=self.int_var_feriados,
                                                    value=1)
            self.rbtn_cont_feriass.place(x=10, y=150)

            self.rbtn_cont_feriasn = tk.Radiobutton(self.edit_escala, text="Não", variable=self.int_var_feriados,
                                                    value=0)
            self.rbtn_cont_feriasn.place(x=90, y=150)

            if lista[3] == "1":
                self.int_var_feriados.set(1)
            else:
                self.int_var_feriados.set(0)

            self.lbl_cont_escala_mutua = tk.Label(self.edit_escala, text="Escala será mútua?")
            self.lbl_cont_escala_mutua.place(x=10, y=190)

            self.rbtn_cont_escala_mutuas = tk.Radiobutton(self.edit_escala, text="Sim", variable=self.int_var_escala_mutua,
                                                    value=1)
            self.rbtn_cont_escala_mutuas.place(x=10, y=210)

            self.rbtn_cont_escala_mutuan = tk.Radiobutton(self.edit_escala, text="Não", variable=self.int_var_escala_mutua,
                                                    value=0)
            self.rbtn_cont_escala_mutuan.place(x=90, y=210)

            if lista[4] == "1":
                self.int_var_escala_mutua.set(1)
            else:
                self.int_var_escala_mutua.set(0)

            self.btn_ok = tk.Button(self.edit_escala, text='Editar', command=self.button_editar_escala)
            self.btn_ok.place(x=100, y=250)

            self.btn_not_ok = tk.Button(self.edit_escala, text='Cancelar', command=self.edit_escala.destroy)
            self.btn_not_ok.place(x=200, y=250)

    def button_editar_escala(self):
        selecionado = self.tvw_tipo_escala.selection()
        lista = self.tvw_tipo_escala.item(selecionado, "values")

        nome_tipo_escala = self.entry_nome_escala.get()
        finais_semana = self.int_var_finais_semana.get()
        feriados = self.int_var_feriados.get()
        escala_mutua = self.int_var_escala_mutua.get()

        if nome_tipo_escala == "":
            messagebox.showinfo("Insira um nome completo", "O campo nome da escala está incorreto!")
            self.edit_escala.deiconify()
        elif escala_mutua == "":
            messagebox.showinfo("Insira os dias", "Nenhuma seleção em escala mútua!")
            self.edit_escala.deiconify()
        elif finais_semana == "":
            messagebox.showinfo("Selecione um tipo", "Nenhuma seleção no finais de semana!")
            self.edit_escala.deiconify()
        elif feriados == "":
            messagebox.showinfo("Selecione um tipo", "Nenhuma seleção no feriados!")
            self.edit_escala.deiconify()
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
                self.atualizar_tvw_tipo_escala()
                self.edit_escala.destroy()
            else:
                messagebox.showinfo("Nome do tipo de escala já cadastrado", "O Nome do tipo de escala já está cadastrado")
                self.edit_escala.deiconify()

    def excluir_tipo_escala(self, event):
        selecionado = self.tvw_tipo_escala.selection()
        lista = self.tvw_tipo_escala.item(selecionado, "values")
        mensagem = messagebox.askyesno(f'Excluir', f'Você tem certeza que deseja excluir o tipo de escala: {lista[1]}?')
        if mensagem:
            sql = f'DELETE FROM tipo_escala WHERE tipo_escala_id={lista[0]};'
            bd.deletar(sql)
            messagebox.showinfo("Excluído", "Tipo de escala excluída com sucesso")
            self.atualizar_tvw_tipo_escala()
        self.janelaprincipal.deiconify()

janela = tk.Tk()
Tela(janela)
janela.mainloop()
