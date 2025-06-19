"""Runs the main program. Runs the Flask application."""
import app

if __name__ == "__main__":
    #instantiates a Flask application
    my_app = app.create_app()

    my_app.run(host="0.0.0.0", port=8080, debug=True)
