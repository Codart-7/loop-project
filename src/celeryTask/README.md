# Implementing the processing algorithm
The API layer is half of the work. Another important half is the algoritm to actually generate the report.

NOTE: This celery task has not yet been integrated with the API

## Approach
Generating the report is placed as a task to be managed by Celery. `task.py` is the entry point. It retrieves all the unique storeID from the database and performs a report generation for each store via a sub-task. This is to increase modularity and efficiency as the sub-tasks are all asynchronous.

The sub-task performs the port generation for each store and saves the report in the database along with the main taskID. An enpoint can then be implemented in the API layer to either retrive the report for all the stores using the taskID or for a specific store using the taskID and the storeID

### Sub-task algorithm
The function `generateReport` takes in the storeID. It creates an instance of the `Report` class, calls all its methods (wich perform the necessary computations) and fills the result of these method calls into a dictionary. It then returns the complete dictionary which now has all the values required of a report. The sub-task takes this dictionary and saves the data into the database.





