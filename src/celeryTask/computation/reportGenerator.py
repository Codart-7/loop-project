#!/usr/bin/env python3
""" Contains the function to generate a report given the store ID """
from datetime import datetime
from typing import Dict

import pytz
from celeryTask import dbQuery
from reportClass import Report


def generateReport(store: str) -> Dict:
    """ Function to generate report as a dictionary """

    # Instantiate report dictionary
    report = dict()

    # Add store_id to report
    report["store_id"] = store

    # Get store timezone
    timezone_data = dbQuery.get_store_timezone(store_id=store)
    timezone_str = str(timezone_data[0][1])

    # get current time
    timeZone = pytz.timezone(timezone_str)
    current = datetime.now(timeZone)

    # Create an instance of Report class
    createdReport = Report(storeID=store, timeZone=timezone_str, current_datetime=current)

    # Add necessary data to report dictionary
    report["uptime_last_hour"] = createdReport.uptime_last_hour()
    report["uptime_last_day"] = createdReport.uptime_last_day()
    report["uptime_last_week"] = createdReport.uptime_last_week()
    report["downtime_last_hour"] = createdReport.downtime_last_hour()
    report["downtime_last_day"] = createdReport.downtime_last_day()
    report["downtime_last_week"] = createdReport.downtime_last_week()

    # Return the report
    return report
