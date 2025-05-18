from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class MRAccessPoint(Base):
    __tablename__ = "mr_access_points"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, unique=True, index=True)
    wifi_standard = Column(String)
    radios = Column(Integer)
    antenna_type = Column(String)
    poe = Column(Boolean)
    notes = Column(String)