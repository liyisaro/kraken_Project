# Funcion para hacer el llamado a la API
import os
import krakenex
import pandas as pd
import time
import platform
import datetime
from datetime import datetime, timedelta

def tstamp2date(x):
    return datetime.fromtimestamp(x)

def fun_call_api(init_date,moneda_find):
    k = krakenex.API()
    k.load_key('kraken.key')
    df = pd.DataFrame(columns=[0, 1, 2, 3, 4, 5, 6])

    init_date = datetime.timestamp(init_date)
    balance = k.query_public('Trades?pair=' + moneda_find)
    end_date = pd.DataFrame(balance['result'][moneda_find])[2].max()-1
    sistema = platform.system()

    while init_date <= end_date:
        balance = k.query_public('Trades?pair='+moneda_find+'&since='+str(init_date))
        df = df.append(balance['result'][moneda_find], ignore_index=True)
        init_date = df[2].max()+1
        if sistema == 'Windows':
            os.system('cls')
        time.sleep(1)
        print('Descargando cotizaciones, por favor espere...')
    df= df.rename(columns={0: "PRICE", 1: "VOLUME", 2: "TIME", 3: "BUY/SELL", 4: "MARKET/LIMIT", 5: "miscellaneous", 6: "ID"})    
    df['DATE_TIME']=df['TIME'].apply(tstamp2date)
    print('\033[1m'+"COTIACIONES DESCARGADAS"+'\033[0m')
    return df
