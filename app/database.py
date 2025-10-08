import sqlite3
from flask import g


DATABASE = 'users.db'


def get_db():
db = getattr(g, '_database', None)
if db is None:
db = g._database = sqlite3.connect(DATABASE)
db.row_factory = sqlite3.Row
return db


def close_db(exception=None):
db = getattr(g, '_database', None)
if db is not None:
db.close()


def init_db():
db = get_db()
db.execute('''
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE NOT NULL,
password TEXT NOT NULL,
is_admin INTEGER DEFAULT 0
)
''')
db.commit()


def query_db(query, args=(), one=False):
cur = get_db().execute(query, args)
rv = cur.fetchall()
cur.close()
return (rv[0] if rv else None) if one else rv
