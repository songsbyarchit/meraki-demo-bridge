from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class MSSwitch(Base):
    __tablename__ = "ms_switches"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, unique=True, index=True)
    use_case = Column(String)
    ports_1gbe = Column(Integer)
    ports_mgig = Column(Integer)
    uplinks = Column(String)  # Comma-separated list
    poe_support = Column(String)
    stackable = Column(Boolean)
    routing = Column(String)
    catalyst = Column(Boolean)
    notes = Column(String)