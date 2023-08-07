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

        self.lbl_novaprog = tk.Label(self.frm_cima, text="Atribuir Escala", font=("Arial",14), bg="#3CB371", fg="white", width=20, height=1)
        self.lbl_novaprog.place(x=10, y=50)
        self.lbl_novaprog.bind("<Button-1>", self.Atribuir_Escala)

        self.imgicon = tk.PhotoImage(file="Images/a.png", height=222)
        self.janelaprincipal.iconphoto(False, self.imgicon)

        self.lbl_verifica_escala = tk.Label(self.frm_cima, text="Verificar Escalas", font=("Arial",14), bg="#3CB371", fg="white", width=20, height=1)
        self.lbl_verifica_escala.place(x=10, y=90)
        self.lbl_verifica_escala.bind("<Button-1>", self.verificar_escala)

        # #APRENDENDO
        # self.text1 = tk.StringVar()
        # w = tk.OptionMenu(self.janelaprincipal, self.text1, "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        # w.config(bg="Green", fg="WHITE")
        # w["menu"].config(bg="RED")
        # w.place(x=10, y=150)
        

        self.Tipo_escala = []


    def Atribuir_Escala(self, event):
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
        
        query = 'SELECT usuario_id, nome_completo, nome_usuario FROM usuario;'
        dados = bd.consultar(query)
        colaboradores = []
        for tupla in dados:
            colaboradores.append(tupla[1])
        self.cbx_usuario = ttk.Combobox(self.frm_janela2_c, values=colaboradores, state="readonly", font="30", width=28, height=5, )

        self.cbx_usuario.place(x=20, y=30)
        self.cbx_usuario.current(0)

        self.lbl_Tipo_escala = tk.Label(self.frm_janela2_c, text="Tipo:")
        self.lbl_Tipo_escala.place(x=20, y=60)

        self.string_Var_comb_tipo_p = tk.StringVar()

        query = 'SELECT nome_escala FROM escala;'
        dados = bd.consultar(query)

        for tupla in dados:
            for escala in tupla:
                self.Tipo_escala.append(escala)

        self.cbx_tipo_escala = ttk.Combobox(self.frm_janela2_c, values=self.Tipo_escala, state="readonly", font="30", width=28, height=5, textvariable=self.string_Var_comb_tipo_p)
        self.cbx_tipo_escala.place(x=20, y=80)
        self.cbx_tipo_escala.current(0)

        
        self.lbl_Periodo = tk.Label(self.frm_janela2_c, text="Periodo:")
        self.lbl_Periodo.place(x=20, y=110)
        #Exemplos de Periodos

        self.cal_escolha = Calendar(self.frm_janela2_c, locale='pt_BR', date_pattern='dd/MM/yyyy')
        self.cal_escolha.place(x=40, y=150)


        self.btn_ok = tk.Button(self.frm_janela2_c, text='Criar', command=self.Criar)
        self.btn_ok.place(x=100, y=350)

    def Criar(self):
        # print(self.cbx_usuario.get())
        # print(self.cbx_tipo_escala.get())
        # print(self.cal_escolha.selection_get()) 
        query = f'''SELECT usuario_id, escala_id FROM escala, usuario 
        WHERE nome_escala LIKE "{self.cbx_tipo_escala.get()}" and nome_completo LIKE "{self.cbx_usuario.get()}";'''
        dados = bd.consultar(query)

        ids = []

        for tupla in dados:
            for id in tupla:
                ids.append(id)

        usuario_id = ids[0]
        escala_id = ids[1]
        data_inicio = self.cal_escolha.get_date()
        query = f'INSERT INTO usuario_escala ("usuario_id", "escala_id", "data_inicio") VALUES ("{usuario_id}", {escala_id}, "{data_inicio}");'
        bd.inserir(query)
        self.janela2.destroy()


    def verificar_escala(self, event):
        self.janela_verifica_escala = tk.Toplevel()
        self.janela_verifica_escala.title("Exemplo")
        self.janela_verifica_escala.geometry("600x400")
        
        query = f'SELECT nome_completo FROM usuario;'
        dados = bd.consultar(query)

        usu = []

        for tupla in dados:
            for usuario in tupla:
                usu.append(usuario)
        # print(usu)

        self.cbx_usuario_es = ttk.Combobox(self.janela_verifica_escala, values=usu, state="readonly", font="30", width=28, height=5, )
        self.cbx_usuario_es.place(x=20, y=30)
        self.cbx_usuario_es.current(0)

        query = f'SELECT nome_escala FROM escala;'
        dados = bd.consultar(query)

        escala = []

        for tupla in dados:
            for usuario in tupla:
                escala.append(usuario)
        # print(escala)

        self.cbx_escala_es = ttk.Combobox(self.janela_verifica_escala, values=escala, state="readonly", font="30", width=28, height=5, )
        self.cbx_escala_es.place(x=20, y=80)
        self.cbx_escala_es.current(0)

        self.btn_verifica = tk.Button(self.janela_verifica_escala, text='Verificar', command=self.Aplica_Calendario)
        self.btn_verifica.place(x=100, y=150)

        self.verifica_cal = Calendar(self.janela_verifica_escala, font="Arial 14", locale='pt_BR', cursor="hand1", selectmode="none", background='#008000', foreground='white')
        self.verifica_cal.place(x=200, y=150)


    def Aplica_Calendario(self):
        query = f'''SELECT eu.usuario_escala_id
        FROM usuario_escala eu
        JOIN usuario u ON u.usuario_id = eu.usuario_id
        JOIN escala e ON e.escala_id = eu.escala_id
        WHERE u.nome_completo LIKE "{self.cbx_usuario_es.get()}"
        AND e.nome_escala LIKE  "{self.cbx_escala_es.get()}";'''
        dados = bd.consultar(query)

        self.id_usu_escala = 0

        for tupla in dados:
            for id in tupla:
                self.id_usu_escala = id
        # print(self.id_usu_escala)
        if self.id_usu_escala != 0:
            # print(self.id_usu_escala)
            query = f'SELECT data_inicio FROM usuario_escala WHERE usuario_escala_id = {self.id_usu_escala};'
            dados = bd.consultar(query)
            dados = dados[0]

            for data_escala in dados:
                pass
            data_escala = str(data_escala)
            data_escala = data_escala.split("/")

            DIAS = [
            'Segunda-feira',
            'Terça-feira',
            'Quarta-feira',
            'Quinta-Feira',
            'Sexta-feira',
            'Sábado',
            'Domingo'
            ]

            query = f'''SELECT e.dias_escala
            FROM usuario_escala ue
            JOIN escala e ON ue.escala_id = e.escala_id
            WHERE ue.usuario_escala_id = {self.id_usu_escala}'''
            dados = bd.consultar(query)
            dados = dados[0]
            for dias_de_escala in dados:
                pass
            # print(dias_de_escala)


            query = f'''SELECT e.finais_semana, e.feriados
            FROM usuario_escala ue
            JOIN escala e ON ue.escala_id = e.escala_id
            WHERE ue.usuario_escala_id = {self.id_usu_escala}'''
            dados = bd.consultar(query)
            for contar_finais_semana, conta_feriados in dados:
                pass

            mes_escolha = int(data_escala[1])
            ano_escolha = int(data_escala[2])
            dia_escolha = int(data_escala[0])
            cor_escolhida_escala = "#FFFACD"
            cor_escolhida_ferias = "#FF7F50"
            vetor_dias_corridos_na_escala = []
            vetor_finais_semana = []
            dia_cont = dia_escolha

            procura_final_semana = dias_de_escala
            
            year = ano_escolha
            month = mes_escolha

            if contar_finais_semana == 0:
                while procura_final_semana > 0:
                    day = dia_cont
                    # print(dia_cont)

                    # print(year, month, day)
                    data_ = datetime(year, month, day)
                    # monthrange retorna o último dia do mês, basta setá-lo na data e pronto
                    Ultimo_dia_mes = data_.replace(day=monthrange(data_.year, data_.month)[1])

                    data_ = datetime(year, 12, day)
                    # monthrange retorna o último dia do mês, basta setá-lo na data e pronto
                    Ultimo_dia_ano = data_.replace(day=monthrange(data_.year, data_.month)[1])


                    data = datetime(year, month, day)
                    # print(data)   


                    indice_da_semana = data.weekday()
                    # print(indice_da_semana)


                    dia_da_semana = DIAS[indice_da_semana]
                    # print(dia_da_semana)

                    numero_do_dia_da_semana = data.isoweekday()
                    # print(numero_do_dia_da_semana)
                
                    if(numero_do_dia_da_semana == 6 or numero_do_dia_da_semana == 7 ):
                        # print("Final de semana")
                        vetor_finais_semana.append(data)
                        dias_de_escala += 1
                        procura_final_semana +=1
                        # print(data)

                    if dia_cont == 28 or dia_cont == 29 or dia_cont == 30 or dia_cont == 31 or dia_cont == 32:
                        if dia_cont == Ultimo_dia_mes.day:
                            month += 1
                            dia_cont = 0
                        if Ultimo_dia_ano.day > year:
                            year +=1
                        

                    dia_cont += 1
                    procura_final_semana -=1


            #data atual =  date = cal.datetime.today()
            date = self.verifica_cal.datetime.today()

            escala_ecolha_dia = self.verifica_cal.datetime(ano_escolha, mes_escolha, dia_escolha)
            #print(escala_ecolha_dia)

            #pegando todos os dias escolhidos na escala para comparar depois com as ferias
            dias = 0
            aux_dias_de_escala = dias_de_escala
            while dias < aux_dias_de_escala:
                # print(dia_escolha + dias)
                data_ = datetime(ano_escolha, mes_escolha, dia_escolha + dias)
                # monthrange retorna o último dia do mês, basta setá-lo na data e pronto
                Ultimo_dia_mes = data_.replace(day=monthrange(data_.year, data_.month)[1])
                if dia_escolha + dias == Ultimo_dia_mes.day:
                    mes_escolha += 1
                    dia_escolha = 1

                dias_corridos_na_escala = self.verifica_cal.datetime(ano_escolha, mes_escolha, dia_escolha + dias)
                #print(dias_corridos_na_escala)
                vetor_dias_corridos_na_escala.append(dias_corridos_na_escala)

                aux_dias_de_escala -=1
                dias +=1


            feriados= holidays.Brazil()

            ano_feriado = str(date).split("-")[0]
            vetor_feriados = []
            for feriado in feriados[f"{ano_feriado}-01-01": f'{ano_feriado}-12-31']:

                dia = str(feriado).split("-")[2]
                mes = str(feriado).split("-")[1]
                ano = str(feriado).split("-")[0]

                feriados = self.verifica_cal.datetime(year=int(ano), month=int(mes), day=int(dia))
                #print(feriados)
                
                vetor_feriados.append(feriados)

                if conta_feriados == 0:
                    if feriados in vetor_dias_corridos_na_escala:
                        dias_de_escala += 1
            
            for feriados1 in vetor_feriados:
                self.verifica_cal.calevent_create(feriados1 , 'Ferias', 'Ferias')


            for i in range(0, dias_de_escala):
                self.verifica_cal.calevent_create(escala_ecolha_dia + self.verifica_cal.timedelta(days=i), 'escalas', 'escala')

            if conta_feriados == 0:
                for feriados1 in vetor_feriados:
                    self.verifica_cal.calevent_create(feriados1 , 'Ferias', 'Ferias')

            for final_semana in vetor_finais_semana:
                self.verifica_cal.calevent_create(final_semana, "final_semana", "final_semana")
            


            self.verifica_cal.tag_config('Ferias', background=cor_escolhida_ferias, foreground='white')
            self.verifica_cal.tag_config('escala', background=cor_escolhida_escala, foreground='black')
            self.verifica_cal.tag_config("final_semana", background="#cccccc", foreground='black')
            

            # print(dia_escolha, ano_escolha, mes_escolha, dias_de_escala)


janela = tk.Tk()
Tela(janela)
janela.mainloop()
"""
folgas: verde
sobreaviso: vermelho
ferias: verde
"""