import sqlite3


def create_table():
    connection = sqlite3.connect("practice_3_b.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_list
                      (
                          id
                          INTEGER
                          PRIMARY
                          KEY
                          AUTOINCREMENT,
                          username
                          TEXT,
                          password
                          TEXT,
                          nickname
                          TEXT,
                          account_status
                          INTEGER
                      )
                   """)
    connection.commit()
    connection.close()


def save_user(username, password, nickname, account_status):
    connection = sqlite3.connect("practice_3_b.db")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO user_list (username, password, nickname, account_status)
                      VALUES (?, ?, ?, ?)""",
                   (username, password, nickname, account_status))
    connection.commit()
    connection.close()
