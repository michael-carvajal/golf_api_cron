import os
import requests
import psycopg2
from dotenv import load_dotenv
from clubs import create_clubs_table,  insert_or_update_clubs
from courses import create_courses_table, insert_or_update_courses
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


# Function to fetch course data from API
def fetch_courses():
    url = os.getenv("API_URL")
    username = os.getenv("API_USERNAME")
    password = os.getenv("API_PASSWORD")
    response = requests.get(f'{url}/courses', auth=(username, password))
    if response.status_code == 200:
        return response.json()
    else:
        return None





def main():
    clubs_data = fetch_clubs()
    if clubs_data:
        conn = connect_to_db()
        cursor = conn.cursor()
        create_clubs_table(cursor)
        insert_or_update_clubs(cursor, clubs_data)
        conn.commit()
        cursor.close()
        conn.close()
        print("Club data inserted or updated successfully!")
    else:
        print("Failed to fetch club data from API.")

    courses_data = fetch_courses()
    if courses_data:
        conn = connect_to_db()
        cursor = conn.cursor()
        create_courses_table(cursor)
        insert_or_update_courses(cursor, courses_data)
        conn.commit()
        cursor.close()
        conn.close()
        print("Course data inserted or updated successfully!")
    else:
        print("Failed to fetch course data from API.")

if __name__ == "__main__":
    main()

