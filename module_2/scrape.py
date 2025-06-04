import urllib3
from bs4 import BeautifulSoup
import math

def scrape_data(url, tag, starting_tag_index = 0, http = None):
    """
    Performs an http GET request. Scrapes raw html data from site using
    BeautifulSoup. Returns a list of every element of the specified 'tag' from 
    the webpage.
    """
    # http object should be passed in from the main function to avoid creating
    # a new http object for every webpage.
    if http is None:
        http = urllib3.PoolManager()
    response = http.request("GET", url)
    soup = BeautifulSoup(response.data, 'html.parser')
    html = soup.find_all(tag)[starting_tag_index:]
    return html

def _extract_text(html_rows):
    """
    Removes html tags and leaves only the text. Returns a list called 
    'extracted_text.'
    """
    extracted_text = []
    for html_row in html_rows:
        html_cells = html_row.find_all('td')
        text_cells = [cell.get_text(strip=True) for cell in html_cells]
        if text_cells == ['']:
            continue
        extracted_text.append(text_cells)
    return extracted_text

def _extract_links(html_rows):
    """
    Finds link to every entry's webpage. Saves data to a list structure 
    called 'extracted_links.
    '"""
    extracted_links = []
    for html_row in html_rows:
        link_tag = html_row.find("a", href=True)
        if link_tag and "/result/" in link_tag['href']:
            detail_url = "https://www.thegradcafe.com" + link_tag['href']
            extracted_links.append(detail_url)
    return extracted_links

def _create_entries(scraped_text,scraped_links):
    """
    Passes in the lists from extract_text() and extract_links(). Restructures
    this data into dictionaries, where each dictionary represents one entry on the
    Grad Cafe's website. Returns a list of these dictionaries called 'entries.'
    """
    i = 0
    counter = 0
    entries = []
    while i < len(scraped_text) - 1:
        entry = {'row_1': scraped_text[i],
                 'row_2': scraped_text[i+1],
                 'row_3': None,
                 'link': scraped_links[counter]}
        if i+2 < len(scraped_text) and len(scraped_text[i+2]) == 1:
            entry['row_3'] = scraped_text[i+2][0]
            i += 1
        entries.append(entry)
        i += 2
        counter += 1
    return(entries)

def scrape_pages(base_url, num_entries, http):
    """
    Passes in the desired number of entries we want to scrape from the Grad
    Cafe. Calculates the total number of pages that must be scraped. Scrapes
    each page on the website in a for loop, and returns all entries in a single
    list called all_entries.
    """
    # The gradcafe website has 20 entries per page
    num_pages = math.ceil(num_entries/20) 

    all_entries = []
    for i in range(num_pages):
        url = f"{base_url}survey/?page={i+1}"
        html_rows = scrape_data(url, "tr", starting_tag_index = 1, http = http)
        scraped_text = _extract_text(html_rows)
        scraped_links = _extract_links(html_rows)
        page_entries = _create_entries(scraped_text,scraped_links)
        all_entries.extend(page_entries)
    
    all_entries = all_entries[0:num_entries]
    return all_entries


    
    
    