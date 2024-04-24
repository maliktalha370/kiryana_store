import streamlit as st
import datetime
# Assuming the utility functions are correctly defined in your utilities package
from utilities.get_db_records import *
from utilities.add_db_records import *
from utilities.utils import *

def reset():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()
def main():
    st.title("Customer Sales Record")
    now = datetime.datetime.now()
    date_time = now.strftime('%Y-%m-%d %H:%M:%S')

    # Initialize session states for message display and timestamp
    if 'show_message' not in st.session_state:
        st.session_state.show_message = False
    if 'message_time' not in st.session_state:
        st.session_state.message_time = datetime.datetime.now()

    customer_mobile = st.text_input('Enter Customer Mobile Number:', key="input")

    if customer_mobile:
        # Fetching the last 10 sales records
        sales_records = get_last_10_sales(customer_mobile)

        if sales_records:
            st.write(f"Last 10 sales records for mobile number: **{customer_mobile}**")
            # Use a dataframe or a table to display the records nicely
            for idx, record in enumerate(sales_records, start=1):
                st.text(
                    f"{idx}. Date: {record[0]}, Total Price: {record[1]}, Amount Paid: {record[2]}, Remaining Amount: {record[3]}")
        else:
            st.write("No sales record found for the given mobile number.")

        record = get_customer_data(customer_mobile)

        if record:
            st.sidebar.write(f"Name: **{record[0]}**", key="name")
            st.sidebar.write(f"Total Sales: **Rs {record[1]:.2f}**", key="sales")
            st.sidebar.write(f"Udhaar: **Rs {record[2]:.2f}**", format="%d", step=1, key="udhaar")
            wasooli = st.sidebar.number_input("**Wasooli**", format="%d", step=1, key="wasooli")
            customer_id = search_customer(customer_mobile)
            wasooli = -1 * wasooli
            if customer_id is None:
                st.error('Alert! Customer ID not found')
            else:
                if st.sidebar.button("Submit Wasooli"):
                    add_sale(customer_id, date_time, 0, 0, 0, 0, wasooli)
                    reset()
        else:
            st.write("No record found for the given mobile number.")


