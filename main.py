import os
import requests
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def fetch_clubs():
    url = os.getenv("API_URL")
    username = os.getenv("API_USERNAME")
    password = os.getenv("API_PASSWORD")
    response = requests.get(f'{url}/clubs', auth=(username, password))
    if response.status_code == 200:
        return response.json()
    else:
        return None


# Function to connect to PostgreSQL database
def connect_to_db():
    conn = psycopg2.connect(
        dbname="api_data",
        user="user_one",
        password="password",
        host="localhost",
        port="5432"
    )
    return conn

# Function to create table
def create_table(cursor):
    # Create a list of column names and data types
    columns = {
        "club_id": "TEXT",
        "club_name": "TEXT",
        "club_membership": "TEXT",
        "number_of_holes": "TEXT",
        "address": "TEXT",
        "city": "TEXT",
        "state": "TEXT",
        "country": "TEXT",
        "postal_code": "TEXT",
        "phone": "TEXT",
        "fax": "TEXT",
        "website": "TEXT",
        "longitude": "FLOAT",
        "latitude": "FLOAT",
        "contact_name": "TEXT",
        "contact_title": "TEXT",
        "email_address": "TEXT",
        "driving_range": "TEXT",
        "putting_green": "TEXT",
        "chipping_green": "TEXT",
        "practice_bunker": "TEXT",
        "motor_cart": "TEXT",
        "pull_cart": "TEXT",
        "golf_clubs_rental": "TEXT",
        "club_fitting": "TEXT",
        "pro_shop": "TEXT",
        "golf_lessons": "TEXT",
        "caddie_hire": "TEXT",
        "restaurant": "TEXT",
        "reception_hall": "TEXT",
        "changing_room": "TEXT",
        "lockers": "TEXT",
        "lodging_on_site": "TEXT",
        "last_update": "TIMESTAMP"
    }
    
    # Create the SQL query
    columns_str = ",\n".join([f"{column} {data_type}" for column, data_type in columns.items()])
    create_query = f"""
        CREATE TABLE IF NOT EXISTS clubs (
            id SERIAL PRIMARY KEY,
            {columns_str}
        )
    """

    # Execute the query
    cursor.execute(create_query)


# Function to insert or update data in the table
def insert_or_update_clubs(cursor, data):
    for club in data:
        columns = ', '.join(club.keys())
        placeholders = ', '.join(['%s'] * len(club))
        values = [club[key] for key in club.keys()]
        
        # Generate the INSERT ... ON CONFLICT ... DO UPDATE query
        insert_query = f"""
            INSERT INTO clubs ({columns})
            VALUES ({placeholders})
            ON CONFLICT (id) DO UPDATE
            SET {', '.join([f"{column}=EXCLUDED.{column}" for column in club.keys() if column != 'id'])};
        """
        
        cursor.execute(insert_query, values)



# Main function
def main():
    clubs_data = fetch_clubs()
    # print(clubs_data)
    if clubs_data:
        conn = connect_to_db()
        cursor = conn.cursor()
        create_table(cursor)
        insert_or_update_clubs(cursor, clubs_data)
        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully!")
        return
    else:
        print("Failed to fetch data from API.")

if __name__ == "__main__":
    main()
