#!/usr/bin/env python3
""" Model for the store_status table """
from sqlalchemy import Column, Integer, String, DateTime

from db.base_class import Base

class Store_Status(Base):
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(String, nullable=False)
    status = Column(String, nullable=False, index=True)
    timestamp_utc = Column(DateTime(timezone=True))
    