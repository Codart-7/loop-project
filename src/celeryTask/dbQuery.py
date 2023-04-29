#!/usr/bin/env python3
""" All database queries to perform the Celery task. """
import pytz
from datetime import datetime, time
from sqlalchemy.sql.sqltypes import TIME
from sqlalchemy import String, func, text, bindparam

# Uncomment the below to test any of the functions
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import models
from db.models.storeHours import Store_Hours
from db.models.storeStatus import Store_Status
from db.models.storeTimezone import Store_Timezone
from db.models.storeRecords import Store_Records

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
    store_hours = db.query(
        Store_Hours.day,
        Store_Hours.start_time_local,
        Store_Hours.end_time_local
    ).filter_by(store_id=store_id).all()
    db.close()
    return store_hours[-7:]


def get_store_status_local(store_id: str, timezone: str):
    """ Gets status data from database by store_id
        'timezone_str' is already converted to the timezone passed as argument
    """
    db = SessionLocal()

    status = db.query(
        Store_Status.status,
        text("(timestamp_utc AT TIME ZONE 'UTC') AT TIME ZONE :timezone").bindparams(bindparam("timezone", value=timezone, type_=String))
        ).filter_by(store_id=store_id).all()
    db.close
    return status


def get_store_timezone(store_id: str):
    """ gets timezone data from database """
    db = SessionLocal()

    timezone_data = db.query(
        Store_Timezone.store_id,
        Store_Timezone.timezone_str
        ).filter_by(store_id=store_id).all()
    db.close()
    return timezone_data


# Uncomment the below to test any of the functions. Implement your testing code as well
#if __name__ == "__main__":
#    storeHours = get_store_hours("1481966498820158979")
#    for data in storeHours:
#        print(data)
#        print("")
    
#    status = get_store_status_local("1481966498820158979", 'Asia/Beirut')
#    timesList = []
#    for data in status:
#       print(data)
#       print("")
#       timesList.append(data[1])
#
#    print(timesList)
#    print("")
#    print(max(timesList))
   

#    timezone = get_store_timezone("1481966498820158979")
#    for time in timezone:
#        print(time)
