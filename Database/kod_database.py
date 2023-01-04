import sqlite3

"""
Создание базы данных
"""

def connect():
    conn =sqlite3.connect('database_new.db')
    cur =conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS database_new (temp INT, female_walk TEXT,female_sport TEXT, female_day TEXT,male_walk TEXT,male_sport TEXT, male_day TEXT)''')
    conn.commit()
    conn.close()
connect()
