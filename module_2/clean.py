import re
def clean_data(entries):
    entry_counter = 1
    cleaned_entries = []
    for entry in entries:
        row_1 = entry['row_1']
        row_2 = entry['row_2']
        row_3 = entry['row_3']
        link = entry['link']
        gre_score = entry['gre_score']

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

        # Parse through row_2
        term_match = re.search(r'(Fall|Spring|Summer|Winter) \d{4}', row_2[0])
        term = term_match.group(0) if term_match else None

        if "International" in row_2[0]:
            origin = "International"
        elif "American" in row_2[0]:
            origin = "American"
        else:
            origin = None

        gpa_match = re.search(r'GPA\s?([\d.]+)', row_2[0])
        gpa = gpa_match.group(1) if gpa_match else None

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
            'gre_general': gre_score['gre_general'],
            'gre_verbal': gre_score['gre_verbal'],
            'gpa': gpa,
            'gre_aw': gre_score['gre_aw'],}
        
        cleaned_entries.append(cleaned_entry)
        entry_counter += 1
