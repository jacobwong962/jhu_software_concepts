from flask import Blueprint, render_template

# Instantiates a blueprint for the Flask application
bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    """Creates the 'home' webpage from the 'home' Jinja template."""
    return render_template("pages/home.html", active_page='home')

@bp.route("/projects")
def projects():
    """Creates the 'projects' webpage from the 'projects' Jinja template."""
    return render_template("pages/projects.html", active_page='projects')

@bp.route("/contact")
def contact():
    """Creates the 'contacts' webpage from the 'contacts' Jinja template."""
    return render_template("pages/contact.html", active_page='contact')

