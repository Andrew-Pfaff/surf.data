import requests
import json
import pandas 
from datetime import *
from time import *
import wget
import urllib.request

import sessiontime as st
#-TIDE-

#correct url for the date and time





testoufile = {
 "queryCost": 25,
 "latitude": 34.4357,
 "longitude": -119.825,
 "resolvedAddress": "Goleta, CA, United States",
 "address": "goleta",
 "timezone": "America/Los_Angeles",
 "tzoffset": -7,
 "days": [
  {
   "datetime": "2022-08-03",
   "datetimeEpoch": 1659423600,
   "windgust": 15,
   "windspeed": 17.2,
   "winddir": 238.1,
   "hours": [
    {
     "datetime": "12:00:00",
     "datetimeEpoch": 1659466800,
     "windgust": 6.7,
     "windspeed": 10.3,
     "winddir": 250
    },
    {
     "datetime": "13:00:00",
     "datetimeEpoch": 1659470400,
     "windgust": 8.1,
     "windspeed": 12.8,
     "winddir": 270
    },
    {
     "datetime": "14:00:00",
     "datetimeEpoch": 1699470400,
     "windgust": 8.9,
     "windspeed": 3.8,
     "winddir": 270
    },
    {
     "datetime": "15:00:00",
     "datetimeEpoch": 1259470400,
     "windgust": 1.1,
     "windspeed": 19.8,
     "winddir": 277
    }
   ]
  }
 ]
}
with open("sample.json", "w") as outfile:
    json.dump(testoufile, outfile)










start_time = st.start_time()
end_time = st.end_time() 
date = st.getdate()




#format date and time user input into datetime format
user_start_datetime = datetime.strptime(date + " " + start_time, '%Y-%m-%d %H:%M')
user_end_datetime = datetime.strptime(date + " " + end_time, '%Y-%m-%d %H:%M')

user_start_time = user_start_datetime.time()
user_end_time = user_end_datetime.time()

user_date = user_start_datetime.date()



land_response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/goleta/" + date + "/" + date + "?unitGroup=us&elements=datetime%2Cwindspeed%2Cwinddir&include=hours&key=XARWQVQ3JNLRBEF53B2CA8M7E&contentType=json")

land_response = land_response.json()





land_response = (land_response['days'][0]['hours'])

land_response_data = pandas.DataFrame.from_records(land_response)

land_response_data['windspeed'] = land_response_data['windspeed'].astype(float)


land_response_data['datetime'] =  pandas.to_datetime(land_response_data["datetime"])



#land_response_data = land_response_data[land_response_data['datetime'].dt.date == user_date]
	

land_response_data = land_response_data.set_index('datetime')


land_response_data_during_sesh = land_response_data.between_time(user_start_time, user_end_time)







land_average_wind_speed = land_response_data_during_sesh["windspeed"].mean()
land_average_wind_speed = round(land_average_wind_speed, 2)



land_start_wind_direction = land_response_data_during_sesh['winddir'].iat[0]
land_end_wind_direction = land_response_data_during_sesh['winddir'].iat[-1]


land_mode_wind_direction = land_response_data_during_sesh['winddir'].value_counts().idxmax()