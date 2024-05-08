import streamlit as st
from utilities.add_db_records import *


# Streamlit UI
def main():
    st.title("Add New Product")

    product_name = st.text_input("Enter Product Name:")
    if st.button("Add Product"):
        if product_name:
            add_product(product_name)
            st.success(f"Product '{product_name}' added successfully!")
        else:
            st.error("Please enter a product name.")
    if st.sidebar.button("Logout"):
        st.session_state.clear()  # Clear session state upon logout
        st.switch_page('login_page.py')
if __name__ == "__main__":
    main()
