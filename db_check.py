import sqlite3
from sqlite3 import Error

def create_table(conn):
    create_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
    """
    try:
        c = conn.cursor()
        c.execute(create_sql)
    except Error as e:
        print(f'Exception as {e}')
def create_connection(db_file):
    """Create a database connection to a SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f'Exception as {e}')

    return conn

if __name__=='__main__':
    conn = create_connection('users.db')
    if conn is not None:
        create_table(conn)
