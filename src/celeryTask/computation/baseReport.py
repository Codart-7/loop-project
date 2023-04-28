#!/usr/bin/env python3
""" Creates the base class for all reports """
import datetime


class BaseReport:
    """ Base class for all reports.
        Initializes the data needed to perform all necessary computations
    """

    def __init__(self) -> None:
        self.current_day: int = datetime.datetime.utcnow().weekday()
        self.current_hour: int = datetime.datetime.utcnow().hour
