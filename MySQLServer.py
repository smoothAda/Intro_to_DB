#!/usr/bin/python3
"""
MySQLServer.py
Creates the database 'alx_book_store' if it does not already exist.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update with your credentials)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",       # change if needed
            password="password"  # change if needed
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: Could not connect to the database. {e}")

    finally:
        # Close resources properly
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
        except:
            pass

if __name__ == "__main__":
    create_database()
