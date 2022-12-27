import plotly.express as px
def plot1(df,moneda):
    dfp=df[['PRICE','DATE_TIME']]
    fig = px.line(dfp,y='PRICE',x='DATE_TIME',title='Relacion '+moneda+' en el tiempo')
    fig.update_yaxes(categoryorder='category ascending')
    fig.update_layout(template='plotly_dark')
    M10=df['PRICE'].rolling(10).mean().round(6)
    M60=df['PRICE'].rolling(60).mean().round(6)
    fig.add_scatter(x=df['DATE_TIME'], y=M10,name='Media movil 10') # Not what is desired - need a line 
    fig.add_scatter(x=df['DATE_TIME'], y=M60,name='Media movil 60')
    fig.show()