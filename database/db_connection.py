import mariadb
import sys
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve connection details from environment variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_NAME = os.getenv("DB_NAME")


# Connect to the MariaDB database
def connect_to_db():
    print("Attempting to connect to the database...")
    try:
        conn = mariadb.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
        )
        print("Successfully connected to the database!")  # Success message
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        sys.exit(1)


# Example usage: Get a cursor to interact with the database
def get_cursor():
    conn = connect_to_db()
    cur = conn.cursor()
    return cur, conn


def close_connection(conn, cur=None):
    """Close the cursor and the connection."""
    try:
        if cur:
            cur.close()
        if conn:
            conn.close()
            print("Connection closed.")
    except Exception as e:
        print(f"Error closing connection: {e}")


if __name__ == "__main__":
    get_cursor()
