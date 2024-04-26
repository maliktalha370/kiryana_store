import streamlit as st
from utilities.constants import *

def main():
    st.title(TITLE)
    st.write("Please select an option below:")

    # Define custom styles for your buttons, including color
    button_style = """
    <style>
    div.stButton > button:first-child {
        width: 300px;       /* Width of the button */
        height: 75px;       /* Height of the button */
        font-size: 20px;    /* Font size */
        color: white;       /* Text color */
        background-color: #4CAF50; /* Background color */
        border-radius: 25px; /* Rounded corners */
        border: 2px solid #4CAF50; /* Border color */
    }
    div.stButton > button:first-child:hover {
        background-color: #45a049;  /* Darker shade for hover */
    }
    </style>
    """
    # Apply the custom styles
    st.markdown(button_style, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    if col1.button("gahak"):
        st.write("You clicked 'gahak'.")
        # You can add more functionality related to 'gahak' here
        exec(open('gahak/sales_entry.py').read())



    if col2.button("Khata"):
        st.write("You clicked 'Khata'.")
        # You can add more functionality related to 'Khata' here
        exec(open('khata/search_panel.py').read())



if __name__ == "__main__":
    main()