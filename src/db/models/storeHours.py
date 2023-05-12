#!/usr/bin/env python3
""" Model for the store_hours table """
from sqlalchemy import Column, Integer, String, TIME

from db.base_class import Base

class Store_Hours(Base):
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(String, nullable=False, index=True)
    day = Column(Integer, index=True)
    start_time_local = Column(TIME)
    end_time_local = Column(TIME)
