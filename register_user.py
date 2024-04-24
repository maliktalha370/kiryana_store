import hashlib

import streamlit as st
import sqlite3

from utilities.constants import *
from sqlite3 import Error

# Function to create a connection to the SQLite database
def create_connection(db_file):
    """Create a database connection to a SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        st.error(e)

    return conn

# Function to create a table (if it doesn't exist)
def create_table(conn):
    create_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,  -- Added UNIQUE constraint to enforce uniqueness
        name TEXT NOT NULL,
        password TEXT NOT NULL
    );
    """
    try:
        c = conn.cursor()
        c.execute(create_sql)
    except Error as e:
        st.error(e)

# Function to insert a new user into the users table
def insert_user(conn, username, name, password):
    insert_sql = '''INSERT INTO users(username, name, password) VALUES(?, ?, ?)'''
    try:
        c = conn.cursor()
        c.execute(insert_sql, (username, name, password))
        conn.commit()
        return c.lastrowid
    except sqlite3.IntegrityError as e:  # Catch IntegrityError for duplicate username
        st.error("Username already exists. Please choose a different username.")
        return None
    except Error as e:
        st.error(e)
        return None

# Function to check if a username already exists
def check_username_exists(conn, username):
    select_sql = '''SELECT id FROM users WHERE username = ?'''
    try:
        c = conn.cursor()
        c.execute(select_sql, (username,))
        row = c.fetchone()
        if row:
            return True  # Username exists
        else:
            return False  # Username doesn't exist
    except Error as e:
        st.error(e)
        return False

# Initialize database connection and table
conn = create_connection(USERS_DB)
if conn is not None:
    create_table(conn)

# Streamlit UI
st.title('User Registration')

with st.form("user_registration_form", clear_on_submit=True):
    username = st.text_input("Username", key="username")
    name = st.text_input("Name", key="email")
    password = st.text_input("Password", type="password", key="password")
    hash_password = hashlib.md5(password.encode()).hexdigest()
    submit_button = st.form_submit_button("Register")

    if submit_button:
        if check_username_exists(conn, username):
            st.error("Username already exists. Please choose a different username.")
        else:
            user_id = insert_user(conn, username, name, hash_password)
            if user_id:
                st.success(f"User {username} registered successfully with ID {user_id}")

if conn:
    conn.close()
