import sqlite3
from sqlite3 import Error
import rc_strings as rcs

def create_connection(file):
    conn = None
    try:
        conn = sqlite3.connect(file)
    except Error as e:
        print(e)
 
    return conn

def select_task(conn, task):
    cur = conn.cursor()
    cur.execute(task)
    
    return cur.fetchall()

def get_sqlite_data(file, task):
    conn = create_connection(file)
    with conn:
        data = select_task(conn, task)
        if data:
            return data
