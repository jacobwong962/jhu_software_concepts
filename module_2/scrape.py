import urllib3
from bs4 import BeautifulSoup
import math

def scrape_data(url, tag, starting_tag_index = 0, http = None):
    """Scrapes raw html data from cite. Returns a list of ever <tr> element"""
    if http is None:
        http = urllib3.PoolManager()
    response = http.request("GET", url)
    soup = BeautifulSoup(response.data, 'html.parser')
    html = soup.find_all(tag)[starting_tag_index:]
    return html

def extract_text(html_rows):
    extracted_text = []
    for html_row in html_rows:
        html_cells = html_row.find_all('td')
        text_cells = [cell.get_text(strip=True) for cell in html_cells]
        if text_cells == ['']:
            continue
        extracted_text.append(text_cells)
    return extracted_text

def scrape_links(html_rows):
    scraped_links = []
    for html_row in html_rows:
        html_cells = html_row.find_all('td')
        for cell in html_cells:
            link_tag = cell.find("a", href=True)
        if link_tag and "/result/" in link_tag['href']:
            detail_url = "https://www.thegradcafe.com" + link_tag['href']
            scraped_links.append(detail_url)
    return scraped_links

def scrape_gre_scores(scraped_links,http):
    gre_scores=[]
    for link in scraped_links:
        html_elements = scrape_data(link, "span", http=http)
        text = [element.get_text(strip=True) for element in html_elements]
        gre_general = text[text.index('GRE General:')+1] if 'GRE General:' in text else None
        gre_verbal = text[text.index('GRE Verbal:')+1] if 'GRE Verbal:' in text else None
        gre_aw = text[text.index('Analytical Writing:')+1] if 'Analytical Writing:' in text else None
        gre_score = {'gre_general': gre_general,
                  'gre_verbal': gre_verbal,
                  'gre_aw': gre_aw,}
        gre_scores.append(gre_score)
    return gre_scores

def create_entries(scraped_text,scraped_links,gre_scores):
    """
    Passes in the list returned from scrape_data(). Restructures this list into
    a list of dictionaries, where each dictionary is one entry from the Grad
    Cafe website.
    """
    i = 0
    counter = 0
    entries = []
    while i < len(scraped_text) - 1:
        entry = {'row_1': scraped_text[i],
                 'row_2': scraped_text[i+1],
                 'row_3': None,
                 'link': scraped_links[counter],
                 'gre_score': gre_scores[counter]}
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
    each page on the website in a for loop, and returns all of the """
    # The gradcafe website has 20 entries per page
    num_pages = math.ceil(num_entries/20) 

    entries = []
    for i in range(num_pages):
        url = f"{base_url}survey/?page={i+1}"
        html_rows = scrape_data(url, "tr", starting_tag_index = 1, http = http)
        scraped_text = extract_text(html_rows)
        scraped_links = scrape_links(html_rows)
        gre_scores = scrape_gre_scores(scraped_links,http)
        page_entries = create_entries(scraped_text,scraped_links,gre_scores)
        entries.extend(page_entries)
    
    entries = entries[0:num_entries]
    return entries

if __name__ =="__main__":
    http = urllib3.PoolManager()
    base_url = f"https://www.thegradcafe.com/"
    num_entries = 100
    all_entries = scrape_pages(base_url, num_entries, http)
    
    
    