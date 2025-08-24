#!/usr/bin/python3
"""
MySQLServer.py
Creates the database 'alx_book_store' if it does not already exist.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None

    try:
        # Try to connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",       # change if needed
            password="password"  # change if needed
        )

        cursor = connection.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except Error as e:
            print(f"Error: Failed to create database. {e}")

    except Error as e:
        print(f"Error: Could not connect to the MySQL server. {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
