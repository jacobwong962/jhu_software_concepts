import scrape, clean
import urllib3

def main():
    """
    The main program. Scrapes 10,000 entries from the grad cafe website,
    cleans up the data, and saves it to a json file.
    """
    base_url = f"https://www.thegradcafe.com/"
    num_entries = 10000
    http = urllib3.PoolManager()
    all_entries = scrape.scrape_pages(base_url, num_entries, http)

    cleaned_entries = clean.clean_data(all_entries)
    clean.save_data(cleaned_entries)

if __name__ =="__main__":
    main()