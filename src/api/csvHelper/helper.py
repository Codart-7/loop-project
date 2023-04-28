#!/usr/bin/env python3
""" All functions to help with injecting files into the database """
import os
import sys

from db.session import SessionLocal
from db.models.storeStatus import Store_Status
from db.models.storeHours import Store_Hours
from db.models.storeTimezone import Store_Timezone


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# Insert data into the database using sqlalchemy ORM

def insert_status_into_database(data):
    session = SessionLocal()

    for row in data:
        obj = Store_Status(**row)
        session.add(obj)
    session.commit()
    session.close()


def insert_hours_into_database(data):
    session = SessionLocal()

    for row in data:
        obj = Store_Hours(**row)
        session.add(obj)
    session.commit()
    session.close()


def insert_timezone_into_database(data):
    session = SessionLocal()

    for row in data:
        obj = Store_Timezone(**row)
        session.add(obj)
    session.commit()
    session.close()
