import sqlite3
from utilities.constants import *

def add_customer(name, mobile_number):
    connection = sqlite3.connect(SALES_DB)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Customers (name, mobile_number) VALUES (?, ?)', (name, mobile_number))
    connection.commit()
    connection.close()

def add_product(product_name):
    connection = sqlite3.connect(SALES_DB)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Products (product_name) VALUES (?)', (product_name,))

    connection.commit()
    connection.close()

def add_sale(customer_id, date_time, discount, amount_paid, total_price, grand_total, remaining_amount):
    connection = sqlite3.connect(SALES_DB)
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO Sales (customer_id, date_time, discount, amount_paid, total_price, 
                      grand_total, remaining_amount) 
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', 
                   (customer_id, date_time, discount, amount_paid, total_price, grand_total, remaining_amount))
    sale_id = cursor.lastrowid
    connection.commit()
    connection.close()
    return sale_id

def add_sale_item(sale_id, product_id, quantity, unit, unit_price):
    total_price = quantity * unit_price
    connection = sqlite3.connect(SALES_DB)
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO SaleItems (sale_id, product_id, quantity, unit, unit_price, total_price) 
                      VALUES (?, ?, ?, ?, ?, ?)''', 
                   (sale_id, product_id, quantity, unit, unit_price, total_price))
    connection.commit()
    connection.close()

def add_customer(name, mobile_number):
    print('Add Customer Called !!')
    connection = sqlite3.connect(SALES_DB)
    cursor = connection.cursor()

    # Check if customer already exists
    cursor.execute('SELECT customer_id FROM Customers WHERE mobile_number = ?', (mobile_number,))
    existing_customer = cursor.fetchone()

    if existing_customer:
        return existing_customer[0]  # Return existing customer_id

    # If new customer, insert and return new customer_id
    cursor.execute('INSERT INTO Customers (name, mobile_number) VALUES (?, ?)', (name, mobile_number))
    customer_id = cursor.lastrowid  # Get the auto-generated ID

    connection.commit()
    connection.close()

    return customer_id

def search_customer(mobile_number):
    print('Add Customer Called !!')
    connection = sqlite3.connect(SALES_DB)
    cursor = connection.cursor()

    # Check if customer already exists
    cursor.execute('SELECT customer_id FROM Customers WHERE mobile_number = ?', (mobile_number,))
    existing_customer = cursor.fetchone()

    if existing_customer:
        return existing_customer[0]  # Return existing customer_id

    else:
        return None