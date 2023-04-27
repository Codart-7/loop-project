from sqlalchemy import Column, Integer, String

from db.base_class import Base

class Store_Timezone(Base):
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(String, nullable=False, index=True)
    timezone_str = Column(String, nullable=False, index=True)
