from enum import nonmember

import mysql.connector
from mysql.connector import Error

# MySQL / MariaDB Connection Parameters
MYSQL_CONFIG = {
    "host": "127.0.0.1",           # Server hostname or IP
    "port": 3306,                  # MySQL port
    "database": "db_flight_game",  # Target database name
    "user": "root",                # SQL username
    "password": "Hoang",           # SQL password
    "autocommit": True,
    "connection_timeout": 3
}


def fetch_airport_info():
    # Prompt user for ICAO code and normalize to uppercase
    icao_code = input("Enter the ICAO code of an airport: ").strip().upper()
    if not icao_code:
        print("ICAO code cannot be empty.")
        return

    connection = None
    cursor = None

    try:
        # Establish connection to the MySQL database
        connection = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = connection.cursor()

        # Query the airport table using parameterized query to prevent SQL injection
        query = "SELECT name, municipality FROM airport WHERE ident = %s"
        cursor.execute(query, (icao_code,))

        result = cursor.fetchone()

        if result:
            name, municipality = result
            print(f"ICAO Code: {icao_code}")
            print(f"Name: {name}")
            print(f"Location (Municipality): {municipality if municipality else 'N/A'}")
        else:
            print(f"\nNo airport found with ICAO code '{icao_code}'.")

    except Error as e:
        print(f"Database connection or query error: {e}")

    finally:
        # Clean up database resources
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    fetch_airport_info()
