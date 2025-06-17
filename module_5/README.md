# Name: Jacob Wong (jwong86)

# Module 5 Assignment 
## Software Assurance due on 06/17/2025 at 11:59 EST

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

The Module 5 assignment consisted of updating the code from the Module 3 assignment using Pylint and SQL injection protections.

Each of the three python modules (app.py, load_data.py, and query_data.py) have been linted using Pylint. All three files have a 10.0/10.0 Pylint score.

Additionally, each SQL query from the Module 3 code was updated to prevent SQL injection attacks. We used SQL string composition techniques (sql.SQL) to separate the SQL statements from the SQL executables. All user inputs are now formatted with indentifiers and literals.

Lastly, we created a depdency graph for app.py using ppydeps and graphviz.

# Known Bugs:
None