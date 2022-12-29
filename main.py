# Importar archivos con funciones

import datein
import llamar_api
import monedain
import grafica1
import grafica2
import grafica3

# Definir el init_date a partir de la ejecución de la funcion fun_init_date()
init_date=datein.fun_init_date()

# Definir el par de cotizaciones a descargar a paritr de la funcion fun_moneda()
moneda = monedain.fun_moneda()

# Definir el datagrame a partir del llamado a la API
df = llamar_api.fun_call_api(init_date, moneda[0])

# Llamar las funciones para graficar las cotizaciones, media movil y RSI
grafica1.plot1(df,moneda[1])
grafica2.rsiplot(df,moneda[1])
grafica3.plot2(df,moneda[1])


