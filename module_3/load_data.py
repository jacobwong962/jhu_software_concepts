import json
import psycopg2

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

def transform_entry(entry):
    return {"program": f"{entry.get('university')} - {entry.get('program_name')}",
            "comments": entry.get('comment'),
            "date_added": entry.get('date_added'),
            "url": entry.get('url_link'),
            "status": entry.get('status'),
            "term": entry.get('term'),
            "us_or_international": entry.get('origin'),
            "gpa": float(entry.get('gpa')),
            "gre": float(entry.get('gre_general')),
            "gre_v": float(entry.get('gre_verbal')),
            "gre_aw": float(entry.get('gre_aw')),
            "degree": entry.get('degree'),
    }



if __name__ == "__main__":
    connection = create_connection()
    create_table(connection)