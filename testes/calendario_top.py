import tkinter as tk

from tkcalendar import Calendar


def adicionar_dias():
    # Obtém a data selecionada no TkCalendar
    data_selecionada = cal.get_date()

    # Converte a data para um objeto datetime (você pode precisar da biblioteca datetime)
    from datetime import datetime, timedelta
    data_datetime = datetime.strptime(data_selecionada, '%d/%m/%Y')

    # Adiciona a quantidade de dias desejada à data
    dias_a_adicionar = 7  # Substitua pelo número de dias que você deseja adicionar
    nova_data = data_datetime + timedelta(days=dias_a_adicionar)

    # Converte a nova data de volta para o formato de string
    nova_data_formatada = nova_data.strftime('%d/%m/%Y')

    # Define a nova data no TkCalendar
    cal._date = nova_data_formatada
    cal._calendar.selection_set(nova_data_formatada)

# Crie a janela principal
root = tk.Tk()
root.title("Adicionar Dias")

# Crie o widget TkCalendar
cal = Calendar(root, selectmode="day", date_pattern='dd/mm/yyyy')
cal.pack(pady=20)

# Botão para adicionar dias
botao_adicionar = tk.Button(root, text="Adicionar Dias", command=adicionar_dias)
botao_adicionar.pack()

# Inicie a interface gráfica
root.mainloop()