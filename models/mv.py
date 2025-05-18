from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class MVCamera(Base):
    __tablename__ = "mv_cameras"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, unique=True, index=True)
    use_case = Column(String)
    resolution = Column(String)
    onboard_storage = Column(Boolean)
    wireless = Column(Boolean)
    notes = Column(String)