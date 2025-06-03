import urllib3
from bs4 import BeautifulSoup
import math

def scrape_data(url):
    """Scrapes raw data from cite. Any html element with the <td> tag has its
    data stored in the list called 'scraped data.'"""
    http = urllib3.PoolManager()
    response = http.request("GET", url)

    soup = BeautifulSoup(response.data, 'html.parser')

    rows = soup.find_all("tr")[1:]

    scraped_data = []
    for row in rows:
        cells = row.find_all('td')
        text_cells = [cell.get_text(strip=True) for cell in cells]
        if text_cells == ['']:
            continue
        scraped_data.append(text_cells)
    
    return scraped_data

def create_entries(scraped_data):
    """
    Passes in the list returned from scrape_data(). Restructures this list into
    a list of dictionaries, where each dictionary is one entry from the Grad
    Cafe website.
    """
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
        #print(entry)
        #print('##################################')
    return(entries)

def scrape_pages(num_entries):
    """
    Passes in the desired number of entries we want to scrape from the Grad
    Cafe. Calculates the total number of pages that must be scraped. Scrapes
    each page on the website in a for loop, and returns all of the """
    # The gradcafe website has 20 entries per page
    num_pages = math.ceil(num_entries/20) 

    entries = []
    for i in range(num_pages):
        print(f'\n\n###########Page {i+1}############')
        url = f"{base_url}?page={i}"
        scraped_data = scrape_data(url)
        page_entries = create_entries(scraped_data)
        entries.extend(page_entries)
    
    entries = entries[0:num_entries]
    return entries

if __name__ =="__main__":
    base_url = f"https://www.thegradcafe.com/survey/"
    num_entries = 101
    all_entries = scrape_pages(num_entries)
    print(all_entries, f'\nLength of entries: {len(all_entries)}')

    
    
    