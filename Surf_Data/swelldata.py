import pandas as pd
import requests
import wget


station = '46053'
url = 'https://www.ndbc.noaa.gov/data/realtime2/'+station+'.txt'


#text file
# data_txt = wget.download(url)

#csv file
data_csv = pd.read_csv(url, delim_whitespace=True)

print(data_csv)