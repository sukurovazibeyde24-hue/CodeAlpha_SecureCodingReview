import os
import sqlite3
import json
import bcrypt
import ast

SECRET_KEY = os.getenv("SECRET_KEY")

def login(username, password):
    conn = sqlite3.connect("db.sqlite")
    row = conn.execute("SELECT pass FROM users WHERE name=?", (username,)).fetchone()
    return row and bcrypt.checkpw(password.encode(), row[0])

def save_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def calculate(expr):
    return ast.literal_eval(expr)

def load_data(data):
    return json.loads(data)
