import mysql.connector
from mysql.connector import Error
from geopy.distance import geodesic

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


def get_airport_data(cursor, icao_code):
    """Helper function to fetch airport name and coordinates by ICAO code."""
    query = "SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(query, (icao_code,))
    return cursor.fetchone()


def calculate_airport_distance():
    print("--- Airport Distance Calculator ---")

    # Prompt user for both ICAO codes and normalize to uppercase
    icao1 = input("Enter the first airport ICAO code: ").strip().upper()
    icao2 = input("Enter the second airport ICAO code: ").strip().upper()

    if not icao1 or not icao2:
        print("Both ICAO codes must be provided.")
        return

    connection = None
    cursor = None
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = connection.cursor()

        # Fetch first airport info
        airport1 = get_airport_data(cursor, icao1)
        if not airport1:
            print(f"Airport with ICAO code '{icao1}' was not found in the database.")
            return

        # Fetch second airport info
        airport2 = get_airport_data(cursor, icao2)
        if not airport2:
            print(f"Airport with ICAO code '{icao2}' was not found in the database.")
            return

        name1, lat1, lon1 = airport1
        name2, lat2, lon2 = airport2

        # Ensure coordinates exist
        if lat1 is None or lon1 is None or lat2 is None or lon2 is None:
            print("Error: Missing coordinate data for one or both airports.")
            return

        # Define coordinates as (latitude, longitude) tuples
        coord1 = (lat1, lon1)
        coord2 = (lat2, lon2)

        # Calculate distance using geopy's geodesic function
        distance_km = geodesic(coord1, coord2).kilometers

        # Print out the results clearly
        print(f"\n--- Distance Result ---")
        print(f"Airport 1: {name1} ({icao1})")
        print(f"Airport 2: {name2} ({icao2})")
        print(f"Distance: {distance_km:.2f} km")

    except Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Clean up database resources
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    calculate_airport_distance()