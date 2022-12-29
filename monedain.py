# Funcion para que el usuario eliga de la lista desplegable de cotizaciones disponibles

import tkinter as tk
from tk import *

def fun_moneda():
    try:
        with open('monedalist.txt', 'r') as dict_file:
            dict_text = dict_file.read()
            dict_from_file = eval(dict_text)
        dmoneda = {}
        OptionList=[]
        for k in dict_from_file['result'].keys():
            dmoneda[k]=dict_from_file['result'][k]['wsname']


        for k in dmoneda.values():
            OptionList.append(k)

        app = tk.Tk()

        app.geometry('100x200')

        variable = tk.StringVar(app)
        #variable2 = tk.StringVar(app)

        variable.set(OptionList[0])
        #variable2.set(OptionList[0])

        opt = tk.OptionMenu(app, variable, *OptionList)
        opt.config(width=90, font=('Helvetica', 12))
        opt.pack(side="top")

        #opt2 = tk.OptionMenu(app, variable2, *OptionList)
        #opt2.config(width=90, font=('Helvetica', 12))
        #opt2.pack(side="top")

        labelTest = tk.Label()

        #variable.trace("w",'callback')

        tk.Button(app, text="ok", command=app.destroy).pack()

        app.mainloop()
        #value1=variable.get()
        #value2=variable2.get()
        value1=list(dmoneda.keys())[list(dmoneda.values()).index(variable.get())]
        #value2=list(dmoneda.keys())[list(dmoneda.values()).index(variable2.get())]
        #print(value1)
        #print(value2)
        return(value1,variable.get())

    except Exception as e:
        error = repr(e)
        print('Error obteniendo los pares de monedas disponibles: ' + error)