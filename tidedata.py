import requests
from datetime import datetime
from xml.etree import ElementTree
import xmltodict
import json


#-INPUTS-

#date
#form YYYYMMDD
def getdate():
    print('Input the date in form YYYYMMDD or input "t" for todays date.')
    Error = True
    while Error == True:
        dayin = input('Date: ')
        dayin = str(dayin)
        inputlen = len(dayin)
        if dayin == 't' or day == 'T':
            now = datetime.now()
            day = now.strftime("%Y%m%d")
            Error = False
        elif inputlen != 8:
            print('Error. String not the right length. Make sure you are inputting the date in the form YYYYMMDD. For example for April 9th, 2021, you would input "20210421".')
        elif inputlen == 8:
            day = dayin
            Error = False
    return day

#start time
def start_time():
    print('Input the start time in the format HH:MM in 24 hour time (for example 8:06AM = 08:06 and and 8:06PM = 20:06PM).')
    stimein = input('Start Time: ')
    stime = stimein
    return stime

#end time
def end_time():
    print('Input the end time in the format HH:MM in 24 hour time (for example 8:06AM = 08:06 and and 8:06PM = 20:06PM).')
    etimein = input('End Time: ')
    etime = etimein
    return etime


#-TIDE-

#correct url for the date and time
day = getdate()
stime = start_time()
etime = end_time()
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