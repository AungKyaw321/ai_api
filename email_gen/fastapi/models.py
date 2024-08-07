from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from datetime import datetime

Base = declarative_base()

class SavedEmail(Base):
    __tablename__ = "saved_emails"

    id = Column(Integer, primary_key=True, index=True)
    base64_html = Column(Text, nullable=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())