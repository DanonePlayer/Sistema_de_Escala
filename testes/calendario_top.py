try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import tkinter as tk
    #import ttk

from tkcalendar import DateEntry

DateEntry(locale='en_US').pack()
DateEntry(locale='pt_BR', date_pattern='dd/MM/yyyy').pack()

tk.mainloop()