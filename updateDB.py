#!/usr/bin/env python3
""" Script to update the database from the given CSV file.

    Usage: python updateDB.py <table name> <csv file>

    Update the following lines for your use case:
    23rd line: It uses id as primary key.
               The others are the names of the columns and their data types, in the order they appear in the file
    30th line: The names of the columns as listed above with the right number of format specifiers
"""
import argparse
import csv
import psycopg2


def populate_table(table_name, file_name):
    # Connect to the database
    print("start")
    conn = psycopg2.connect(database="test", user="michael", password="AlphaSql-1", host="localhost", port=5432)
    cur = conn.cursor()

    # Create the table if it doesn't exist
    cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id SERIAL PRIMARY KEY, store_id TEXT, status TEXT, timestamp_utc TIME WITH TIME ZONE)")

    # Open the CSV file and insert the data into the table
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip the header row
        for row in reader:
            cur.execute(f"INSERT INTO {table_name} (store_id, status, timestamp_utc) VALUES (%s, %s, %s)", row)

    # Commit the changes and close the connection
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Populate a table in a Postgres database with data from a CSV file")
    parser.add_argument("table_name", help="Name of the table to populate")
    parser.add_argument("file_name", help="Name of the CSV file to read data from")
    args = parser.parse_args()

    populate_table(args.table_name, args.file_name)
    print("done")
