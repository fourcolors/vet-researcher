"""
Main FastAPI application module.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Vet Researcher API",
    description="API for veterinary research analysis",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Configure this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to the Vet Researcher API"}

def start():
    """Start the API server."""
    uvicorn.run("vet_researcher.api.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start() 