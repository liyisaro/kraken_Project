import plotly.express as px
def plot2(df,moneda):

    try:
        df['M60'] = df['PRICE'].rolling(60).mean().round(6)
        dfp=df[['M60','DATE_TIME']]
        fig = px.line(dfp,y='M60',x='DATE_TIME',title='Media Movil 60 periodos '+moneda+' en el tiempo')
        fig.update_yaxes(categoryorder='category ascending')
        fig.update_layout(template='plotly_dark')
        fig.show()

    except Exception as e:
        error = repr(e)
        print('Error graficando la media movil: ' + error)