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

## Data Sources
The following are links to the data
- [store_status](https://drive.google.com/file/d/1UIx1hVJ7qt_6oQoGZgb8B3P2vd1FD025/view?usp=sharing)
- [store_hours](https://drive.google.com/file/d/1va1X3ydSh-0Rt1hsy2QSnHRA4w57PcXg/view?usp=sharing)
- [store_timezone](https://drive.google.com/file/d/101P9quxHoMZMZCVWQ5o-shonk2lgK1-o/view?usp=sharing)

### Extra
I implented some endpoints to help with populating your database tables with the data from these files.
Check `src/api/routes/router.py`.
Alternatively, use the `updateDB.py` file. Open the file and read the instructions first.


## Usage
- Install requirements.txt
- Create a `.env` file that has the same fields as `.env.example`
- Have access to a PostgreSQL database
- Take a look at the config.config file and follow the instruction
- Start the app: `uvicorn main:app`

