import re, json

def clean_data(entries): 
    """
    Passes in the results of the scrape.scrape_pages() function as a variable
    called 'entries.' Parses through 'entries' and reformats it into a
    dictionary. Returns a list of dictionaries called 'cleaned_entries.'
    """
    entry_counter = 1
    cleaned_entries = []

    for entry in entries:
        row_1 = entry['row_1']
        row_2 = entry['row_2']
        row_3 = entry['row_3']
        link = entry['link']

        # Parse through row_1
        university = row_1[0]
        program_and_degree = row_1[1] # needs splitting with regex
        date_added = row_1[2]
        status = row_1[3]

        # Use regex to split program and degree
        match = re.match(r'(.+?)(Masters|PhD|JD|MFA)$', program_and_degree)
        if match:
            program = match.group(1)
            degree = match.group(2)
        else:
            program = program_and_degree
            degree = ""

        # Use regex to extract the academic term.
        term_match = re.search(r'(Fall|Spring|Summer|Winter) \d{4}', row_2[0])
        term = term_match.group(0) if term_match else None

        if "International" in row_2[0]:
            origin = "International"
        elif "American" in row_2[0]:
            origin = "American"
        else:
            origin = None

        # Use regex to extract the gpa.
        gpa_match = re.search(r'GPA\s?([\d.]+)', row_2[0])
        gpa = gpa_match.group(1) if gpa_match else None

        # Use regex to extract the gpa the gre scores
        gre_general_match = re.search(r'GRE\s?(\d{2,3})', row_2[0])
        gre_general = gre_general_match.group(1) if gre_general_match else None
        gre_verbal_match = re.search(r'GRE V\s?(\d{2,3})', row_2[0])
        gre_verbal = gre_verbal_match.group(1) if gre_verbal_match else None
        gre_aw_match = re.search(r'GRE AW\s?([\d.]+)', row_2[0])
        gre_aw = gre_aw_match.group(1) if gre_aw_match else None

        cleaned_entry = {
            'program_name': program,
            'university': university,
            'comment': row_3, # row_3 in its entirety is just the comment
            'date_added': date_added,
            'url_link': link,
            'status': status,
            'term': term,
            'origin': origin,
            'degree': degree,
            'gre_general': gre_general,
            'gre_verbal': gre_verbal,
            'gpa': gpa,
            'gre_aw': gre_aw
        }
        cleaned_entries.append(cleaned_entry)
        entry_counter += 1
    
    return cleaned_entries

def save_data(entries, filename="applicant_data.json"):
    """Saves data to a file in json format."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2)

def load_data(filename="applicant_data.json"):
    """Loads json file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)