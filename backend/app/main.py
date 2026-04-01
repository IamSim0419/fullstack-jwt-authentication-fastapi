from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api.routes import auth_route
from app.api.routes import users_route
from fastapi.middleware.cors import CORSMiddleware

# Create the database tables based on the defined models
Base.metadata.create_all(bind=engine)

# Run: uvicorn app.main:app --reload
app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://yourfrontenddomain.com",
]

app.add_middleware(
    CORSMiddleware,
    #allow_origins=origins, # Allows only specified origins
    allow_origins=["*"], # Allows all origins
    allow_credentials=True,
    allow_methods=["*"], # Allows all HTTP methods
    allow_headers=["*"], # Allows all headers
)

app.include_router(auth_route.router)
app.include_router(users_route.router)

@app.get("/")
def health():
    return {"status": "ok🎉"}






