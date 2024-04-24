import streamlit as st
import datetime
from utilities.utils import *
from utilities.constants import *
from utilities.get_db_records import *
from utilities.add_db_records import *

def add_item():
    # Functionality to add an empty product item
    st.session_state['products'].append(
        {'name': '', 'quantity': 0, 'unit': '', 'unit_price': 0, 'price': 0})

def delete_product(index):
    # Functionality to delete a product from the list
    del st.session_state['products'][index]


product_names = get_products()
print('PRODUCT NAMES ', product_names)
def main():
    st.title(TITLE)
    st.sidebar.title("Customer Details")
    # Inputs for customer details
    customer_name = st.sidebar.text_input("Name")
    customer_mobile = st.sidebar.text_input("Mobile Number")

    now = datetime.datetime.now()
    date_time = now.strftime('%Y-%m-%d %H:%M:%S')

    st.header("Enter Purchased products:")

    if 'products' not in st.session_state:
        st.session_state['products'] = []

    # Button to add new product entries
    if st.button("Add Item"):
        add_item()

    total_price = 0

    for index, product in enumerate(st.session_state['products']):
        cols = st.columns([3, 2, 3, 2, 3, 2, 2])

        with cols[0]:
            # Dynamic selection for the product name
            product['name'] = st.selectbox("Product Name", options=product_names, index=0, key=f"name{index}")
        with cols[1]:
            # Input for quantity
            product['quantity'] = st.number_input("Quantity", min_value=0, value=product['quantity'], key=f"quantity{index}")
        with cols[2]:
            # Dynamic selection for the unit
            product['unit'] = st.selectbox("Unit", options=units, index=0, key=f"unit{index}")
        with cols[3]:
            # Input for unit price
            product['unit_price'] = st.number_input("Unit Price", min_value=0, value=product['unit_price'], key=f"unit_price{index}")
        with cols[4]:
            # Calculate and display price
            product['price'] = product['quantity'] * product['unit_price']
            st.write(f"PRICE: {product['price']}")
        with cols[5]:
            if st.button("Add", key=f"add{index}"):
                add_item()
        with cols[6]:
            if st.button("Delete", key=f"del{index}"):
                delete_product(index)

        total_price += product['price']

    st.markdown(f"### Total PRICE: {total_price}")
    if total_price > 0:
        # Add a text input box for discount
        row_input = st.columns((1, 1))
        # username input at column 1
        with row_input[0]:
            # username input
            discount = st.number_input("**Discount**", min_value=0)
            grand_total = total_price - discount
        st.markdown(f"### GRAND TOTAL: {grand_total}")

        row_input = st.columns((1, 1))
        # username input at column 1
        with row_input[0]:
            # username input
            amount_paid = st.number_input("**Total Deposited**", min_value=0, value = grand_total)
            remaining_amount = grand_total - amount_paid

        if st.button("Submit Sale"):
            if len(customer_name) <= 0 or len(customer_mobile) <= 0:
                st.error('Alert! Enter Customer Name and Mobile Number')
            else:
                customer_id = add_customer(customer_name, customer_mobile)
                add_sale(customer_id, date_time, discount, amount_paid, total_price, grand_total, remaining_amount)
                generate_enhanced_bill_image(
                    TITLE,
                    customer_name,
                    customer_mobile,
                    total_price,
                    discount,
                    amount_paid,
                    remaining_amount,
                    f'bills/{customer_name}/'
                )

                print('Sales added in Database !!!')
                st.success("Sale  submitted successfully!")
                st.session_state['products'] = []
                reset_form()

if __name__ == "__main__":
    main()