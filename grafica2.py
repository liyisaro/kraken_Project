# Función para graficar RSI del par de cotizaciones

import pandas_ta as pta
import plotly.express as px

def rsiplot(df,moneda):

    try:
        # Definición de periodos
        periodos=14

        # Añadir columna del rsi al dataframe mediante pandas_ta, usando funcion rsi
        df['rsi'] = pta.rsi(df['PRICE'].astype('float'), length = periodos)

        # Graficar  RSI
        fig = px.line(df,y='rsi',x='DATE_TIME',title='RSI '+moneda +' en '+str(periodos)+' periodos')
        fig.update_yaxes(categoryorder='category ascending')
        fig.update_layout(template='plotly_dark')
        fig.show()

    # Manejo de excepciones
    except Exception as e:
        error = repr(e)
        print('Error al graficar RSI: ' + error)