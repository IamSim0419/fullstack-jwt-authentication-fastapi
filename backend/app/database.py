from sqlalchemy import create_engine, Column, Integer, String
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

# The 'connect_args' parameter is used to pass additional arguments to the database connection      
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
    if "sqlite" in DATABASE_URL else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()   





