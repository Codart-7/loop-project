#!/usr/bin/env python3
""" FastAPI router to define all the enpoints """
from fastapi import APIRouter
from fastapi import File, UploadFile
import csv
from api.csvHelper.helper import insert_status_into_database
from api.csvHelper.helper import insert_hours_into_database
from api.csvHelper.helper import insert_timezone_into_database

from schema.message import Message


end_points = APIRouter()


# main endpoints
# Celery task has not yet been integrated

@end_points.get("/trigger_report")
async def trigger_report():
	return "Report"


@end_points.get("/get_report")
async def get_report(reportID: Message):
	return reportID.report_id


# endpoints to help with populating the database

@end_points.post("/uploadStatusFile/")
async def upload_status_file(file: UploadFile = File(...)):
    """
    Endpoint that receives a csv file and inserts the data into the Postgres database
    """
    # Read csv file
    file_content = await file.read()
    csv_data = csv.reader(file_content.decode('utf-8').splitlines())

    # Convert csv data to desired format for insertion into database
    data_to_insert = []
    for row in csv_data:
        data_to_insert.append({
            'store_id': row[0],
            'timestamp_utc': row[1],
            'status': row[2]
        })

    # Insert data into database
    insert_status_into_database(data_to_insert)

    return {"status": "File uploaded and data inserted into database."}

@end_points.post("/uploadHoursFile/")
async def upload_hours_file(file: UploadFile = File(...)):
    """
    Endpoint that receives a csv file and inserts the data into the Postgres database
    """
    # Read csv file
    file_content = await file.read()
    csv_data = csv.reader(file_content.decode('utf-8').splitlines())

    # Convert csv data to desired format for insertion into database
    data_to_insert = []
    for row in csv_data:
        data_to_insert.append({
            'store_id': row[0],
            'day': row[1],
            'start_time_local': row[2],
            'end_time_local': row[3]
        })

    # Insert data into database
    insert_hours_into_database(data_to_insert)

    return {"status": "File uploaded and data inserted into database."}


@end_points.post("/uploadTimezoneFile/")
async def upload_timezone_file(file: UploadFile = File(...)):
    """
    Endpoint that receives a csv file and inserts the data into the Postgres database
    """
    # Read csv file
    file_content = await file.read()
    csv_data = csv.reader(file_content.decode('utf-8').splitlines())

    # Convert csv data to desired format for insertion into database
    data_to_insert = []
    for row in csv_data:
        data_to_insert.append({
            'store_id': row[0],
            'timezone_str': row[1]
        })

    # Insert data into database
    insert_timezone_into_database(data_to_insert)

    return {"status": "File uploaded and data inserted into database."}
