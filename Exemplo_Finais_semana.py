import tkinter as tk
from tkcalendar import Calendar, DateEntry
import holidays


class Tela:
    def __init__(self, master):
        self.janelaprincipal = master
        self.janelaprincipal.title("Exemplo")
        self.janelaprincipal.geometry("600x400")

        mes = 6
        ano = 2023
        dia = 1
        dias_de_escala = 11
        cor_escolhida_escala = "#FFFACD"
        cor_escolhida_ferias = "#FF7F50"
        vetor_dias_corridos_na_escala = []

        cal = Calendar(self.janelaprincipal, font="Arial 14", locale='pt_BR', cursor="hand1", selectmode="none", background='#008000', foreground='white')

        

        #data atual =  date = cal.datetime.today()
        date = cal.datetime.today()

        escala_ecolha_dia = cal.datetime(ano, mes, dia)
        #print(escala_ecolha_dia)

        #pegando todos os dias escolhidos na escala para comparar depois com as ferias
        for dias in range(1, dias_de_escala+1):
            dias_corridos_na_escala = cal.datetime(ano, mes, dias)
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
        
            
        
        for i in range(0, dias_de_escala):
            cal.calevent_create(escala_ecolha_dia + cal.timedelta(days=i), 'escalas', 'escala')

        for feriados1 in vetor_feriados:
            cal.calevent_create(feriados1 , 'Ferias', 'Ferias')


        cal.tag_config('Ferias', background=cor_escolhida_ferias, foreground='white')
        cal.tag_config('escala', background=cor_escolhida_escala, foreground='black')

        cal.pack(fill="both", expand=True)




janela = tk.Tk()
Tela(janela)
janela.mainloop()