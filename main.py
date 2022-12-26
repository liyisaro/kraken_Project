import datein
import llamar_api
import monedain

init_date=datein.fun_init_date()

moneda = monedain.fun_moneda()
moneda_find = moneda[0]+moneda[1]
print(moneda_find)
print(type(moneda_find))

df = llamar_api.fun_call_api(init_date, moneda_find)
print(df)


