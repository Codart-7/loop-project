from sqlalchemy import Column, Integer, String, DateTime

from db.base_class import Base

class Store_Status(Base):
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(String, nullable=False)
    timestamp_utc = Column(DateTime(timezone=True))
    status = Column(String, nullable=False, index=True)