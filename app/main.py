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

# Path parameters
@app.get("/invoices/{invoice_id}")
def get_invoice(invoice_id: int):
    """
    Get a specific invoice by ID

    Args:
        invoice_id (int): The invoice ID

    Returns:
        Invoice data
    """
    # Fake data
    return {
        "invoice_id": invoice_id,
        "client": "Acme Corp",
        "total": 1500.00,
        "status": "pending"
    }

@app.get("/clients/{client_name}")
def get_client(client_name: str):
    """Get client information by name

    Args:
        client_name (str): Name of the client
    
    Returns:
        Client data with invoices summary
    """
    return {
        "name": client_name,
        "total_invoices": 1,
        "total_amount": 1500.00,
        "status": "active"
    }