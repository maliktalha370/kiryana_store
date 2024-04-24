from utilities.constants import *
import streamlit as st
import sqlite3
import hashlib

def check_user(conn, username, password):
    hash_password = hashlib.md5(password.encode()).hexdigest()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hash_password))
    user = cursor.fetchone()
    return user


def main():
    st.title('Login Page')

    with st.form('Login Form'):
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        login_button = st.form_submit_button('Login')

    # Move the navigation button outside the form
    if login_button:
        conn = sqlite3.connect(USERS_DB)
        user = check_user(conn, username, password)
        if user:
            print('Log In Successful !')
            st.session_state['logged_in'] = True
            st.session_state['page'] = 'success'
            st.experimental_rerun()
        else:
            st.error('Incorrect Username/Password')

    if st.button('Go to Register Page'):
        st.session_state['page'] = 'register'
        st.experimental_rerun()

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'page' not in st.session_state:
    st.session_state['page'] = 'login'

# The main login logic
if st.session_state.page == 'login' and not st.session_state.logged_in:
    main()

# Redirect to registration page logic
elif st.session_state.page == 'register':
    st.experimental_memo.clear()
    st.experimental_singleton.clear()
    exec(open('register_user.py').read())

# This block will only be executed if the user is successfully logged in
# Redirection handling; move this block right before the last line of the script.
if 'logged_in' in st.session_state and st.session_state['logged_in'] and st.session_state['page'] == 'success':
    print('INSIDE !!!')
    exec(open('option_selection.py').read())