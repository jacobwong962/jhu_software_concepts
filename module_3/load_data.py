import json
import psycopg2
from datetime import datetime

def load_json_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def create_connection():
    return psycopg2.connect(
        dbname="gradcafe",
        user="postgres",
        password="POGI",
        host="localhost",
        port="5432"
    )
        
def create_table(connection):
    with connection.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS applicants (
                p_id SERIAL PRIMARY KEY,
                program TEXT,
                comments TEXT,
                date_added DATE,
                url TEXT,
                status TEXT,
                term TEXT,
                us_or_international TEXT,
                gpa FLOAT,
                gre FLOAT,
                gre_v FLOAT,
                gre_aw FLOAT,
                degree TEXT
            )"""
        )
        connection.commit()
        print("Table created successfully.")

def _try_float(val):
    try:
        return float(val)
    except (TypeError,ValueError):
        return None

def _parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%B %d, %Y").date()
    except Exception:
        return None

def transform_entry(entry):
    return {"program": f"{entry.get('university')} - {entry.get('program_name')}",
            "comments": entry.get('comment'),
            "date_added": _parse_date(entry.get('date_added')),
            "url": entry.get('url_link'),
            "status": entry.get('status'),
            "term": entry.get('term'),
            "us_or_international": entry.get('origin'),
            "gpa": _try_float(entry.get('gpa')),
            "gre": _try_float(entry.get('gre_general')),
            "gre_v": _try_float(entry.get('gre_verbal')),
            "gre_aw": _try_float(entry.get('gre_aw')),
            "degree": entry.get('degree'),
    }

def insert_entry(cur, entry):
    insert_query = """
    INSERT INTO applicants (
        program, comments, date_added, url, status, term,
        us_or_international, gpa, gre, gre_v, gre_aw, degree
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        entry["program"],
        entry["comments"],
        entry["date_added"],
        entry["url"],
        entry["status"],
        entry["term"],
        entry["us_or_international"],
        entry["gpa"],
        entry["gre"],
        entry["gre_v"],
        entry["gre_aw"],
        entry["degree"]
    )
    cur.execute(insert_query, values)

def clear_table(conn):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM applicants")
    conn.commit()

if __name__ == "__main__":
    connection = create_connection()
    create_table(connection)
    clear_table(connection)
    raw_entries = load_json_data('applicant_data.json')
    with connection.cursor() as cur:
        for raw_entry in raw_entries:
            entry = transform_entry(raw_entry)
            insert_entry(cur,entry)
        connection.commit()
    connection.close()