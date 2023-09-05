import tkinter as tk
from datetime import datetime, timedelta

from tkcalendar import Calendar


def adicionar_dias():
    data_atual = cal.get_date()
    data_atual = datetime.strptime(data_atual, "%d/%m/%Y")
    
    # Adicione o número de dias que você deseja à data atual
    dias_a_adicionar = 40  # Altere esse valor para a quantidade de dias que você deseja adicionar
    nova_data = data_atual + timedelta(days=dias_a_adicionar)
    print(nova_data)
    
    # Destrua o widget Calendar atual e crie um novo com a nova data
    cal.destroy()
    criar_calendario(nova_data.strftime("%d/%m/%Y"))

def criar_calendario(data):
    global cal
    cal = Calendar(root, date_pattern="dd/MM/yyyy", date=data)
    cal.pack(padx=20, pady=20)

root = tk.Tk()
root.title("Atualizar Calendário")

criar_calendario("")  # Crie o widget Calendar vazio

botao_adicionar = tk.Button(root, text="Adicionar Dias", command=adicionar_dias)
botao_adicionar.pack()

root.mainloop()