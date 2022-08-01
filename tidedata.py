import requests
from xml.etree import ElementTree
import xmltodict
import json

import sessiontime as st

#-TIDE-
def tide():
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
    dictlist = js['predictions']

    #pick out initial and final values out of dictionaries
    initial = dictlist[0]   #dictonary for init time
    final = dictlist[-1]    #dictonary for final time
   
    tides = []
    tides.append(initial['v'])
    tides.append(final['v'])

    return tides
