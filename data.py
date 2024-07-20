#coding=utf-8
import sqlite3

def create_datatable():
    connection = sqlite3.connect('data.db', timeout=20)
    cur = connection.cursor()

    query = '''
        CREATE TABLE IF NOT EXISTS users_base(
        id INTEGER,
        user_id INTEGER
        );
    '''
    cur.execute(query)
    cur.execute(
            f'INSERT INTO users_base VALUES(0, 0);'
        )
    connection.commit()
    connection.close()

def content_num():
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    query = f'SELECT user_id FROM users_base WHERE id = 0'
    results = cur.execute(query).fetchone()
    connection.close()
    if results != 0:
        return results[0]
    else:
        return

def user_reg(user_id):
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    query = f'SELECT user_id FROM users_base WHERE user_id = {user_id}'
    results = cur.execute(query).fetchone()
    if results == None:
        cur.execute(
            f'INSERT INTO users_base VALUES({content_num()+1}, {user_id});'
        )
        cur.execute(
        f'UPDATE users_base SET user_id = {content_num()}+1 WHERE id = 0;'
    )
    connection.commit()
    connection.close()

def clear_base():
    connection = sqlite3.connect('data.db')
    cur = connection.cursor()
    cur.execute('DELETE FROM users_base')
    connection.commit()
    connection.close()
