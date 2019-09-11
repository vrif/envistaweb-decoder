import pandas as pd
import numpy as np
import datetime

def load_AQ_data_excel(url):
    
    '''
    Imports Hourly XLS files from https://envistaweb.env.gov.bc.ca/DynamicTable2.aspx?G_ID=331
    Please see readme on how to download files from the website.
    This decoder only works with hourly data.
    
    Arguments:
    url -- The location of the targeted file
    
    Returns:
    data --  Returns a pandas DataFrame of the data
    
    '''
    
    data = pd.read_excel(url)
    
    data.columns = data.loc[0]
    data.drop(index=[0,1], inplace=True)
    data.drop(index=data[-8:].index, inplace=True) #Removes bottom rows.
    
    for i in range(data.shape[0]):
        if (data['Time'].iloc[i] == '24:00 AM'): #If the datetime is 24:00 AM, shift the day by +1
            data['Date'].iloc[i] += pd.DateOffset(1)
        elif (isinstance(data['Time'].iloc[i], datetime.time)): #Changes the format of the timestamp
            data['Date'].iloc[i] += pd.to_timedelta(data['Time'].iloc[i].strftime("%H:%M:%S"))
        else: #Accounts for blank lines.
            pass
    
    data.drop(columns='Time', inplace=True)
    data['Date'] = pd.to_datetime(data['Date']) #converts to datetime
    data.reset_index(drop=True, inplace=True)
    
    return(data)


def load_AQ_data_csv(url):
    
    '''
    Imports Hourly CSV files from https://envistaweb.env.gov.bc.ca/DynamicTable2.aspx?G_ID=331
    Please see readme on how to download files from the website.
    This decoder only works with hourly data.
    
    Arguments:
    url -- The location of the targeted file
    
    Returns:
    data --  Returns a pandas DataFrame of the data
    
    '''
    
    data = pd.read_csv(url)

    data.drop(columns=data.columns[0], inplace=True)
    data.drop(index=[0], inplace=True)
    data.drop(index=data[-8:].index, inplace=True) #Removes bottom rows.

    data.reset_index(drop=True, inplace=True)

    colname = list(map(lambda x: x.strip(), list(data.columns.values)))
    colname[0] = 'Date'
    data.columns = colname

    for i in range(data.shape[0]):
        #Try to convert the entry to date time. If it fails, the code assembles the datetime stamp
        try:
            data['Date'].iloc[i] = pd.to_datetime(data['Date'].iloc[i])
        except:
            date_split_list = str.split(data['Date'].iloc[i].strip(), sep=' ')
            data['Date'].iloc[i] = pd.to_datetime(date_split_list[0]) + pd.DateOffset(1)
            
    data.reset_index(drop=True, inplace=True)
    data['Date'] = pd.to_datetime(data['Date']) #converts to datetime
    
    return(data)