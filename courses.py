# Function to create the courses table
def create_courses_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id SERIAL PRIMARY KEY,
            course_id TEXT,
            club_id TEXT,
            course_name TEXT,
            holes TEXT,
            par TEXT,
            course_type TEXT,
            course_architect TEXT,
            open_date TEXT,
            guest_policy TEXT,
            weekday_price TEXT,
            weekend_price TEXT,
            twilight_price TEXT,
            fairway TEXT,
            green TEXT,
            currency TEXT,
            last_update TIMESTAMP
        )
    """)



# Function to insert or update course data in the table
def insert_or_update_courses(cursor, data):
    for course in data:
        columns = ', '.join(course.keys())
        placeholders = ', '.join(['%s'] * len(course))
        values = [course[key] for key in course.keys()]
        
        # Generate the INSERT ... ON CONFLICT ... DO UPDATE query
        insert_query = f"""
            INSERT INTO courses ({columns})
            VALUES ({placeholders})
            ON CONFLICT (id) DO UPDATE
            SET {', '.join([f"{column}=EXCLUDED.{column}" for column in course.keys() if column != 'course_id'])};
        """
        
        cursor.execute(insert_query, values)