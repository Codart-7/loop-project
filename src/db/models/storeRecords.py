from sqlalchemy import Column, Integer, String

from db.base_class import Base

class Store_Records(Base):
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(String, nullable=False, index=True)
    record_id = Column(String, nullable=False, index=True)
    uptime_last_hour = Column(Integer, index=True)
    uptime_last_day = Column(Integer, index=True)
    uptime_last_week = Column(Integer, index=True)
    downtime_last_hour = Column(Integer, index=True)
    dowmtime_last_day = Column(Integer, index=True)
    downtime_last_week = Column(Integer, index=True)