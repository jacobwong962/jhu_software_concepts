import urllib3
from bs4 import BeautifulSoup

def scrape_data():
    url = "https://www.thegradcafe.com/survey/"
    http = urllib3.PoolManager()
    response = http.request("GET", url)

    soup = BeautifulSoup(response.data, 'html.parser')

    rows = soup.find_all("tr")[1:]

    scraped_data = []
    for row in rows[:100]:
        cells = row.find_all('td')
        text_cells = [cell.get_text(strip=True) for cell in cells]
        scraped_data.append(text_cells)
    
    return scraped_data

def create_entries(scraped_data):
    i = 0
    entries = []
    while i < len(scraped_data) - 1:
        entry = {'row_1':scraped_data[i],
                 'row_2':scraped_data[i+1]}
        if i+2 < len(scraped_data) and len(scraped_data[i+2]) == 1:
            entry['row_3'] = scraped_data[i+2]
            i += 1
        entries.append(entry)
        i += 2
        print(entry)
        print('##################################')
    return(entries)

if __name__ =="__main__":
    scraped_data = scrape_data()
    entries = create_entries(scraped_data)
    