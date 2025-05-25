from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class MXAppliance(Base):
    __tablename__ = "mx_appliances"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, unique=True, index=True)
    use_case = Column(String)
    throughput_mbps = Column(Integer)
    max_users = Column(Integer)
    uplink_ports = Column(String)  # Comma-separated list
    has_wireless = Column(Boolean)
    has_cellular = Column(Boolean)
