from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# PostgreSQL connection string (To connect to the postgtres Server DB)
DATABASE_URL = "postgresql://postgres:Password1!@192.168.122.50:5432/postgres"

# Create engine (core DB connection)
engine = create_engine(DATABASE_URL)

# Create session factory (used in API routes)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)