from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class MSSwitch(Base):
    __tablename__ = "ms_switches"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, unique=True, index=True)
    use_case = Column(String)
    ports_1gbe = Column(Integer)
    ports_mgig = Column(Integer)
    uplinks = Column(String)  # Comma-separated string like "2x 10G SFP+, 4x 1G SFP"
    poe_support = Column(String)
    stackable = Column(Boolean)
    routing = Column(String)  # e.g., "L2", "DHCP relay", "Dynamic"
    catalyst = Column(Boolean)
    datasheet_url = Column(String, nullable=True)
