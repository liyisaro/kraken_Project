# Función para graficar el par de cortizaciones y la media movil

import plotly.express as px
def plot1(df,moneda):

    try:
        # Definir dataframe solo con precio y fecha
        dfp=df[['PRICE','DATE_TIME']]

        # Graficar precio vs fecha del par de cotizaciones
        fig = px.line(dfp,y='PRICE',x='DATE_TIME',title='Relacion '+moneda+' en el tiempo')
        fig.update_yaxes(categoryorder='category ascending')
        fig.update_layout(template='plotly_dark')
        # Graficar la media movil para 10 y 60 ciclos/periodos
        M10=df['PRICE'].rolling(10).mean().round(6)
        M60=df['PRICE'].rolling(60).mean().round(6)
        fig.add_scatter(x=df['DATE_TIME'], y=M10,name='Media movil 10')
        fig.add_scatter(x=df['DATE_TIME'], y=M60,name='Media movil 60')
        fig.show()

    # Manejo de Excepciones
    except Exception as e:
        error = repr(e)
        print('Error graficando las medias moviles y las cotizaciones: ' + error)