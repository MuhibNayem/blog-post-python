from fastapi import FastAPI
from app.api.api_v1.api import api_router
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

from app.db.init_db import init_db


app = FastAPI(title=settings.PROJECT_NAME)

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix=settings.API_V1_STR)

# Create tables
init_db()

print("Tables created successfully!")

@app.get("/")
def root():
    return {"message": "Welcome to the Blog API!"}
