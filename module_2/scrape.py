import urllib3
from bs4 import BeautifulSoup

url = "https://www.thegradcafe.com/survey/"
http = urllib3.PoolManager()
response = http.request("GET", url)

soup = BeautifulSoup(response.data, 'html.parser')
type(soup)
rows = soup.find_all("tr")[1:]

for row in rows[:5]:
    cells = row.find_all('td')