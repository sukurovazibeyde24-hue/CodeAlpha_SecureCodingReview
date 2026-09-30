import sqlite3
import pickle
import hashlib

SECRET_KEY = "admin123"

def login(username, password):
    conn = sqlite3.connect("db.sqlite")
    query = "SELECT * FROM users WHERE name='" + username + "' AND pass='" + password + "'"
    return conn.execute(query).fetchone()

def save_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def calculate(expr):
    return eval(expr)

def load_data(data):
    return pickle.loads(data)
