from app.db import base_class
from app.db.session import engine

def init_db():
    base_class.Base.metadata.create_all(bind=engine)
