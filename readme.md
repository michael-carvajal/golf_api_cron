# Golf API Data Importer

This Python script fetches data from a golf course API and imports it into a PostgreSQL database.

## Prerequisites

- Python 3.x installed on your system
- PostgreSQL installed and running
- Access to the golf course API
- Access to a PostgreSQL database

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.

## Setup

1. Copy the `.env.example` file and rename it to `.env`.
2. Fill in the required environment variables in the `.env` file:
   - `API_URL`: URL of the golf course API.
   - `API_USERNAME`: Username for accessing the API.
   - `API_PASSWORD`: Password for accessing the API.
   - `DB_NAME`: Name of the PostgreSQL database.
   - `DB_USER`: Username for accessing the PostgreSQL database.
   - `DB_PASSWORD`: Password for accessing the PostgreSQL database.

## Running the Script

1. Ensure that PostgreSQL is running.
2. Run the following command to install the required Python packages:
- pip install -r requirements.txt
3. Run the script using the following command:
- python main.py



The script will fetch data from the API and import it into the PostgreSQL database.

## Notes

- Make sure to set up the environment variables correctly in the `.env` file before running the script.
- Ensure that the PostgreSQL database and tables are created before running the script.

