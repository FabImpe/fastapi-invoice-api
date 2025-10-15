"""
FastAPI Invoice Management API - Main application entry point.
"""
from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI(
    title = "Invoice Management",
    description = "REST API for managing invoices, clients, and payments",
    version="0.1.0",
)

# First endpoint - Health check
@app.get("/")
def read_root():
    """
    Health check endpoint.
    
    Returns:
        Message confirming API is running
    """
    return {
        "message": "Invoice Management API",
        "version": "0.1.0",
        "status": "running"
    }

@app.get("/health")
def health_check():
    """Health check for monitoring"""
    return {"status": "healthy"}

@app.get("/about")
def about():
    """
    Information about the API.
    
    Returns info about the project and tech stack.
    """
    return {
        "project": "FastAPI Invoice Management API",
        "author": "Fabien Impellizzeri",
        "tech_stack": ["FastAPI", "Python"]
    }

