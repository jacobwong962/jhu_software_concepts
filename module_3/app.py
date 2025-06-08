import psycopg2
from flask import Flask, render_template
import load_data
from query_data import (question_1,question_2,question_3,question_4,question_5,
                        question_6,question_7)

app = Flask(__name__)

@app.route('/')
def index():
    conn = load_data.create_connection()
    analysis_results = {
        "fall_2025_count": question_1(conn),
        "intl_percent": question_2(conn),
        "averages": question_3(conn),
        "avg_gpa_american": question_4(conn),
        "percent_accepted": question_5(conn),
        "avg_gpa_accepted": question_6(conn),
        "jhu_cs_masters": question_7(conn)
    }
    conn.close()
    return render_template('pages/index.html', **analysis_results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)