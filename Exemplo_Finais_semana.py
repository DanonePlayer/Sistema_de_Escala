import tkinter as tk
from tkcalendar import Calendar, DateEntry
import holidays
from datetime import datetime


class Tela:
    def __init__(self, master):
        self.janelaprincipal = master
        self.janelaprincipal.title("Exemplo")
        self.janelaprincipal.geometry("600x400")
        DIAS = [
        'Segunda-feira',
        'Terça-feira',
        'Quarta-feira',
        'Quinta-Feira',
        'Sexta-feira',
        'Sábado',
        'Domingo'
        ]
        mes_escolha = 7
        ano_escolha = 2023
        dia_escolha = 1
        dias_de_escala = 11
        cor_escolhida_escala = "#FFFACD"
        cor_escolhida_ferias = "#FF7F50"
        vetor_dias_corridos_na_escala = []
        vetor_finais_semana = []
        
        for i in range(dia_escolha, dias_de_escala):
    
            data = datetime(year=ano_escolha, month=mes_escolha, day=i)
            # print(data)

            indice_da_semana = data.weekday()
            # print(indice_da_semana)


            dia_da_semana = DIAS[indice_da_semana]
            # print(dia_da_semana)

            numero_do_dia_da_semana = data.isoweekday()
            #print(numero_do_dia_da_semana)

            if(numero_do_dia_da_semana == 6 or numero_do_dia_da_semana == 7 ):
                # print("Final de semana")
                vetor_finais_semana.append(data)
                #dias_de_escala += 1

        cal = Calendar(self.janelaprincipal, font="Arial 14", locale='pt_BR', cursor="hand1", selectmode="none", background='#008000', foreground='white')

        

        #data atual =  date = cal.datetime.today()
        date = cal.datetime.today()

        escala_ecolha_dia = cal.datetime(ano_escolha, mes_escolha, dia_escolha)
        #print(escala_ecolha_dia)

        #pegando todos os dias escolhidos na escala para comparar depois com as ferias
        for dias in range(1, dias_de_escala+1):
            dias_corridos_na_escala = cal.datetime(ano_escolha, mes_escolha, dias)
            #print(dias_corridos_na_escala)
            vetor_dias_corridos_na_escala.append(dias_corridos_na_escala)

        feriados= holidays.Brazil()

        ano_feriado = str(date).split("-")[0]
        vetor_feriados = []
        for feriado in feriados[f"{ano_feriado}-01-01": f'{ano_feriado}-12-31']:

            dia = str(feriado).split("-")[2]
            mes = str(feriado).split("-")[1]
            ano = str(feriado).split("-")[0]

            feriados = cal.datetime(year=int(ano), month=int(mes), day=int(dia))
            #print(feriados)
            
            vetor_feriados.append(feriados)

            print(vetor_finais_semana)

            # if feriados in vetor_dias_corridos_na_escala:
            #     dias_de_escala += 1
        
        for i in range(0, dias_de_escala):
            cal.calevent_create(escala_ecolha_dia + cal.timedelta(days=i), 'escalas', 'escala')

        for feriados1 in vetor_feriados:
            cal.calevent_create(feriados1 , 'Ferias', 'Ferias')

        for final_semana in vetor_finais_semana:
            cal.calevent_create(final_semana, "final_semana", "final_semana")
        


        cal.tag_config('Ferias', background=cor_escolhida_ferias, foreground='white')
        cal.tag_config('escala', background=cor_escolhida_escala, foreground='black')
        cal.tag_config("final_semana", background="#dbd6d1", foreground='black')

        cal.pack(fill="both", expand=True)

        # print(dia_escolha, ano_escolha, mes_escolha, dias_de_escala)





janela = tk.Tk()
Tela(janela)
janela.mainloop()








# for i in range(1, 32):
    
#     data = date(year=2023, month=7, day=i)
#     print(data)

#     indice_da_semana = data.weekday()
#     print(indice_da_semana)


#     dia_da_semana = DIAS[indice_da_semana]
#     print(dia_da_semana)

#     numero_do_dia_da_semana = data.isoweekday()
#     #print(numero_do_dia_da_semana)

#     if(numero_do_dia_da_semana == 6 or numero_do_dia_da_semana == 7 ):
#         print("Final de semana")