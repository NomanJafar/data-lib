from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from dotenv import load_dotenv
import os

from ..models.tables import Base  # Update import

# Load environment variables from .env file
load_dotenv()


class DatabaseManager:
    def __init__(self, database_url: str = None):
        self.database_url = database_url or os.getenv('DATABASE_URL')
        self.engine = create_engine(self.database_url)
        self.SessionLocal = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)

    @contextmanager
    def get_session(self):
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def create_all(self):
        Base.metadata.create_all(self.engine)