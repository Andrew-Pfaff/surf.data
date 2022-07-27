from xml.dom import xmlbuilder
import requests
from bs4 import BeautifulSoup
from datetime import date
from xml.etree import ElementTree
import xmltodict
import json
import pandas

#-INPUTS-

#date

#start time

#end time


#-TIDE-

#correct url for the date
day = '20220724'
start = '10:30'
end = '11:45'
tide_url = 'https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date=20220724%2010:04&end_date=20220724%2011:55&station=9411340&product=predictions&datum=mllw&units=english&time_zone=lst_ldt&application=web_services&format=json'

#request page
page = requests.get(tide_url)

#json
js = page.json()

#get list of dictionaries
this = js['predictions']

#pick out initial and final values 
initial = this[0]
final = this[-1]
init_tide = initial['v']
final_tide = final['v']


#-SWELL-

swell_url = 'https://www.ndbc.noaa.gov/station_page.php?station=46053'

#request page
swell_page = requests.get(swell_url)
wow = pandas.read_html(swell_page.text)

print(wow[11])

# soup = BeautifulSoup(swell_page.content, 'html.parser')
# page_body = soup.body
# print(page_body)

# data = []
# table = soup.find('table', attrs={'class':'lineItemsTable'})
# table_body = table.find('tbody')

# rows = table_body.find_all('tr')