import requests
import psycopg2

# Function to fetch data from API
def fetch_clubs():
    url = "https://api.golf-course-database.com:8000/clubs"
    response = requests.get(url, auth=("andrewwhite", "Hd3@j2Dmh3"))
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
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clubs (
            id SERIAL PRIMARY KEY,
            name TEXT,
            address TEXT,
            city TEXT,
            state TEXT,
            country TEXT,
            phone TEXT,
            email TEXT
            -- Add more columns as needed
        )
    """)

# Function to insert data into table
def insert_data(cursor, data):
    for club in data:
        cursor.execute("""
            INSERT INTO clubs (name, address, city, state, country, phone, email)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            club.get('name', ''),
            club.get('address', ''),
            club.get('city', ''),
            club.get('state', ''),
            club.get('country', ''),
            club.get('phone', ''),
            club.get('email', '')
        ))

# Main function
def main():
    clubs_data = fetch_clubs()
    print(clubs_data)
    if clubs_data:
        return
        conn = connect_to_db()
        cursor = conn.cursor()
        create_table(cursor)
        insert_data(cursor, clubs_data)
        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully!")
    else:
        print("Failed to fetch data from API.")

if __name__ == "__main__":
    main()
