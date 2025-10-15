"""
FastAPI Invoice Management API - Main application entry point.
"""
from fastapi import FastAPI
from typing import Optional

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
    """
    Get client information by name

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

# Query parameters
@app.get("/invoices")
def list_invoices(status: Optional[str] = None, limit: int = 10, skip: int = 0):
    """
    List invoices with optional filtering.

    Args:
        status (Optional[str], optional): Filter by status (paid, pending, overdue). Defaults to None.
        limit (int, optional): Manimum number of results. Defaults to 10.
        skip (int, optional): Number of results to skip (pagination). Defaults to 0.

    Return:
        List of invoices
    """
    # Fake data
    invoices = [
        {"id": 1, "client": "Acme Corp", "total": 1500.00, "status": "paid"},
        {"id": 2, "client": "Beta Inc", "total": 2500.00, "status": "pending"},
        {"id": 3, "client": "Gamma Ltd", "total": 800.00, "status": "overdue"},
        {"id": 4, "client": "Acme Corp", "total": 3200.00, "status": "paid"},
        {"id": 5, "client": "Delta Co", "total": 1200.00, "status": "pending"},
    ]

    # Filtre par status si fourni
    if status:
        invoices = [invoice for invoice in invoices if invoice["status"] == status]
    
    # Pagination
    return {
        "total": len(invoices),
        "skip": skip,
        "limit": limit,
        "results": invoices[skip : skip + limit]
    }

@app.get("/search/invoices")
def search_invoices(client: Optional[str] = None, min_amount: Optional[float] = None, max_amount: Optional[float] = None):
    """
    Search for invoices with filters.

    Args:
        client (Optional[str], optional): Filter by client name. Defaults to None.
        min_amount (Optional[float], optional): Minimum invoice amount. Defaults to None.
        max_amount (Optional[float], optional): Maximum invoice amount. Defaults to None.
    
    Returns:
        Filtered invoices
    """
    # TON CODE ICI
    # Utilise les mêmes données fake que list_invoices
    # Applique les filtres :
    # - Si client est fourni, filtre par nom (case-insensitive, partial match)
    # - Si min_amount est fourni, garde seulement les factures >= min_amount
    # - Si max_amount est fourni, garde seulement les factures <= max_amount

    # Fake data
    invoices = [
        {"id": 1, "client": "Acme Corp", "total": 1500.00, "status": "paid"},
        {"id": 2, "client": "Beta Inc", "total": 2500.00, "status": "pending"},
        {"id": 3, "client": "Gamma Ltd", "total": 800.00, "status": "overdue"},
        {"id": 4, "client": "Acme Corp", "total": 3200.00, "status": "paid"},
        {"id": 5, "client": "Delta Co", "total": 1200.00, "status": "pending"},
    ]

    # Filter by Client name if provided
    if client:
        invoices = [invoice for invoice in invoices if client.lower() in invoice["client"].lower()]

    # Filter by Min amount if provided
    if min_amount:
        invoices = [invoice for invoice in invoices if invoice["total"] >= min_amount]

    # Filter by Max amount if provided
    if max_amount:
        invoices = [invoice for invoice in invoices if invoice["total"] <= max_amount]
    
    return {
        "total": len(invoices),
        "client": client,
        "min_amount": min_amount,
        "max_amount": max_amount,
        "results": invoices
    }