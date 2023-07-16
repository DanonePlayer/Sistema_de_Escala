import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import holidays




class Tela:
    def __init__(self, master):
        self.janelaprincipal = master
        self.janelaprincipal.title("Controle de Escalas")
        self.janelaprincipal.geometry("400x200")
        # self.janelaprincipal["bg"] = "gray"


        self.frm_cima = tk.Frame(self.janelaprincipal, width=400, height=400)
        self.frm_cima.grid(column=0, row=0, pady=25)



        self.lbl_criar_escala = tk.Label(self.frm_cima, text="Criar Escala", font=("Arial",14), bg="#3CB371", fg="white", width=20, height=1)
        self.lbl_criar_escala.place(x=10, y=10)
        self.lbl_criar_escala.bind("<Button-1>", self.criar_escala) 


        self.lbl_novaprog = tk.Label(self.frm_cima, text="+ Nova programação", font=("Arial",14), bg="#3CB371", fg="white", width=20, height=1)
        self.lbl_novaprog.place(x=10, y=50)
        self.lbl_novaprog.bind("<Button-1>", self.Nova_programacao)

        self.imgicon = tk.PhotoImage(file="../Images/a.png", height=222)
        self.janelaprincipal.iconphoto(False, self.imgicon)


        self.lbl_verifica_escala = tk.Label(self.frm_cima, text="Verificar Escalas", font=("Arial",14), bg="#3CB371", fg="white", width=20, height=1)
        self.lbl_verifica_escala.place(x=10, y=90)
        self.lbl_verifica_escala.bind("<Button-1>", self.verifica_escala)





        #APRENDENDO
        self.text1 = tk.StringVar()
        w = tk.OptionMenu(self.janelaprincipal, self.text1, "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        w.config(bg="Green", fg="WHITE")
        w["menu"].config(bg="RED")
        w.place(x=10, y=150)
        

        self.Tipo_p = []





    def criar_escala(self, event):
        self.janela_criar_escala = tk.Toplevel()
        self.janela_criar_escala.title("Criar Escala")
        self.janela_criar_escala.grab_set()
        self.janela_criar_escala.geometry("600x400")


        self.lbl_nome_escala = tk.Label(self.janela_criar_escala, text="Nome da Escala:")
        self.lbl_nome_escala.place(x=10, y=10)

        self.entry_nome_escala = tk.Entry(self.janela_criar_escala, borderwidth=2)
        self.entry_nome_escala.place(x=10, y=30)

        self.lbl_dias = tk.Label(self.janela_criar_escala, text="Quantos dias:")
        self.lbl_dias.place(x=10, y=70)

        self.entry_dias = tk.Entry(self.janela_criar_escala, borderwidth=2)
        self.entry_dias.place(x=10, y=90)

        self.int_var_sem = tk.IntVar()
        self.int_var_fer = tk.IntVar()

        self.lbl_cont_final_semana = tk.Label(self.janela_criar_escala, text="Contará os finais de semana?")
        self.lbl_cont_final_semana.place(x=10, y=130)

        self.rbtn_cont_final_semanas = tk.Radiobutton(self.janela_criar_escala, text="Sim", variable=self.int_var_sem, value=1)
        self.rbtn_cont_final_semanas.place(x=10, y=150)
        
        self.rbtn_cont_final_semanan = tk.Radiobutton(self.janela_criar_escala, text="Não", variable=self.int_var_sem, value=2)
        self.rbtn_cont_final_semanan.place(x=90, y=150)



        self.lbl_cont_ferias = tk.Label(self.janela_criar_escala, text="Contará as Férias?")
        self.lbl_cont_ferias.place(x=10, y=190)

        self.rbtn_cont_feriass= tk.Radiobutton(self.janela_criar_escala, text="Sim", variable=self.int_var_fer, value=1)
        self.rbtn_cont_feriass.place(x=10, y=210)
        
        self.rbtn_cont_feriasn = tk.Radiobutton(self.janela_criar_escala, text="Não", variable=self.int_var_fer, value=2)
        self.rbtn_cont_feriasn.place(x=90, y=210)


        self.btn_ok = tk.Button(self.janela_criar_escala, text='Criar', command=self.button_criar_escala)
        self.btn_ok.place(x=100, y=350)


    def button_criar_escala(self):
        if self.Tipo_p != []:
            if (f"{self.entry_nome_escala.get()} - {self.string_Var_comb.get()}") in self.Tipo_p:
                print("replica")
                self.janela_criar_escala.destroy()
            else:
                self.Tipo_p.append(f"{self.entry_nome_escala.get()} - {self.string_Var_comb.get()}")
                self.janela_criar_escala.destroy()
        else:
            self.Tipo_p.append(f"{self.entry_nome_escala.get()} - {self.string_Var_comb.get()}")
            self.janela_criar_escala.destroy()




    def Nova_programacao(self, event):
        self.vetes = []
        #APRENDENDO
        #print(self.text1.get())

        self.janela2 = tk.Toplevel()
        self.janela2.grab_set()
        self.janela2.title("Nova Programação")
        self.janela2.geometry("500x400")
        self.frm_janela2_c = tk.Frame(self.janela2, width=500, height=400)
        self.frm_janela2_c.grid(column=0, row=0)


        self.lbl_programar = tk.Label(self.frm_janela2_c, text="Para quem:")
        self.lbl_programar.place(x=20, y=10)
        #Exemplos de colaboradores
        colaboradores = ["Busque por um colaborador", "jardeson", "Maria"]

        self.cbx_programar = ttk.Combobox(self.frm_janela2_c, values=colaboradores, state="readonly", font="30", width=28, height=5, )

        self.cbx_programar.place(x=20, y=30)
        self.cbx_programar.current(0)


        self.lbl_Tipo_p = tk.Label(self.frm_janela2_c, text="Tipo:")
        self.lbl_Tipo_p.place(x=20, y=60)
        #Exemplos de Tipos
        Tipo_p = []
        self.string_Var_comb_tipo_p = tk.StringVar()
        if self.Tipo_p != []:
            for Tips in self.Tipo_p:
                Tipo_p.append(str(Tips).split("-")[0])
                print(self.Tipo_p)
                print(Tipo_p)
                self.cbx_tipo_p = ttk.Combobox(self.frm_janela2_c, values=Tipo_p, state="readonly", font="30", width=28, height=5, textvariable=self.string_Var_comb_tipo_p)
        else:
            self.cbx_tipo_p = ttk.Combobox(self.frm_janela2_c, values=Tipo_p, state="readonly", font="30", width=28, height=5, textvariable=self.string_Var_comb_tipo_p)

            

        

        self.cbx_tipo_p.place(x=20, y=80)

        if self.cbx_tipo_p.get() != "":

            self.cbx_tipo_p.current(0)

        
        self.lbl_Periodo = tk.Label(self.frm_janela2_c, text="Periodo:")
        self.lbl_Periodo.place(x=20, y=110)
        #Exemplos de Periodos
        self.cal_escolha = Calendar(self.frm_janela2_c)
        self.cal_escolha.place(x=40, y=150)


        self.btn_ok = tk.Button(self.frm_janela2_c, text='OK', command=self.ok)
        self.btn_ok.place(x=100, y=350)

    def ok(self):
        self.vetes.append(self.cal_escolha.selection_get())
        self.janela2.destroy()


    def verifica_escala(self, event):
        self.janela_verifica = tk.Toplevel()
        self.janela_verifica.grab_set()
        self.janela_verifica.title("Exemplo")
        self.janela_verifica.geometry("600x400")

        # self.janela_verifica.overrideredirect(True)
        #self.janela_verifica["bg"] = "gray"
        


        cor_escolhida = "#FFFACD"

        cal = Calendar(self.janela_verifica, font="Arial 14", locale='pt_BR', cursor="hand1", selectmode="none", background='#008000', foreground='white')

        

        #data atual =  date = cal.datetime.today()
        date = cal.datetime.today()


        print(self.vetes)


        escala_ecolha_dia = self.cal_escolha.selection_get()#cal.datetime(ano, mes, dia)
        print(escala_ecolha_dia)


        for sas in self.Tipo_p:
            dias_de_escala = (str(sas).split("-")[-1])
            dias_de_escala = int(dias_de_escala)
            print(dias_de_escala)


        for i in range(0, dias_de_escala):
        
            cal.calevent_create(escala_ecolha_dia + cal.timedelta(days=i), 'Reminder 1', 'reminder')

        feriados= holidays.Brazil()

        ano_feriado = str(date).split("-")[0]
        vetor_ferias = []
        for feriado in feriados[f"{ano_feriado}-01-01": f'{ano_feriado}-12-31']:

            dia = str(feriado).split("-")[2]
            mes = str(feriado).split("-")[1]
            ano = str(feriado).split("-")[0]
            

            feriados = cal.datetime(year=int(ano), month=int(mes), day=int(dia))
            
            cal.calevent_create(feriados , 'Reminder 1', 'reminder 2')

            vetor_ferias.append(int(dia))
        

        cal.tag_config('reminder 2', background='#FF7F50', foreground='white')
        cal.tag_config('reminder', background=cor_escolhida, foreground='black')

        cal.pack(fill="both", expand=True)





janela = tk.Tk()
Tela(janela)
janela.mainloop()
"""
folgas: verde
sobreaviso: vermelho
ferias: verde
"""