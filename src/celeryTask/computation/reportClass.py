#!/usr/bin/env python3
""" Creates the class to represent and manage reports """
from baseReport import BaseReport
import datetime
from dbQuery import get_store_hours


# None of the code has really been implemented
class Report(BaseReport):
    """ Represents a report and the methods required to manage it """

    def __init__(self, storeID: str):
        """ Initialize the class """
        super().__init__()
        self.storeID = storeID
    

    def uptime_last_hour(self) -> int:
        """ Calculates uptime in the last hour in minutes """       
        return 4
    

    def uptime_last_day(self) -> int:
        """ Calculates uptime in the last day in hours """
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
