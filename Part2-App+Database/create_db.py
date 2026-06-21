from database import engine
from models import Base

# This creates all tables defined in models.py
Base.metadata.create_all(bind=engine)