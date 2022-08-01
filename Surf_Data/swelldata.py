import pandas
import requests

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