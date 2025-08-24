
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
    )

    if mydb.is_connected():
        cursor = mydb.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        cursor.execute(sql)
        print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as e:
    print(f"Can't connect bc of: {e}")

finally:
    if mydb.is_connected():
        cursor.close();
        mydb.close()