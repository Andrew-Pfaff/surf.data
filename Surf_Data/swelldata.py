import requests
import json
import pandas 
from datetime import *
from time import *
import wget
import urllib.request
from datetime import *
import pandas
import requests
import wget
import urllib.request
from datetime import *
import sessiontime as st

user_date = st.getdate()
user_start_time = st.start_time()
user_end_time = st.end_time()



#format date and time user input into datetime format
user_start_datetime = datetime.strptime(date + " " + start_time, '%Y-%m-%d %H:%M')
user_end_datetime = datetime.strptime(date + " " + end_time, '%Y-%m-%d %H:%M')

user_start_time = user_start_datetime.time()
user_end_time = user_end_datetime.time()

user_date = user_start_datetime.date()





url = 'https://www.ndbc.noaa.gov/data/realtime2/46053.spec'
response = urllib.request.urlopen(url)
swells_data=pandas.read_fwf(response)


swells_data = swells_data.drop(0)





swells_data['date time'] =  pandas.to_datetime(swells_data["#YY"] + "/" + swells_data["MM"] + "/" + swells_data["DD"] + " " + swells_data["hh"] + ":" + swells_data["mm"])

swells_data.drop(['#YY', 'MM', "DD", "hh", "mm"], axis=1, inplace=True)


swells_data_during_sesh = swells_data[((swells_data['date time'].dt.date) == user_date)]
swells_data_during_sesh = swells_data_during_sesh.set_index('date time')
swells_data_during_sesh = swells_data_during_sesh.between_time(user_start_time, user_end_time)


swells_data_during_sesh['SwH'] = swells_data_during_sesh['SwH'].astype(float)
swells_data_during_sesh['SwP'] = swells_data_during_sesh['SwP'].astype(float)
swells_data_during_sesh['WWH'] = swells_data_during_sesh['WWH'].astype(float)
swells_data_during_sesh['WWP'] = swells_data_during_sesh['WWP'].astype(float)

SWH = swells_data_during_sesh["SwH"].mean()
SWp = swells_data_during_sesh["SwP"].mean()
WWH = swells_data_during_sesh["WWH"].mean()
WWp = swells_data_during_sesh["WWP"].mean()