from fastapi import FastAPI

from .routers import encrypt_payload

app = FastAPI(
    title="Simple App",
    description="This is a simple FastAPI application",
    version="1.0.0",
)

app.include_router(encrypt_payload.router)


@app.get("/")
def read_root():
    """Handle GET requests to the root endpoint."""
    return {"message": "Welcome to the Simple App!"}
