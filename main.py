import datein
import llamar_api
import monedain
import grafica1
import grafica2
import grafica3

init_date=datein.fun_init_date()

moneda = monedain.fun_moneda()
#moneda_find = moneda[0]+moneda[1]

df = llamar_api.fun_call_api(init_date, moneda[0])

grafica1.plot1(df,moneda[1])
grafica2.rsiplot(df,moneda[1])
grafica3.plot2(df,moneda[1])


