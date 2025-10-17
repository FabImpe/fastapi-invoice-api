"""
Pydantic schemas for Payment validation.
"""
from pydantic import BaseModel, Field
from datetime import date
from enum import Enum


class PaymentMethod(str, Enum):
    """
    List of payment method

    Args:
        str: Ensures values are JSON-serializable as strings.
        Enum: Enables enumeration of allowed payment methods.

    Attributes:
        card (str): Payment by credit or debit card.
        bank_transfer (str): Payment via bank transfer.
        cash (str): Payment made in cash.

    Returns:
        PaymentMethod: A valid payment method enum member.
    """
    CARD = "card"
    BANK_TRANSFER = "bank_transfer"
    CASH = "cash"

class PaymentStatus(str, Enum):
    """
    List of payment status

    Args:
        str: Ensures values are JSON-serializable as strings.
        Enum: Enables enumeration of allowed payment status.

    Attributes:
        processed (str): The payment is processing.
        pending (str): The payment is pending.
        failed (str): The payment is failed.

    Returns:
        PaymentStatus: A valid payment status enum member.
    """
    PROCESSED = "processed"
    PENDING = "pending"
    FAILED = "failed"

class PaymentCreate(BaseModel):
    """Schema for creating a payment."""
    invoice_id: int = Field(..., gt=0, description="ID of the invoice being paid")
    amount: float = Field(..., gt=0, description="Payment amount")
    payment_date: date
    method: PaymentMethod

    class Config:
        json_schema_extra = {
            "example": {
                "invoice_id": 101,
                "amount": 1500.00,
                "payment_date": "2025-10-17",
                "method": "card"
            }
        }

class PaymentResponse(BaseModel):
    """Schema for payment response."""
    id: int
    invoice_id: int
    amount: float
    payment_date: date
    method: PaymentMethod
    status: PaymentStatus
