#!/usr/bin/env python3
""" The Celery task to handle the generation of reports """
from celery import Celery
from dbQuery import list_of_stores, save_report
from computation.reportGenerator import generateReport


app = Celery('reports', broker='amqp://localhost')


@app.task
def main_task():
    """ Defines the task """
    task_id = main_task.request.id
    
    # Get list of storeIDs
    storeIDs = list_of_stores()

    # Operate on each store
    for storeID in storeIDs:
        report_task.delay(storeID, task_id)


@app.task
def report_task(storeID, task_id):
    """ Generates the report for a single store.
        Saves the report and the parent task_ID to the database
    """
    report = generateReport(store=storeID)
    save_report(reportData=report, reportID=task_id)

    

