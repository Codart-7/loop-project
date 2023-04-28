#!/usr/bin/env python3
""" Creates everything needed for the SQLAlchemy connection """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from config.config import settings


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
