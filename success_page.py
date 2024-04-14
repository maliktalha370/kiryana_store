import streamlit as st


def show_success_message():
    # Creating a full-page container
    container = st.container()

    # Calculate the columns for center alignment
    left_column, center_column, right_column = container.columns([1, 2, 1])

    # Using the middle column to display the message
    with center_column:
        # Display a success message
        st.markdown("<h1 style='text-align: center;'>Login Successful!</h1>", unsafe_allow_html=True)
