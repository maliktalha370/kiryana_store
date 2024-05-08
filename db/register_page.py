# register_page.py
import streamlit as st
import sqlite3
import hashlib

from utilities.constants import *


def insert_user(conn, username, password):
    hash_password = hashlib.md5(password.encode()).hexdigest()
    conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hash_password))
    conn.commit()


def main():
    st.title('Register New User')

    with st.form('Register Form'):
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        register_button = st.form_submit_button('Register')

        if register_button:
            conn = sqlite3.connect(USERS_DB)
            insert_user(conn, username, password)
            st.success(f'User {username} registered successfully!')
            conn.close()

            st.session_state['page'] = 'login'
            st.experimental_rerun()
    if st.sidebar.button("Logout"):
        st.session_state.clear()  # Clear session state upon logout
        st.switch_page('login_page.py')

if 'page' not in st.session_state:
    st.session_state.page = 'register'

if st.session_state.page == 'register':
    main()