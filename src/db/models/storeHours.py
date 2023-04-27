from sqlalchemy import Column, Integer, String, TIME

from db.base_class import Base

class Store_Hours(Base):
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(String, nullable=False, index=True)
    day_of_week = Column(Integer, index=True)
    start_time_local = (TIME)
    end_time_local = (TIME)
