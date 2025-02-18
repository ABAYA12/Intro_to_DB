import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Update with your MySQL username
            password=''   # Update with your MySQL password
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_BOOK_STORE")
            print("Database 'ALX_BOOK_STORE' created successfully!")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()