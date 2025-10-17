"""
Pydantic schemas for Invoice validation.
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class InvoiceItemCreate(BaseModel):
    """Schema for creating an invoice item."""
    description: str = Field(..., min_length=1, max_length=200)
    quantity: int = Field(..., gt=0)
    unit_price: float = Field(..., gt=0)


class InvoiceCreate(BaseModel):
    """Schema for creating an invoice."""
    client: str = Field(..., min_length=1, max_length=100)
    due_date: date
    items: list[InvoiceItemCreate]
    notes: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "client": "Acme Corp",
                "due_date": "2025-11-30",
                "items": [
                    {
                        "description": "Consulting services",
                        "quantity": 10,
                        "unit_price": 150.00
                    },
                    {
                        "description": "Software license",
                        "quantity": 1,
                        "unit_price": 500.00
                    }
                ],
                "notes": "Payment due within 30 days"
            }
        }


class InvoiceResponse(BaseModel):
    """Schema for invoice response."""
    id: int
    client: str
    invoice_number: str
    due_date: date
    total: float
    status: str
    items_count: int