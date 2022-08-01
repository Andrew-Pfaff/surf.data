import requests
from xml.etree import ElementTree
import xmltodict
import json

import sessiontime as st

#-TIDE-

#correct url for the date and time
day = st.getdate()
stime = st.start_time()
etime = st.end_time()
tide_url = 'https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date='+day+'%20'+stime+'&end_date='+day+'%20'+etime+'&station=9411340&product=predictions&datum=mllw&units=english&time_zone=lst_ldt&application=web_services&format=json'

#request page
page = requests.get(tide_url)

#json
js = page.json()

#get list of dictionaries
this = js['predictions']

#pick out initial and final values out of dictionaries
initial = this[0]
final = this[-1]
init_tide = initial['v']
final_tide = final['v']

# print(init_tide)
# print(final_tide)