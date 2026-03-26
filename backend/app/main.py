from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth_route
from fastapi.middleware.cors import CORSMiddleware

# Create the database tables based on the defined models
Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://yourfrontenddomain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Allows all origins from the list
    allow_credentials=True,
    allow_methods=["*"], # Allows all HTTP methods
    allow_headers=["*"], # Allows all headers
)

app.include_router(auth_route.router)

@app.get("/")
def health():
    return {"status": "ok🎉"}






