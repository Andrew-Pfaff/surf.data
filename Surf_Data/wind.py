import pandas
import requests
import wget
import urllib.request
from datetime import date

#dataset is 6 hours ahead

def rounder(number, multiple):
	answer = multiple * (number / multiple)
	return answer

start_time = "08:06" #REPLACE THIS WITH INPUT FROM OTHER FILE
end_time = "09:06" #REPLACE THIS WITH INPUT FROM OTHER FILE
date = "2022-07-31" #REPLACE THIS WITH INPUT FROM OTHER FILE

strt_sesh_hr = int(start_time[:2])
start_sesh_mn = int(start_time[3:5])

end_sesh_hr = int(end_time[:2])
end_sesh_mn = int(end_time[3:5])


start_sesh_total_mn = strt_sesh_hr*60 + start_sesh_mn
start_sesh_total_mn = rounder(start_sesh_total_mn, 6)

end_sesh_total_mn = end_sesh_hr*60 + end_sesh_mn
end_sesh_total_mn = rounder(end_sesh_total_mn, 6)





sesh_yr = date[:4]
sesh_mnth = date[5:7]
sesh_day = date[8:10]





url = 'https://www.ndbc.noaa.gov/data/realtime2/NTBC1.txt'
response = urllib.request.urlopen(url)
winddata=pandas.read_fwf(response)
winddata = winddata.drop(winddata.index[0])
winddata = winddata[['#YY','MM', 'DD', 'hh', 'mm', 'WDIR', 'WSPD']]

winddata = winddata[winddata.WSPD != "MM"]

winddata['hh'] = winddata['hh'].astype(int)
winddata['mm'] = winddata['mm'].astype(int)
winddata['WSPD'] = winddata['WSPD'].astype(float)


winddata['wind_minutes_plus_hours'] = winddata['mm'] + (winddata['hh'] * 60)

winddata_during_sesh = winddata.loc[(winddata['MM'] == sesh_mnth) & (winddata['DD'] == sesh_day)]
winddata_during_sesh = winddata_during_sesh[winddata_during_sesh['wind_minutes_plus_hours'].between(start_sesh_total_mn, end_sesh_total_mn)]


start_wind_speed = winddata_during_sesh['WSPD'].iat[0]
end_wind_speed = winddata_during_sesh['WSPD'].iat[-1]


average_wind_speed = winddata_during_sesh["WSPD"].mean()

start_wind_direction = winddata_during_sesh['WDIR'].iat[0]
end_wind_direction = winddata_during_sesh['WDIR'].iat[-1]

mode_wind_direction = winddata_during_sesh["WDIR"].mode()