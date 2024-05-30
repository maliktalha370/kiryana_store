import streamlit as st
import sqlite3

from utilities.constants import *
from sqlite3 import Error

def create_user_credentials_table(db_file):
    """Create a database connection to a SQLite database specified by db_file"""
    conn = sqlite3.connect(db_file)
    # Creating Table
    create_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        password TEXT NOT NULL
    );
    """
    try:
        c = conn.cursor()
        c.execute(create_sql)
    except Error as e:
        st.error(e)

################################# Sales DataBase ##################################33
def create_sales_db_and_tables(SALES_DB):
    connection = sqlite3.connect(SALES_DB)
    cursor = connection.cursor()

    # Create Tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
                        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        mobile_number TEXT NOT NULL UNIQUE)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        product_name TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Sales (
                        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_id INTEGER NOT NULL,
                        date_time TEXT NOT NULL,
                        discount INTEGER NOT NULL,
                        amount_paid INTEGER NOT NULL,
                        total_price INTEGER NOT NULL,
                        grand_total INTEGER NOT NULL,
                        remaining_amount INTEGER NOT NULL,
                        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS SaleItems (
                        sale_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sale_id INTEGER NOT NULL,
                        product_id INTEGER NOT NULL,
                        quantity INTEGER NOT NULL,
                        unit TEXT NOT NULL,
                        unit_price INTEGER NOT NULL,
                        total_price INTEGER NOT NULL,
                        FOREIGN KEY (sale_id) REFERENCES Sales(sale_id),
                        FOREIGN KEY (product_id) REFERENCES Products(product_id))''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    # create_user_credentials_table(USERS_DB)
    # print("USER's table created !!")
    create_sales_db_and_tables(SALES_DB)
    print("Sale's table created !!")