# Selección por parte del usuario de la fecha a partir de la cual se desean las cotizaciones

from tkinter import *               # Librerias para poder mostrar el calendario y seleccionar fecha
from tkcalendar import Calendar
from datetime import datetime

def fun_init_date():
    try:
        # Creacion del objeto
        root = Tk()

        # Determinar el tamaño del calendario
        root.geometry("400x400")

        # Añadir el calendario y fijar una fecha por defecto al mostrarse al usuario
        cal = Calendar(root, selectmode = 'day',
                    year = 2022, month = 12,
                    day = 27)

        cal.pack(pady = 20)

        def grad_date():
            date.config(text = "Fecha de inicio seleccionada: " + cal.get_date())

        # Añadir boton y etiqueta para seleccionar la fecha
        Button(root, text = "Seleccionar fecha inicio",
            command = grad_date).pack(pady = 20)

        date = Label(root, text = "")
        date.pack(pady = 20)

        # ejecutar al seleccionar el boton de finalizar, se obtiene la fecha de inicio de cotizaciones
        Button(root, text="Finalizar", command=root.destroy).pack()
        root.mainloop()
        init_date = datetime.strptime(cal.get_date(), '%m/%d/%y')
        return(init_date)

    except Exception as e:  #Manejo de excepciones en caso de error en la función
        error = repr(e)
        print('Error al definir la fecha de inicio para la descarga de cotizaciones: ' + error)
