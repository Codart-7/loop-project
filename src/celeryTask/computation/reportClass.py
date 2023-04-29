#!/usr/bin/env python3
""" Creates the class to represent and manage reports """
from baseReport import BaseReport
import datetime
import dbQuery


# None of the code has really been implemented
class Report(BaseReport):
    """ Represents a report and the methods required to manage it """

    def __init__(self, storeID: str):
        """ Initialize the class """
        super().__init__()
        self.storeID = storeID
    

    def uptime_last_hour(self) -> int:
        """ Calculates uptime in the last hour in minutes """
        timezone_data = dbQuery.get_store_timezone(store_id=self.storeID)
        timezone_str = str(timezone_data[1])
        status = dbQuery.get_store_status_local(store_id=self.storeID, timezone=timezone_str)
        
        timesList = []
        for data in status:
            timesList.append(data[1])
        
        last_entry = max(timesList)

        start_time = last_entry - datetime.timedelta(hours=24)

        data_24hrs = [entry for entry in timesList if entry >= start_time]
        return 4
    

    def uptime_last_day(self) -> int:
        """ Calculates uptime in the last day in hours """
        timezone_data = dbQuery.get_store_timezone(store_id=self.storeID)
        timezone_str = str(timezone_data[1])
        status = dbQuery.get_store_status_local(store_id=self.storeID, timezone=timezone_str)
        
        timesList = []
        for data in status:
            timesList.append(data[1])
        
        last_entry = max(timesList)

        start_time = last_entry - datetime.timedelta(hours=24)

        data_24hrs = [entry for entry in timesList if entry >= start_time]
        return 4
    

    def uptime_last_week(self) -> int:
        """ Calculates uptime in the last week in hours """
        return 4
    

    def downtime_last_hour(self) -> int:
        """ Calculates downtime in the last hour in minutes """
        return 4
    

    def downtime_last_day(self) -> int:
        """ Calculates downtime in the last day in hours """
        return 4
    

    def downtime_last_week(self) -> int:
        """ Calculates downtime in the last week in hours """
        return 4
