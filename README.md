# The Loop Project

## Problem Statement
Loop monitors several restaurants in the US and needs to monitor if the store is online or not.
All restaurants are supposed to be online during their business hours.
Due to some unknown reasons, a store might go inactive for a few hours.
Restaurant owners want to get a report of the how often this happened in the past.

We want to build backend APIs that will help restaurant owners achieve this goal.

## Data output requirement
We want to output a report to the user that has the following schema:

<big><pre>
store_id, uptime_last_hour(in minutes), uptime_last_day(in hours), uptime_last_week(in hours), downtime_last_hour(in minutes), downtime_last_day(in hours), downtime_last_week(in hours)
</pre></big>

Uptime and downtime should only include observations within business hours.

## API requirement
You need two APIs 
- `/trigger_report` endpoint that will trigger report generation from the database
    - No input
    - Output: report_id
    - report_id will be used for polling the status of report completion

- `/get_report` endpoint that will return the status of the report and the csv
    - Input: report_id
    - Output:
        - if report generation is not complete, return “Running” as the output
        - if report generation is complete, return “Complete” along with the CSV file with the schema described above.

## Usage
- Install requirements
- Create a `.env` file that has the same fields as `.env.example`
- Have access to a PostgreSQL database
- Start the app: `uvicorn main:app`