#!/usr/bin/env python3
""" All database queries to perform the Celery task. """
import pytz
from datetime import datetime, time, timedelta
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
    store_hours = db.query(Store_Hours).filter_by(store_id=store_id).all()
    db.close()
    return store_hours[-7:]


def get_store_status_local(store_id: str, timezone: str, activityStatus: str):
    """ Gets status data from database by store_id and required status.
        'timezone_str' is already converted to the timezone passed as argument
    """
    db = SessionLocal()

    status = db.query(
        Store_Status.status,
        text("(timestamp_utc AT TIME ZONE 'UTC') AT TIME ZONE :timezone").bindparams(bindparam("timezone", value=timezone, type_=String))
        ).filter_by(store_id=store_id, status=activityStatus).all()
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
if __name__ == "__main__":
    timezone_data = get_store_timezone("1481966498820158979")
    timezone_str = str(timezone_data[0][1])
    
    status = get_store_status_local("1481966498820158979", timezone=timezone_str, activityStatus="inactive")
        
    timesList = []
    for data in status:
        timesList.append(data[1])
        

    try:
        last_entry = max(timesList)
    
        storeHours = get_store_hours("1481966498820158979")
    
        for data in storeHours:
            if data.day == last_entry.weekday():
                # get current time
                timeZone = pytz.timezone(timezone_str)
                current = datetime.now(timeZone)
                current_time = current.time()

                if current_time > data.start_time_local and current_time < data.end_time_local:
                    print("within time frame")
                    minute_difference = int((current - last_entry).total_seconds() / 60)
                    print(minute_difference)
                
                else:
                    print("should return 0")
    except ValueError:
        print("no value for last entry.")
            #time_part = last_entry.time()
            #start_time = data.start_time_local
            #if time_part > start_time:
            #    print("time_part is greater than start_time")
            #else:
            #    print("start_time is greater than or equal to time_part")



    
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

#   storeHours = get_store_hours("1481966498820158979")
#    for data in storeHours:
#        print(f"ID: {data.id}, Store ID: {data.store_id}, Day: {data.day}, Start Time: {data.start_time_local}, End Time: {data.end_time_local}")
#        print("")
