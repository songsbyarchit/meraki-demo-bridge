from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class MVCamera(Base):
    __tablename__ = "mv_cameras"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, unique=True, index=True)
    onboard_storage = Column(Boolean)
    location = Column(String)
    fov = Column(String)
    max_fps = Column(Integer)
    resolution = Column(String)
    use_case = Column(String)
    datasheet_url = Column(String, nullable=True)
