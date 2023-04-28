#!/usr/bin/env python3
""" All database queries to perform the Celery task. """
from db.session import SessionLocal
from typing import List, Dict


def list_of_stores() -> List: # type: ignore
    """ Retrieves a list of unique storeIDs from the database """
    db = SessionLocal


def save_report(reportData: Dict, reportID: str):
    """ Saves report data and report ID to the database """
    db = SessionLocal