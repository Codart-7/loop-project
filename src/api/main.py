#!/usr/bin/env python3
""" The main API entry point """
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from config.config import settings
from routes.router import end_points
from db.session import engine
from db.base import Base


def include_router(app):
	app.include_router(end_points)


def create_tables():
	print("create_tables")
	Base.metadata.create_all(bind=engine) # type: ignore


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    return app


app = start_application()
