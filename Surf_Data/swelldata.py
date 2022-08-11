import pandas as pd
import requests
import wget

def swell(day_time):
    
    station = '46053'
    url = 'https://www.ndbc.noaa.gov/data/realtime2/'+station+'.txt'


    #text file
    # data_txt = wget.download(url)

    #csv file
    data_csv = pd.read_csv(url, delim_whitespace=True)


    print(type(data_csv))

    start_time = day_time[1]
    end_time = day_time[2]
    date = day_time[3]
