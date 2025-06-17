"""
This module uses SQL queries to answer the seven analysis questions from the
module 3 assignment.
"""
from psycopg2 import sql
from load_data import create_connection

def question_1(connection):
    """Queries the SQL database to solve Question 1 from the assignment."""
    with connection.cursor() as cur:
        statement = sql.SQL("""
            SELECT COUNT(*)
            FROM {table}
            WHERE term = {term}
            LIMIT 1
        """).format(
            table = sql.Identifier("applicants"),
            term = sql.Literal("Fall 2025")
        )
        cur.execute(statement)
        return cur.fetchone()[0]

def question_2(connection):
    """Queries the SQL database to solve Question 2 from the assignment."""
    with connection.cursor() as cur:
        # Finds the total number of international applicants.
        statement_1 = sql.SQL("""
            SELECT COUNT(*) FROM {table}
            WHERE us_or_international = {us_or_international}
            LIMIT 1
        """).format(
            table = sql.Identifier("applicants"),
            us_or_international = sql.Literal('International')
        )
        cur.execute(statement_1)
        international = cur.fetchone()[0]

        # Finds the total number of applicants.
        statement_2 = sql.SQL("""
            SELECT COUNT(*) FROM {table}
            LIMIT 1
        """).format(
            table = sql.Identifier("applicants")
        )
        cur.execute(statement_2)
        total = cur.fetchone()[0]
        return round(international/total*100,2)

def question_3(connection):
    """Queries the SQL database to solve Question 3 from the assignment."""
    with connection.cursor() as cur:
        statement = sql.SQL("""
            SELECT
                AVG(gpa),
                AVG(gre),
                AVG(gre_v),
                AVG(gre_aw)
            FROM {table}
            WHERE
                gpa BETWEEN 0 AND 4.3 AND
                gre BETWEEN 130 AND 170 AND
                gre_v BETWEEN 130 AND 170 AND
                gre_aw BETWEEN 0 AND 6
            LIMIT 1
        """).format(
            table=sql.Identifier("applicants")
        )
        cur.execute(statement)
        result = cur.fetchone()
        return tuple(round(val, 2) if val is not None else None for val in result)

def question_4(connection):
    """Queries the SQL database to solve Question 4 from the assignment."""
    with connection.cursor() as cur:
        statement = sql.SQL("""
            SELECT AVG(gpa) FROM {table}
            WHERE
                us_or_international = {us_or_international}
                AND term = {term}
            LIMIT 1
        """).format(
            table = sql.Identifier("applicants"),
            us_or_international = sql.Literal("American"),
            term = sql.Literal("Fall 2025")
        )
        cur.execute(statement)
        return round(cur.fetchone()[0],2)

def question_5(connection):
    """Queries the SQL database to solve Question 5 from the assignment."""
    with connection.cursor() as cur:
        # Counts the total number of Fall 2025 applicants
        statement_1 = sql.SQL("""
            SELECT COUNT(*) from {table}
            WHERE term = {term}
            LIMIT 1
        """).format(
            table = sql.Identifier("applicants"),
            term = sql.Literal("Fall 2025")
        )
        cur.execute(statement_1)
        total = cur.fetchone()[0]

        # Counts the total number of Fall 2025 applicants that were accepted
        statement_2 = sql.SQL("""
            SELECT COUNT(*) FROM {table}
            WHERE 
                term = {term}
                AND status ILIKE '%accept%'
            LIMIT 1
        """).format(
            table = sql.Identifier("applicants"),
            term = sql.Literal("Fall 2025")
        )
        cur.execute(statement_2)
        accepted = cur.fetchone()[0]

        return round((accepted / total) * 100, 2)

def question_6(connection):
    """Queries the SQL database to solve Question 6 from the assignment."""
    with connection.cursor() as cur:
        statement = sql.SQL("""
            SELECT AVG(gpa) FROM {table}
            WHERE
                term = {term} AND
                status ILIKE '%accept%' AND
                gpa BETWEEN 0 AND 4.3
            LIMIT 1
        """).format(
            table = sql.Identifier("applicants"),
            term = sql.Literal("Fall 2025")
        )
        cur.execute(statement)
        return round(cur.fetchone()[0], 2)

def question_7(connection):
    """Queries the SQL database to solve Question 7 from the assignment."""
    with connection.cursor() as cur:
        statement = sql.SQL("""
            SELECT COUNT(*)
            FROM {table}
            WHERE
                program ILIKE '%johns hopkins%' AND
                program ILIKE '%computer science%' AND
                degree ILIKE '%master%'
            LIMIT 1
        """).format(
            table=sql.Identifier("applicants")
        )
        cur.execute(statement)
        return cur.fetchone()[0]

if __name__ == "__main__":
    db_connection = create_connection()

    result_1 = question_1(db_connection)
    print(f"Fall 2025 applicant count: {result_1}")

    result_2 = question_2(db_connection)
    print(f"Percent International: {result_2:.2f}%")

    result_3 = question_3(db_connection)
    print(f"Averages: GPA-{result_3[0]:.2f}, GRE-{result_3[1]:.2f}, "
          "GRE V-{result_3[2]:.2f}, GRE AW-{result_3[3]:.2f}")

    result_4 = question_4(db_connection)
    print(f"Average GPA of Americans - Fall 2025: {result_4:.2f}")

    result_5 = question_5(db_connection)
    print(f"Percent Accepted - Fall 2025: {result_5:.2f}%")

    result_6 = question_6(db_connection)
    print(f"Average GPA of Accepted - Fall 2025: {result_6:.2f}")

    result_7 = question_7(db_connection)
    print(f"JHU CS Masters Applicants: {result_7}")
