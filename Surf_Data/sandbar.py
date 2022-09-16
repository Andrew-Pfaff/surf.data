import requests
import json
import pandas 
from datetime import *
from time import *
import wget
import urllib.request
from datetime import *
import sessiontime as st



def sandbar(day_time):
	user_date = st.getdate()

	user_date = datetime.strptime(user_date, '%Y-%m-%d')


	url = 'https://www.ndbc.noaa.gov/data/realtime2/46053.spec'
	response = urllib.request.urlopen(url)
	swell_data=pandas.read_fwf(response)


	swell_data = swell_data[swell_data.WVHT != "m"]
	swell_data['WVHT'] = swell_data['WVHT'].astype(float)
	swell_data = swell_data[swell_data.WVHT >= 1.83]

	swell_data['datetime'] =  pandas.to_datetime(swell_data["#YY"] + "/" + swell_data["MM"] + "/" + swell_data["DD"] + " " + swell_data["hh"] + ":" + swell_data["mm"])

	#swell_data = swell_data.set_index('datetime')

	last_swell_data = swell_data.tail(1)










	rainurl = 'https://www.ncei.noaa.gov/data/global-summary-of-the-day/access/2022/99834099999.csv'

	raindata = pandas.read_csv(rainurl)
	
	raindata['DATE'] =  pandas.to_datetime(raindata["DATE"])


	raindata = raindata[raindata.PRCP >= 1]

	last_raindata = raindata.tail(1)






	days_since_last_rain = user_date - last_raindata['DATE']

	days_since_last_swell = user_date - last_swell_data['datetime']

	barstats = []
	barstats.extend((days_since_last_swell, days_since_last_rain))
	return barstats