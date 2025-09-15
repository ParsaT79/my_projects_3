import sqlite3


def create_table():
    connection = sqlite3.connect("data_access/practice_3_b.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users
                      (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          username TEXT,
                          password TEXT,
                          nickname TEXT,
                          account_access INTEGER
                      )
                   """)
    connection.commit()
    connection.close()


def save_user(username, password, nickname, account_access):
    connection = sqlite3.connect("data_access/practice_3_b.db")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO users (username, password, nickname, account_access) VALUES (?, ?, ?, ?)""",
                   (username, password, nickname, account_access))
    connection.commit()
    connection.close()
