#import sqlite3
import mysql.connector as mysql

import click
from flask import current_app, g
from flask.cli import with_appcontext

MYSQL_DATABASE_USER='root'
MYSQL_DATABASE_PASSWORD='root'
MYSQL_DATABASE_DB='blog'
MYSQL_DATABASE_HOST='db'

def get_db():
    if 'db' not in g:
        g.db = mysql.connect(
            user=MYSQL_DATABASE_USER,
            database=MYSQL_DATABASE_DB,
            password=MYSQL_DATABASE_PASSWORD,
            host=MYSQL_DATABASE_HOST,
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
