from fastapi import APIRouter, Request, Response, Body


end_points = APIRouter()


@end_points.get("/trigger_report")
async def trigger_report(request: Request):
	return {"message": "Report"} 


@end_points.get("/get_report")
async def get_report(reportID: Response):
	return reportID.body
