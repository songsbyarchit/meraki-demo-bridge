from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    room_id = Column(String)
    
    # New fields
    role = Column(String)           # AE, SE, etc.
    audience = Column(String)       # partner, customer, internal
    product_line = Column(String)   # mx, mr, etc.
    industry = Column(String)      # e.g., healthcare
    tool_used = Column(String)
    usual_minutes = Column(Integer)
    bridge_minutes = Column(Integer)
    percentage_time_saved = Column(Integer)  # Can be negative or positive
    quality_rating = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    extra_feedback = Column(Text)