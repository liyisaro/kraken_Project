# Funcion para que el usuario eliga de la lista desplegable de cotizaciones disponibles

import tkinter as tk

def fun_moneda():
    try:
        with open('monedalist.txt', 'r') as dict_file:      # Lectura del txt con monedas disponibles
            dict_text = dict_file.read()
            dict_from_file = eval(dict_text)
        dmoneda = {}
        OptionList=[]
        for k in dict_from_file['result'].keys():
            dmoneda[k]=dict_from_file['result'][k]['wsname']


        for k in dmoneda.values():
            OptionList.append(k)        # Cadena a mostrar en la lista desplegable

        app = tk.Tk()       # Creación del objeto

        app.geometry('100x200')       # Definir tamaño de la interfaz grafica para la lista desplegable

        variable = tk.StringVar(app)  # Definir el objeto como una lista desplegable

        variable.set(OptionList[0])   # Fijar un valor por defecto en la lista al iniciar la aplicacion

        opt = tk.OptionMenu(app, variable, *OptionList)  # Confirguración visual de la lista desplegable
        opt.config(width=90, font=('Helvetica', 12))
        opt.pack(side="top")

        labelTest = tk.Label()

        tk.Button(app, text="ok", command=app.destroy).pack()  # Creación de boton para confirmar seleccion de monedas

        app.mainloop()

        value1 = list(dmoneda.keys())[list(dmoneda.values()).index(variable.get())]  # Almacenar la selección en una variable

        return(value1,variable.get())

    except Exception as e:      # Manejo de excepciones
        error = repr(e)
        print('Error obteniendo los pares de monedas disponibles: ' + error)