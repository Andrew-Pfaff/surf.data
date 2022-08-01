import requests
from xml.etree import ElementTree
import xmltodict
import json

#-TIDE-
def tide(day_time):
    #day_time should be a list with different formats to the date and the start/end times for more information on this see that file
    
    #getting the correct url for the date and time:
    day = day_time[0]
    stime = day_time[1]
    etime = day_time[2]
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
