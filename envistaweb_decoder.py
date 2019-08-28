import pandas as pd
import numpy as np
import datetime

def load_AQ_data(url):
    '''
    Imports Hourly XLS files from https://envistaweb.env.gov.bc.ca/DynamicTable2.aspx?G_ID=331
    Please see readme on how to download files from the website.
    This decoder only works with hourly data.
    '''
    data = pd.read_excel(url)
    
    data.columns = data.loc[0]
    
    for i in range(data.shape[0]):
        if (data['Time'].iloc[i] == '24:00 AM'):
            data['Date'].iloc[i] += pd.DateOffset(1)
        elif (isinstance(data['Time'].iloc[i], datetime.time)):
            data['Date'].iloc[i] += pd.to_timedelta(data['Time'].iloc[i].strftime("%H:%M:%S"))
        else:
            pass
    
    data.drop(columns='Time', inplace=True)
    data.drop(index=[0,1], inplace=True)
    data.drop(index=data[-8:].index, inplace=True) #Removes bottom rows.
    data['Date'] = pd.to_datetime(data['Date']) #converts to datetime
    data.reset_index(drop=True, inplace=True)
    
    return(data)