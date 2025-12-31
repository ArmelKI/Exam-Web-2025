from flask import Flask
import sqlite3

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cle_secrete'

def get_db_connection():
    conn = sqlite3.connect('resolutions.db')
    return conn

from routes import *

if __name__ == '__main__':
    app.run(debug=True)