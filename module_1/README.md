# Personal Portfolio Website
This Flask application creates a personal portfolio website to showcase my
biography, software projects, and contact information. Creating this website
fulfills the requirements of the Module 1 Assignment.

## File Structure
module_1/<br>
│<br>
├── app/<br>              
│   └── static/<br>
│       ├── bootstrap.min.css<br>
│       ├── styles.css<br>
│       ├── images/<br>
│           └── prolfile_picture.jpg<br>
│   └── templates/<br> 
│       ├── base.html<br>
│       ├── _navigation.html<br>
│       └── pages/<br>
│           ├── home.html<br>
│           ├── projects.html<br>
│           └── contacts.html<br>
│   └── __init__.py<br>
│   └── pages.py<br>
│<br>
├── run.py<br> 
├── requirements.txt<br>     
└── README.md<br>

## Getting Started
1. Clone the repository from Github and make it your current directory in your terminal.
2. Set up the virtual enviroment using:
    python -m venv venv
    venv\Scripts\activate (for Windows)
3. Install software from requirements.txt
    pip install -r requirements.txt
4. Run app using: $python run.py
5. Open a web browser and visit 'http://localhost:8000' into the URL search bar.
