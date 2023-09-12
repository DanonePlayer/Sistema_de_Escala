from datetime import datetime, timedelta
import tkinter as tk
from tkcalendar import Calendar
# # Suponha que você já tem as variáveis ano_escolha, mes_escolha e dia_escolha definidas
# ano_escolha = 2023
# mes_escolha = 8
# dia_escolha = 27
# dias_a_adicionar = 39

# data_atual = datetime(ano_escolha, mes_escolha, dia_escolha)
# nova_data = data_atual + timedelta(days=dias_a_adicionar)

# # A nova_data agora contém a data resultante após adicionar 30 dias
# print(nova_data.strftime("%d/%m/%Y"))




root = tk.Tk()
cal_show = Calendar(root)
cal_show.pack()


Adicionar_dias = 1



data_str = "06/09/2023"
data_evento = datetime.strptime(data_str, "%d/%m/%Y")

data_evento = data_evento + timedelta(days=Adicionar_dias)

cal_show.calevent_create(data_evento , 'Ferias', 'Ferias')
cal_show.tag_config('Ferias', background="red", foreground='white')

root.mainloop()