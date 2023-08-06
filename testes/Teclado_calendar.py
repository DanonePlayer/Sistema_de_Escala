import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime, timedelta

def on_key_press(event):
    if event.keysym == 'Right':
        next_day()
    elif event.keysym == 'Left':
        prev_day()
    elif event.keysym == 'Down':
        next_week()
    elif event.keysym == 'Up':
        prev_week()
    elif event.keysym == 'Return':  # Tecla Enter
        print_selected_date()

def next_day():
    current_date = datetime.strptime(cal.get_date(), '%d/%m/%Y')
    next_date = current_date + timedelta(days=1)
    cal.selection_set(next_date)

def prev_day():
    current_date = datetime.strptime(cal.get_date(), '%d/%m/%Y')
    prev_date = current_date - timedelta(days=1)
    cal.selection_set(prev_date)

def next_week():
    current_date = datetime.strptime(cal.get_date(), '%d/%m/%Y')
    next_date = current_date + timedelta(weeks=1)
    cal.selection_set(next_date)

def prev_week():
    current_date = datetime.strptime(cal.get_date(), '%d/%m/%Y')
    prev_date = current_date - timedelta(weeks=1)
    cal.selection_set(prev_date)

def print_selected_date():
    selected_date = cal.get_date()
    print("Data selecionada:", selected_date)

root = tk.Tk()
root.title("Calendário com Navegação pelo Teclado")

cal = Calendar(root, selectmode='day', date_pattern='dd/MM/yyyy')
cal.pack(padx=10, pady=10)

root.bind('<KeyPress>', on_key_press)

root.mainloop()