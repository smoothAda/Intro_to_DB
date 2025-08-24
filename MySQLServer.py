import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (replace with your credentials)
    connection = mysql.connector.connect(
        host='localhost',       # or your server host
        user='your_username',   # MySQL username
        password='your_password' # MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close cursor and connection
    if 'cursor' in locals() and cursor.is_connected() == False:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
