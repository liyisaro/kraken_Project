# Función para graficar la media movil (M60) del par de cotizaciones

import plotly.express as px
def plot2(df,moneda):

    try:
        #Agregar columna al dataframe con la media movil M60
        df['M60'] = df['PRICE'].rolling(60).mean().round(6)

        # Crear dataframe solo con las columnas de interes
        dfp=df[['M60','DATE_TIME']]

        # Grafica de la media movil vs fechas
        fig = px.line(dfp,y='M60',x='DATE_TIME',title='Media Movil 60 periodos '+moneda+' en el tiempo')
        fig.update_yaxes(categoryorder='category ascending')
        fig.update_layout(template='plotly_dark')
        fig.show()

    # Manejo de excepciones
    except Exception as e:
        error = repr(e)
        print('Error graficando la media movil: ' + error)