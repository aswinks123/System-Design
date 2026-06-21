# Define what data your system will store in PostgreSQL.

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class PhotoJob(Base):
    __tablename__ = "photo_jobs"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    status = Column(String, nullable=False, default="PROCESSING")

    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)