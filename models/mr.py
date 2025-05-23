from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class MRAccessPoint(Base):
    __tablename__ = "mr_access_points"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, unique=True, nullable=False)
    wifi_standard = Column(String, nullable=False)
    radios = Column(Integer, nullable=False)
    antenna_type = Column(String, nullable=False)
    poe = Column(Boolean, nullable=False)
    catalyst = Column(Boolean, nullable=False)
    datasheet_url = Column(String, nullable=True)
