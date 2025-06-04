import scrape, clean
import urllib3

def main():
    base_url = f"https://www.thegradcafe.com/"
    num_entries = 10
    http = urllib3.PoolManager()
    all_entries = scrape.scrape_pages(base_url, num_entries, http)

    clean.clean_data(all_entries)

if __name__ =="__main__":
    main()