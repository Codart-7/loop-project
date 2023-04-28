#!/usr/bin/env python3
""" All database queries to perform the Celery task. """
import pytz
from datetime import datetime, time
from sqlalchemy.sql.sqltypes import TIME

# Uncomment the below to test any of the functions
# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db.models.storeHours import Store_Hours
from db.session import SessionLocal

from typing import List, Dict


def list_of_stores() -> List: # type: ignore
    """ Retrieves a list of unique storeIDs from the database """
    db = SessionLocal()
    pass


def save_report(reportData: Dict, reportID: str):
    """ Saves report data and report ID to the database """
    db = SessionLocal()
    pass


def get_store_hours(store_id: str):
    """ Gets the store hours from the database given the store ID
        Store hours are usually updated at once by the entire week
        So we return the last 7 entries for this store
        This represents the most recent data for the store
    """
    db = SessionLocal()
    store_hours = db.query(Store_Hours).filter_by(store_id=store_id).all()
    db.close()
    return store_hours[-7:]

# Uncomment the below to test any of the functions. Implement your testing code as well
#if __name__ == "__main__":
#    storeHours = get_store_hours("1481966498820158979")
#    for data in storeHours:
#            if data.day == 6:
#                local_time = TIME(data.end_time_local)  
#                timezone = 'Asia/Beirut'  # example timezone
#                day_of_week = 6