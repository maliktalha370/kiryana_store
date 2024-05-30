from utilities.constants import *
from utilities.get_db_records import *
import streamlit as st
import sqlite3
import threading
import time
from st_pages import hide_pages



def main():
    st.title('Login Page')

    if not st.session_state.get("logged_in", False):
        hide_pages(["sales_entry", "search_panel", "Add_Product", "register"])
        with st.form('Login Form'):
            username = st.text_input('Username')
            password = st.text_input('Password', type='password')
            login_button = st.form_submit_button('Login')

        # Move the navigation button outside the form
        if login_button:
            conn = sqlite3.connect(USERS_DB)
            user = check_user(conn, username, password)
            if user:
                st.session_state["logged_in"] = True
                hide_pages(['login_page'])
                st.success("Logged in!")
                time.sleep(0.5)
                st.switch_page("pages/sales_entry.py")
            else:
                st.error('Incorrect Username/Password')

        if st.button('Go to Register Page'):
            # st.session_state['page'] = 'register'
            st.switch_page("pages/register_page.py")
            st.rerun()

main()
