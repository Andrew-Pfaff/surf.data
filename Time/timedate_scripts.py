from datetime import datetime
from pkgutil import get_data
import join

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

#date in YYYY-MM-DD form
def date_dash(date1):
    dashes = date1[:4]+'-'+date1[4:6]+'-'+date1[6:]
    return dashes

def utc_convert(time):
    datetime.utcnow()
    
