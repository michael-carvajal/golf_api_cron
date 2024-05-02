import os
import requests
import psycopg2
from dotenv import load_dotenv
from clubs import create_table,  insert_or_update_clubs
load_dotenv()

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

def fetch_clubs():
    url = os.getenv("API_URL")
    username = os.getenv("API_USERNAME")
    password = os.getenv("API_PASSWORD")
    response = requests.get(f'{url}/clubs', auth=(username, password))
    if response.status_code == 200:
        return response.json()
    else:
        return None







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
