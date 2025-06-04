## Name: Jacob Wong (jwong86)

## Module 2 Assignment 
# Web Scraping due on 06/03/2025 at 11:59 EST (granted 48hr extension by Liv)


## Approach:

My approach to this assignment was to organize my code into 3 Python modules:
- scrape.py
- clean.py
- main.py

# scrape.py:
There are 5 user defined functions in scrape.py:
- scrape_data(): This function performs an http GET request utilizing the urllib3 library. It then scrapes raw html data from site using BeautifulSoup. Finally, it returns a list of every html element of the specified tag using the BeautifulSoup.find_all() method.

- _extract_text(): This private function removes html tags and leaves only the text. Returns a list called 'extracted_text.'

- _extract_links(): This private function uses the search() function to parse through the data and find the link to each entry's dedicated webpage. Saves the links to a list called 'extracted_links.'
- _create_entries(): Passes in the lists returned from extract_text() and extract_links(). It restructures this data into a list of dictionaries, where each dictionary represents one entry on the Grad Cafe's website. 
- scrape_pages(): Passes in the desired number of entries needed to be scrape from the Grad Cafe's website. Calculates the total number of pages that must be scraped. Scrapes each page on the website utilizing a for loop, and returns all entries in a single list called all_entries.

# clean.py:
There are 5 user defined functions in scrape.py:
- clean_data(): This function passes in the results of the scrape.scrape_pages() function as a variable called 'entries.' Parses through 'entries' and reconstructs it into a new dictionary called 'cleaned_entry' with the required format. Returns a list of dictionaries called 'cleaned_entries.'
- save_data(): Saves the results of clean_data() to a json file using the json.dump() method.
- load_data(): Loads a json file and returns the contents of the file.

# main.py:
The main program. It instantiates the urllib3.PoolManager() object that we send http requests to. It scrapes 10,000 entries from the grad cafe website, cleans up the data, and saves it to a json file. 

# Additional files in this package include:
- README.md
- requirements.txt
- screenshot.jpg (a screenshot of the Grad cafe's robot.txt file)
- applicant_data.json (the resulting file of this assignment containing 10,000 entries from the Grad Cafe's website.)


## Known Bugs:
None