from pydantic import Field
from database import engine
from database import Base

class User(Base):
    __tablename__ = "users"

    id: int = Field(default=None, primary_key=True)
    username: str = Field(default=None, unique=True)
    hashed_password: str = Field(default=None)

# Create the database tables based on the defined models
User.metadata.create_all(bind=engine)



