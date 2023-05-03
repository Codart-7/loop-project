#!/usr/bin/env python3
""" Creates the class to represent and manage reports """
from datetime import datetime, timedelta
import dbQuery


# None of the code has really been implemented
class Report:
    """ Represents a report and the methods required to manage it """

    def __init__(self, storeID: str, timeZone: str, current_datetime: datetime):
        """ Initialize the class """
        self.storeID = storeID
        self.timezone = timeZone
        self.datetime = current_datetime
    

    def uptime_last_hour(self):
        """ Calculates uptime in the last hour in minutes """

        # Get the store status from the database for "active" status
        status = dbQuery.get_store_status_local(store_id=self.storeID, timezone=self.timezone, activityStatus="active")
        
        # Put all the times in a list
        timesList = []
        for data in status:
            timesList.append(data[1])
        
        try:
            # Get the most recent entry
            last_entry = max(timesList)

            # Get store hours
            storeHours = dbQuery.get_store_hours(store_id=self.storeID)

            for data in storeHours:
                # Find storeHours entry for the day of last_entry
                if data.day == last_entry.weekday():
                    current_time = self.datetime.time()

                    # Ensure time of query is within business hours
                    if current_time > data.start_time_local and current_time < data.end_time_local:
                        return int((self.datetime - last_entry) / timedelta(minutes=1))
                    else:
                        return 0
        except ValueError:
            return 0
    

    def uptime_last_day(self) -> int:
        """ Calculates uptime in the last day in hours """
        return 4
    

    def uptime_last_week(self) -> int:
        """ Calculates uptime in the last week in hours """
        return 4
    

    def downtime_last_hour(self):
        """ Calculates downtime in the last hour in minutes """

        # Get the store status from the database for "active" status
        status = dbQuery.get_store_status_local(store_id=self.storeID, timezone=self.timezone, activityStatus="inactive")
        
        # Put all the times in a list
        timesList = []
        for data in status:
            timesList.append(data[1])
        
        try:
            # Get the most recent entry
            last_entry = max(timesList)

            # Get store hours
            storeHours = dbQuery.get_store_hours(store_id=self.storeID)

            for data in storeHours:
                # Find storeHours entry for the day of last_entry
                if data.day == last_entry.weekday():
                    current_time = self.datetime.time()

                    # Ensure time of query is within business hours
                    if current_time > data.start_time_local and current_time < data.end_time_local:
                        return int((self.datetime - last_entry) / timedelta(minutes=1))
                    else:
                        return 0
        except ValueError:
            return 0


    def downtime_last_day(self) -> int:
        """ Calculates downtime in the last day in hours """
        return 4
    

    def downtime_last_week(self) -> int:
        """ Calculates downtime in the last week in hours """
        return 4
