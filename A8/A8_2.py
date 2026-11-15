import mysql.connector
from mysql.connector import Error

# MySQL / MariaDB Connection Parameters
MYSQL_CONFIG = {
    "host": "127.0.0.1",  # Server hostname or IP
    "port": 3306,  # MySQL port
    "database": "db_flight_game",  # Target database name
    "user": "root",  # SQL username
    "password": "Hoang",  # SQL password
    "autocommit": True,
    "connection_timeout": 3
}


def show_airports_by_type():
    country_code = input("Please enter area code (e.g., FI): ").strip().upper()
    if not country_code:
        print("Area code cannot be empty.")
        return

    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = connection.cursor()

        # Query to count airports grouped by type for the given country code
        query = """
            SELECT type, COUNT(*) 
            FROM airport 
            WHERE iso_country = %s 
            GROUP BY type 
            ORDER BY COUNT(*) DESC
        """
        cursor.execute(query, (country_code,))

        # Use fetchall() since we expect multiple rows (one for each airport type)
        results = cursor.fetchall()

        if results:
            print(f"\n--- Airports in '{country_code}' by Type ---")
            for airport_type, count in results:
                print(f"Country {country_code} has {count} {airport_type}(s)")
        else:
            print(f"\nNo airports found for country code '{country_code}'.")

    except Error as e:
        print(f"Database error: {e}")

    finally:
        # Clean up database resources
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    show_airports_by_type()