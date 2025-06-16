# Name: Jacob Wong (jwong86)

# Module 4 Assignment 
## Pytest and Sphinx due on 06/17/2025 at 11:59 EST

# How to Launch Flask Application:
1. Clone the repository from Github and make it your current directory in your terminal.
2. Set up the virtual enviroment using:
    python -m venv venv
    venv\Scripts\activate (for Windows)
3. Install software from requirements.txt
    pip install -r requirements.txt
4. Run app using: $python app.py
5. Open a web browser and visit 'http://localhost:8000' into the URL search bar.

# Approach:

My approach to this assignment was to organize my code into 3 Python modules:
- load_data.py
- query_data.py
- app.py

## load_data.py:
There are 8 user defined functions in load_data.py:
- load_json_data(): Loads the GradCafe applicant data from a JSON file and returns it as a list of dictionaries.
- create_connection(): Establishes a connection to the local PostgreSQL database using the psycopg2 library.
- create_table(): Uses a SQL command to create a PostgreSQL table called 'applicants', if it doesn't already exist.
- _try_float(): Attempts to convert a value to a float; returns None if conversion fails (I made this function over using the built-in float() function because if a value is NoneType, float() raises an error).
- _parse_date(): Converts date strings into datetime.date objects. Returns None on failure.
- transform_entry(): Transforms each entry into a cleaned dictionary matching the correct format.
- insert_entry(): Executes an SQL INSERT INTO query to insert a new entry into the table.
- clear_table(): Deletes all data from the applicants table. Used to avoid duplicating entries in the table if running the script more than once.


## query_data.py:
There are 7 user defined functions in query_data(). Each function executes a SQL query to pull information from the PostgreSQL data base. The functions are organized with a corresponding Analysis Question from this week's assignment.

## app.py:
When run, it creates a Flask application to display the results of my queries from query_data.py. It utilizes blueprints and templates to create a single page site that displays my answers for each of the Analysis Questions.



# Known Bugs:
None