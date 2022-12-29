import pandas_ta as pta
import plotly.express as px

def rsiplot(df,moneda):

    try:
        periodos=14
        df['rsi'] = pta.rsi(df['PRICE'].astype('float'), length = periodos)
        fig = px.line(df,y='rsi',x='DATE_TIME',title='RSI '+moneda +' en '+str(periodos)+' periodos')
        fig.update_yaxes(categoryorder='category ascending')
        fig.update_layout(template='plotly_dark')
        fig.show()

    except Exception as e:
        error = repr(e)
        print('Error al graficar RSI: ' + error)