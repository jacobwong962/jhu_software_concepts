import psycopg2
from load_data import create_connection

def question_1(connection):
    with connection.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM applicants WHERE term = 'Fall 2025'")
        return cur.fetchone()[0]
    
def question_2(connection):
    with connection.cursor() as cur:
        cur.execute("""
            SELECT COUNT(*) FROM applicants
            WHERE us_or_international = 'International'
        """)
        international = cur.fetchone()[0]
        cur.execute("""SELECT COUNT(*) FROM applicants""")
        total = cur.fetchone()[0]
        return round(international/total*100,2)
    
def question_3(connection):
    with connection.cursor() as cur:
        cur.execute("""
            SELECT
                AVG(gpa),
                AVG(gre),
                AVG(gre_v),
                AVG(gre_aw)
            FROM applicants
            WHERE
                gpa BETWEEN 0 AND 4.3 AND
                gre BETWEEN 130 AND 170 AND
                gre_v BETWEEN 130 AND 170 AND
                gre_aw BETWEEN 0 AND 6
        """)
        result = cur.fetchone()
        return tuple(round(val, 2) if val is not None else None for val in result)
    
def question_4(connection):
    with connection.cursor() as cur:
        cur.execute("""
            SELECT
                AVG(gpa)
            FROM applicants
            WHERE
                us_or_international = 'American' AND
                term = 'Fall 2025'
        """)
        return round(cur.fetchone()[0],2)

def question_5(connection):
    with connection.cursor() as cur:
        cur.execute("""
            SELECT COUNT(*) FROM applicants
            WHERE term = 'Fall 2025'
        """)
        total = cur.fetchone()[0]

        cur.execute("""
            SELECT COUNT(*) FROM applicants
            WHERE term = 'Fall 2025' AND status ILIKE '%accept%'
        """)
        accepted = cur.fetchone()[0]

        return round((accepted / total) * 100, 2)

def question_6(connection):
    with connection.cursor() as cur:
        cur.execute("""
            SELECT AVG(gpa)
            FROM applicants
            WHERE
                term = 'Fall 2025' AND
                status ILIKE '%accept%' AND
                gpa BETWEEN 0 AND 4.3
        """)
        return round(cur.fetchone()[0], 2)

def question_7(connection):
    with connection.cursor() as cur:
        cur.execute("""
            SELECT COUNT(*)
            FROM applicants
            WHERE
                program ILIKE '%johns hopkins%' AND
                program ILIKE '%computer science%' AND
                degree ILIKE '%master%'
        """)
        return cur.fetchone()[0]

if __name__ == "__main__":
    connection = create_connection()

    result_1 = question_1(connection)
    print(f"Fall 2025 applicant count: {result_1}")

    result_2 = question_2(connection)
    print(f"Percent International: {result_2:.2f}%")

    result_3 = question_3(connection)
    print(f"Averages: GPA-{result_3[0]:.2f}, GRE-{result_3[1]:.2f}, GRE V-{result_3[2]:.2f}, GRE AW-{result_3[3]:.2f}")

    result_4 = question_4(connection)
    print(f"Average GPA of Americans - Fall 2025: {result_4:.2f}")

    result_5 = question_5(connection)
    print(f"Percent Accepted - Fall 2025: {result_5:.2f}%")

    result_6 = question_6(connection)
    print(f"Average GPA of Accepted - Fall 2025: {result_6:.2f}")

    result_7 = question_7(connection)
    print(f"JHU CS Masters Applicants: {result_7}")