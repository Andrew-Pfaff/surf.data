import pandas
import requests
import wget
import urllib.request
from datetime import *

#dataset is 6 hours ahead
#data is taking every 6 minutes(thus data points are rounded to 6 multiples)
def wind(day_time):
	

	#start_time = "08:06" #REPLACE THIS WITH INPUT FROM OTHER FILE
	#end_time = "09:06" #REPLACE THIS WITH INPUT FROM OTHER FILE
	#date = "2022-07-31" #REPLACE THIS WITH INPUT FROM OTHER FILE
	
	#retreives user data from seperate file (start time end time of sesh)
	start_time = day_time[1]
	end_time = day_time[2]
	date = day_time[3]






	#format date and time user input into datetime format
	user_start_datetime = datetime.strptime(date + " " + start_time, '%Y-%m-%d %H:%M')
	user_end_datetime = datetime.strptime(date + " " + end_time, '%Y-%m-%d %H:%M')

	#Fomrat user inpited date into .date
	user_date = user_start_datetime.date()
	
	#Fomrat user inputed start and end time into .time
	user_start_time = user_start_datetime.time()
	user_end_time = user_end_datetime.time()



	#retrieve data from online source
	url = 'https://www.ndbc.noaa.gov/data/realtime2/NTBC1.txt'
	response = urllib.request.urlopen(url)
	winddata=pandas.read_fwf(response)
	winddata = winddata.drop(winddata.index[0])
		
	#Initial formatting of varibales to be kept in data set
	winddata = winddata[['#YY','MM', 'DD', 'hh', 'mm', 'WDIR', 'WSPD']]

	#deletes rows with missing values in wind speed
	winddata = winddata[winddata.WSPD != "MM"]

	#convert windspeed values to float
	winddata['WSPD'] = winddata['WSPD'].astype(float)

	#Concatenate date and time collums into new single collum formated with datetime.
	winddata['date time'] =  pandas.to_datetime(winddata["#YY"] + "/" + winddata["MM"] + "/" + winddata["DD"] + " " + winddata["hh"] + ":" + winddata["mm"])

	#change times to pacifc standard time
	winddata['date time'] = winddata['date time']-timedelta(hours=6)


	#drop previous time collums besides the single date and time collum
	winddata = winddata[['date time', 'WDIR', 'WSPD']]





	#keep data that is from times during user inputted sesh time
	winddata_during_sesh = winddata[((winddata['date time'].dt.date) == user_date)]
	winddata_during_sesh = winddata_during_sesh.set_index('date time')
	winddata_during_sesh = winddata_during_sesh.between_time(user_start_time, user_end_time)



	#retreive the statstics for the data during sesh
	start_wind_speed = winddata_during_sesh['WSPD'].iat[0]
	end_wind_speed = winddata_during_sesh['WSPD'].iat[-1]


	average_wind_speed = winddata_during_sesh["WSPD"].mean()

	start_wind_direction = winddata_during_sesh['WDIR'].iat[0]
	end_wind_direction = winddata_during_sesh['WDIR'].iat[-1]

	mode_wind_direction = winddata_during_sesh['WDIR'].value_counts().idxmax()


	two_days_ago = user_date - timedelta(days=2)
	average_wind_past_48 = winddata.loc[(winddata["date time"].dt.date).between(two_days_ago, user_date)]

	average_wind_speed_past_48 = average_wind_past_48["WSPD"].mean()
	mode_wind_direction_past_48 = average_wind_past_48['WDIR'].value_counts().idxmax()



	winds = []
	winds.extend(start_wind_speed, end_wind_speed, average_wind_speed, start_wind_direction, end_wind_direction, mode_wind_direction, average_wind_speed_past_48, mode_wind_direction_past_48)

	return winds