from typing import Optional
from pydantic import BaseModel

class Message(BaseModel):
    report_id: str