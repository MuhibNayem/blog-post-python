from sqlalchemy.orm import Session
from app.db import base_class # Import all models
from app.db.session import engine

def init_db():
    base_class.Base.metadata.create_all(bind=engine)
