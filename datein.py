# Selección por parte del usuario de la fecha a partir de la cual se desean las cotizaciones

from tkinter import *
from tkcalendar import Calendar
from datetime import datetime

def fun_init_date():

    # Create Object
    root = Tk()
    
    # Set geometry
    root.geometry("400x400")
    
    # Add Calendar
    cal = Calendar(root, selectmode = 'day',
                year = 2020, month = 5,
                day = 22)
    
    cal.pack(pady = 20)
    
    def grad_date():
        date.config(text = "Fecha de inicio seleccionada: " + cal.get_date())
    
    # Add Button and Label
    Button(root, text = "Seleccionar fecha inicio",
        command = grad_date).pack(pady = 20)
    
    date = Label(root, text = "")
    date.pack(pady = 20)
    
    # Execute Tkinter
    Button(root, text="Finalizar", command=root.destroy).pack()
    root.mainloop()
    init_date = datetime.strptime(cal.get_date(), '%m/%d/%y')
    return(init_date)