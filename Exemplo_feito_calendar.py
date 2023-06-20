import tkinter as tk
from tkcalendar import Calendar, DateEntry
import holidays


class Tela:
    def __init__(self, master):
        self.janelaprincipal = master
        self.janelaprincipal.title("Exemplo")
        self.janelaprincipal.geometry("600x400")

        mes = 2
        ano = 2023
        dia = 1
        dias_de_escala = 30
        cor_escolhida = "#FFFACD"

        cal = Calendar(self.janelaprincipal, font="Arial 14", locale='pt_BR', cursor="hand1", selectmode="none", background='#008000', foreground='white')

        

        #data atual =  date = cal.datetime.today()
        date = cal.datetime.today()

        escala_ecolha_dia = cal.datetime(ano, mes, dia)


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