import sqlite3


def Database():
    global conn, cursor
    conn = sqlite3.connect('../AdminP/data.db')
    cursor = conn.cursor()
