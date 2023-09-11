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

        self.imgicon = tk.PhotoImage(file="images/a.png", height=222)
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

    def update_tvw_type_manage(self):
        for i in self.tvw_tipo_escala.get_children():
            self.tvw_tipo_escala.delete(i)
        query = "SELECT tipo_escala_id, nome_tipo_escala, CASE WHEN finais_semana = 0 THEN 'Não' WHEN finais_semana = 1 THEN 'Sim' END AS finais_semana, CASE WHEN feriados = 0 THEN 'Não' WHEN feriados = 1 THEN 'Sim' END AS feriados, CASE WHEN escala_mutua = 0 THEN 'Não' WHEN escala_mutua = 1 THEN 'Sim' END AS escala_mutua FROM tipo_escala;"
        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw_tipo_escala.insert('', tk.END, values=tupla)

    def atualizar_tvw_tipo_escala(self):
        for i in self.tvw_tipo_escala.get_children():
            self.tvw_tipo_escala.delete(i)
        query = "SELECT tipo_escala_id, nome_tipo_escala, CASE WHEN finais_semana = 0 THEN 'Não' WHEN finais_semana = 1 THEN 'Sim' END AS finais_semana, CASE WHEN feriados = 0 THEN 'Não' WHEN feriados = 1 THEN 'Sim' END AS feriados, CASE WHEN escala_mutua = 0 THEN 'Não' WHEN escala_mutua = 1 THEN 'Sim' END AS escala_mutua FROM tipo_escala;"
        dados = bd.consultar(query)
        for tupla in dados:
            self.tvw_tipo_escala.insert('', tk.END, values=tupla)

    def type_close(self):
        self.create_screen.destroy()
        self.janela_escala.deiconify()

    def criar_tipo_escala(self, event):
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

        self.lbl_nome_escala = tk.Label(self.center_frame, text="NOME DO TIPO DE ESCALA:",font=('Inter', 10, 'bold'),fg='#FFF',bg='#94939B')
        self.lbl_nome_escala.pack(side=tk.TOP,pady=5,padx=10)

        self.entry_nome_escala = tk.Entry(self.center_frame,  width=59)
        self.entry_nome_escala.pack(side=tk.TOP, padx=5, pady=10)

        self.frame_escolhas = tk.Frame(self.center_frame, bg='#94939B')
        self.frame_escolhas.pack(fill=tk.Y, expand=True, padx=10, pady=10, side=tk.TOP)

        self.int_var_finais_semana = tk.IntVar()
        self.int_var_feriados = tk.IntVar()
        self.int_var_escala_mutua = tk.IntVar()

        style = ttk.Style()
        style.configure("Custom.TRadiobutton", background="#94939B", foreground="white", font=("Inter", 10, "bold"))

        self.lbl_cont_final_semana = tk.Label(self.frame_escolhas, text="CONTAR FINAIS DE SEMANA?", font=('Inter', 10), fg='#FFF', bg='#94939B')
        self.lbl_cont_final_semana.grid(row=0, column=0, columnspan=3, sticky='n', pady=10)

        self.rbtn_cont_final_semanas = ttk.Radiobutton(self.frame_escolhas, text="Sim", variable=self.int_var_finais_semana,
                                                      value=1, style="Custom.TRadiobutton")
        self.rbtn_cont_final_semanas.grid(row=2, column=0, padx=10, pady=10, sticky='n')

        self.rbtn_cont_final_semanan = ttk.Radiobutton(self.frame_escolhas, text="Não", variable=self.int_var_finais_semana,
                                                      value=0, style="Custom.TRadiobutton")
        self.rbtn_cont_final_semanan.grid(row=2, column=1, padx=10, pady=10, sticky='n')

        self.lbl_cont_ferias = tk.Label(self.frame_escolhas, text="CONTAR FERIADOS?", font=('Inter', 10, 'bold'), fg='#FFF',bg='#94939B')
        self.lbl_cont_ferias.grid(row=3, column=0, columnspan=2, sticky='nsew', pady=20)

        self.rbtn_cont_feriass = ttk.Radiobutton(self.frame_escolhas, text="Sim", variable=self.int_var_feriados,
                                                value=1, style="Custom.TRadiobutton")
        self.rbtn_cont_feriass.grid(row=4, column=0, padx=10, pady=10, sticky='n')

        self.rbtn_cont_feriasn = ttk.Radiobutton(self.frame_escolhas, text="Não", variable=self.int_var_feriados,
                                                value=0, style="Custom.TRadiobutton")
        self.rbtn_cont_feriasn.grid(row=4, column=1, padx=10, pady=10, sticky='n')

        self.lbl_cont_escala_mutua = tk.Label(self.frame_escolhas, text="ESCALA MUTUA?",
                                              font=('Inter', 10, 'bold'), fg='#FFF',bg='#94939B')
        self.lbl_cont_escala_mutua.grid(row=5, column=0, columnspan=2, sticky='nsew', pady=20)

        self.rbtn_cont_escala_mutuas = ttk.Radiobutton(self.frame_escolhas, text="Sim", variable=self.int_var_escala_mutua,
                                                value=1, style="Custom.TRadiobutton")
        self.rbtn_cont_escala_mutuas.grid(row=6, column=0, padx=10, pady=10, sticky='n')

        self.rbtn_cont_escala_mutuan = ttk.Radiobutton(self.frame_escolhas, text="Não", variable=self.int_var_escala_mutua,
                                                value=0, style="Custom.TRadiobutton")
        self.rbtn_cont_escala_mutuan.grid(row=6, column=1, padx=10, pady=10, sticky='n')

        self.frame_button = tk.Frame(self.center_frame, bg='#94939B')
        self.frame_button.pack(fill=tk.Y, padx=10, pady=10, side=tk.TOP)

        self.bttn_criar = tk.Button(self.frame_button, text='CRIAR', font=('Inter', 10, 'bold'), fg='#FFF',
                                       bg='#3CB371', command=self.button_criar_tipo_escala, borderwidth=0, width=10)
        self.bttn_criar.pack(side=tk.LEFT, pady=5, padx=10)

        self.bttn_clean = tk.Button(self.frame_button, text='LIMPAR', font=('Inter', 10, 'bold'), fg='#605F5F',
                                    bg='#FFFFFF', command='', borderwidth=0, width=10)
        self.bttn_clean.pack(side=tk.LEFT, pady=5, padx=10)

        self.bttn_voltar = tk.Button(self.frame_button, text='VOLTAR', font=("Arial", 10, "bold"), bg="#E1523F",
                                        fg="white", borderwidth=0, command=self.type_close, width=10)
        self.bttn_voltar.pack(side=tk.LEFT, pady=5, padx=10)

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
                self.create_screen.destroy()
                self.janela_escala.deiconify()
            else:
                messagebox.showinfo("Nome do tipo de escala já cadastrado", "O Nome do tipo de escala já está cadastrado")
                self.create_screen.deiconify()

    def type_edit_close(self):
        self.edite_type.destroy()
        self.janela_escala.deiconify()

    def editar_tipo_escala(self, event):
        selecionado = self.tvw_tipo_escala.selection()
        tupla = self.tvw_tipo_escala.item(selecionado, "values")

        if selecionado != ():
            self.edite_type = tk.Toplevel()
            self.edite_type.title("Criar Tipo de Escala")
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

            self.lbl_create = tk.Label(self.center_frame, text='CRIAR TIPO DE ESCALA', font=('Inter', 20, 'bold'),
                                       fg='#0B0B0B', bg='#94939B')
            self.lbl_create.pack(side=tk.TOP, padx=5, pady=10)

            self.lbl_nome_escala = tk.Label(self.center_frame, text="NOME DO TIPO DE ESCALA:",
                                            font=('Inter', 10, 'bold'), fg='#FFF', bg='#94939B')
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

            self.bttn_criar = tk.Button(self.frame_button, text='CRIAR', font=('Inter', 10, 'bold'), fg='#FFF',
                                        bg='#3CB371', command=self.button_criar_tipo_escala, borderwidth=0, width=10)
            self.bttn_criar.pack(side=tk.LEFT, pady=5, padx=10)

            self.bttn_clean = tk.Button(self.frame_button, text='LIMPAR', font=('Inter', 10, 'bold'), fg='#605F5F',
                                        bg='#FFFFFF', command='', borderwidth=0, width=10)
            self.bttn_clean.pack(side=tk.LEFT, pady=5, padx=10)

            self.bttn_voltar = tk.Button(self.frame_button, text='VOLTAR', font=("Arial", 10, "bold"), bg="#E1523F",
                                         fg="white", borderwidth=0, command=self.type_close, width=10)
            self.bttn_voltar.pack(side=tk.LEFT, pady=5, padx=10)

            # self.int_var_finais_semana_edit = tk.IntVar()
            # self.int_var_feriados_edit = tk.IntVar()
            # self.int_var_escala_mutua_edit = tk.IntVar()
            #
            # #style = ttk.Style()
            # #style.configure("Custom.TRadiobutton", background="Pink", foreground="white", font=("Inter", 10, "bold"))
            #
            # self.lbl_cont_final_semana = tk.Label(self.edit_escala, text="Contará os finais de semana?")
            # self.lbl_cont_final_semana.place(x=10, y=70)
            #
            # self.rbtn_cont_final_semanas = tk.Radiobutton(self.edit_escala, text="Sim", variable=self.int_var_finais_semana, value=1,background="Pink", foreground="white", font=("Inter", 10, "bold"))
            # self.rbtn_cont_final_semanas.place(x=10, y=90)
            #
            # self.rbtn_cont_final_semanan = tk.Radiobutton(self.edit_escala, text="Não",
            #                                               variable=self.int_var_finais_semana, value=0,background="Pink", foreground="white", font=("Inter", 10, "bold"))
            # self.rbtn_cont_final_semanan.place(x=90, y=90)
            #
            # if lista[2] == "1":
            #     self.int_var_finais_semana.set(1)
            # else:
            #     self.int_var_finais_semana.set(0)
            #
            # self.lbl_cont_ferias = tk.Label(self.edit_escala, text="Contará os feriados?")
            # self.lbl_cont_ferias.place(x=10, y=130)
            #
            # self.rbtn_cont_feriass = tk.Radiobutton(self.edit_escala, text="Sim", variable=self.int_var_feriados,
            #                                         value=1)
            # self.rbtn_cont_feriass.place(x=10, y=150)
            #
            # self.rbtn_cont_feriasn = tk.Radiobutton(self.edit_escala, text="Não", variable=self.int_var_feriados,
            #                                         value=0)
            # self.rbtn_cont_feriasn.place(x=90, y=150)
            #
            # if lista[3] == "1":
            #     self.int_var_feriados.set(1)
            # else:
            #     self.int_var_feriados.set(0)
            #
            # self.lbl_cont_escala_mutua = tk.Label(self.edit_escala, text="Escala será mútua?")
            # self.lbl_cont_escala_mutua.place(x=10, y=190)
            #
            # self.rbtn_cont_escala_mutuas = tk.Radiobutton(self.edit_escala, text="Sim", variable=self.int_var_escala_mutua,
            #                                         value=1)
            # self.rbtn_cont_escala_mutuas.place(x=10, y=210)
            #
            # self.rbtn_cont_escala_mutuan = tk.Radiobutton(self.edit_escala, text="Não", variable=self.int_var_escala_mutua,
            #                                         value=0)
            # self.rbtn_cont_escala_mutuan.place(x=90, y=210)
            #
            # if lista[4] == "1":
            #     self.int_var_escala_mutua.set(1)
            # else:
            #     self.int_var_escala_mutua.set(0)
            #
            # self.btn_ok = tk.Button(self.edit_escala, text='Editar', command=self.button_editar_escala)
            # self.btn_ok.place(x=100, y=250)
            #
            # self.btn_not_ok = tk.Button(self.edit_escala, text='Cancelar', command=self.edit_escala.destroy)
            # self.btn_not_ok.place(x=200, y=250)

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
