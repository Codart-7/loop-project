from fastapi import APIRouter

from schema.message import Message


end_points = APIRouter()


@end_points.get("/trigger_report")
async def trigger_report():
	return "Report"


@end_points.get("/get_report")
async def get_report(reportID: Message):
	return reportID.report_id
