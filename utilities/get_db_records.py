import hashlib
import sqlite3
from utilities.constants import *

def get_customer_sales(customer_id):
    connection = sqlite3.connect('sales_db.sqlite')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Sales WHERE customer_id=?''', (customer_id,))
    sales = cursor.fetchall()
    connection.close()
    return sales

def get_products():
    connection = sqlite3.connect(SALES_DB)
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Products''')
    products = cursor.fetchall()
    connection.close()
    return [p[1] for p in products]

# Function to fetch customer data based on mobile number
def get_customer_data(mobile_number):
    conn = sqlite3.connect(SALES_DB)
    c = conn.cursor()

    # Query to get customer data (adapt fields and table names to match your schema)
    c.execute('''
        SELECT c.name, SUM(s.grand_total), SUM(s.remaining_amount) 
        FROM Customers c 
        JOIN Sales s ON c.customer_id = s.customer_id 
        WHERE c.mobile_number = ? 
        GROUP BY c.name
    ''', (mobile_number,))

    data = c.fetchone()
    conn.close()
    return data


def get_last_10_sales(mobile_number):
    # Connect to your SQLite database
    conn = sqlite3.connect(SALES_DB)
    c = conn.cursor()

    # Prepare the SQL query. Adjust according to your database schema
    query = '''
    SELECT s.date_time, s.total_price, s.amount_paid, s.remaining_amount
    FROM Sales s
    JOIN Customers c ON s.customer_id = c.customer_id
    WHERE c.mobile_number = ?
    ORDER BY s.date_time DESC
    LIMIT 10
    '''

    # Execute the query and fetch the results
    c.execute(query, (mobile_number,))
    results = c.fetchall()

    # Close the connection
    conn.close()

    return results

def check_user(conn, username, password):
    hash_password = hashlib.md5(password.encode()).hexdigest()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hash_password))
    user = cursor.fetchone()
    return user