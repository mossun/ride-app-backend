from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Ride App Backend",
    description="FastAPI backend for Addis Ababa ride-hailing service",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Ride App Backend", 
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "ride-backend"}

# Basic ride endpoints for testing
@app.post("/api/v1/rides")
async def request_ride():
    return {
        "message": "Ride requested", 
        "ride_id": "test-123",
        "status": "searching_driver"
    }

@app.get("/api/v1/rides/{ride_id}")
async def get_ride(ride_id: str):
    return {
        "ride_id": ride_id, 
        "status": "requested", 
        "driver": None,
        "pickup_location": "Addis Ababa"
    }
