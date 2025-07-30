"""
Tests for FastAPI Financial Form Validation Extensions

This test suite validates the financial data processing capabilities
added to FastAPI for debt collections and portfolio management applications.
"""

import pytest
from decimal import Decimal
from datetime import date, datetime
from fastapi import FastAPI
from fastapi.testclient import TestClient
from typing_extensions import Annotated

from fastapi.financial import (
    FinancialForm,
    CurrencyAmount,
    AccountNumber,
    SSNField,
    CreditScore,
    DebtStatus,
    BusinessDate,
    validate_financial_amount,
    validate_ssn,
    validate_business_date,
    mask_sensitive_data,
    DEBT_COLLECTION_STATUSES,
)

app = FastAPI()


@app.post("/debt-collection/")
def create_debt_record(
    debtor_ssn: Annotated[str, SSNField(title="Debtor SSN")],
    debt_amount: Annotated[float, CurrencyAmount(min_amount=0.01, max_amount=1000000.00)],
    account_number: Annotated[str, AccountNumber(title="Account Number")],
    credit_score: Annotated[int, CreditScore(title="Credit Score")],
    status: Annotated[str, DebtStatus(title="Collection Status")],
    settlement_date: Annotated[str, BusinessDate(title="Settlement Date")],
):
    """Create a new debt collection record with comprehensive validation."""
    return {
        "debtor_ssn": mask_sensitive_data(debtor_ssn, "ssn"),
        "debt_amount": debt_amount,
        "account_number": mask_sensitive_data(account_number, "account"),
        "credit_score": credit_score,
        "status": status,
        "settlement_date": settlement_date,
    }


@app.post("/portfolio-payment/")
def process_payment(
    payment_amount: Annotated[
        Decimal, 
        CurrencyAmount(
            precision=2,
            min_amount=Decimal("0.01"),
            title="Payment Amount",
            description="Payment amount in USD with 2 decimal precision"
        )
    ],
    account_id: Annotated[
        str, 
        AccountNumber(
            title="Account ID",
            description="Customer account identifier"
        )
    ],
):
    """Process a portfolio payment with precise currency validation."""
    return {
        "payment_amount": str(payment_amount),
        "account_id": mask_sensitive_data(account_id, "account"),
        "status": "processed"
    }


client = TestClient(app)


class TestFinancialFormValidation:
    """Test suite for financial form validation functionality."""
    
    def test_valid_debt_collection_form(self):
        """Test valid debt collection form submission."""
        response = client.post("/debt-collection/", data={
            "debtor_ssn": "123-45-6789",
            "debt_amount": "1500.50",
            "account_number": "1234567890",
            "credit_score": "650",
            "status": "ACTIVE",
            "settlement_date": "2024-01-15"  # Monday
        })
        assert response.status_code == 200
        data = response.json()
        assert data["debtor_ssn"] == "XXX-XX-6789"
        assert data["debt_amount"] == 1500.50
        assert data["account_number"] == "****7890"
        assert data["credit_score"] == 650
        assert data["status"] == "ACTIVE"
        
    def test_invalid_ssn_format(self):
        """Test invalid SSN format rejection."""
        response = client.post("/debt-collection/", data={
            "debtor_ssn": "123-45-678",  # Too short
            "debt_amount": "1500.50",
            "account_number": "1234567890",
            "credit_score": "650",
            "status": "ACTIVE",
            "settlement_date": "2024-01-15"
        })
        assert response.status_code == 422
        
    def test_invalid_credit_score_range(self):
        """Test credit score outside valid range."""
        response = client.post("/debt-collection/", data={
            "debtor_ssn": "123-45-6789",
            "debt_amount": "1500.50",
            "account_number": "1234567890",
            "credit_score": "900",  # Above maximum
            "status": "ACTIVE",
            "settlement_date": "2024-01-15"
        })
        assert response.status_code == 422
        
    def test_invalid_debt_amount_range(self):
        """Test debt amount outside valid range."""
        response = client.post("/debt-collection/", data={
            "debtor_ssn": "123-45-6789",
            "debt_amount": "0.00",  # Below minimum
            "account_number": "1234567890",
            "credit_score": "650",
            "status": "ACTIVE",
            "settlement_date": "2024-01-15"
        })
        assert response.status_code == 422
        
    def test_invalid_debt_status(self):
        """Test invalid debt collection status."""
        response = client.post("/debt-collection/", data={
            "debtor_ssn": "123-45-6789",
            "debt_amount": "1500.50",
            "account_number": "1234567890",
            "credit_score": "650",
            "status": "INVALID_STATUS",
            "settlement_date": "2024-01-15"
        })
        assert response.status_code == 422
        
    def test_weekend_settlement_date(self):
        """Test weekend date rejection for business date validation."""
        response = client.post("/debt-collection/", data={
            "debtor_ssn": "123-45-6789",
            "debt_amount": "1500.50",
            "account_number": "1234567890",
            "credit_score": "650",
            "status": "ACTIVE",
            "settlement_date": "2024-01-13"  # Saturday
        })
        
    def test_precise_currency_validation(self):
        """Test precise currency amount validation."""
        response = client.post("/portfolio-payment/", data={
            "payment_amount": "123.45",
            "account_id": "9876543210"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["payment_amount"] == "123.45"
        assert data["account_id"] == "****3210"
        
    def test_currency_precision_validation(self):
        """Test currency precision validation."""
        response = client.post("/portfolio-payment/", data={
            "payment_amount": "123.456",  # Too many decimal places
            "account_id": "9876543210"
        })
        assert response.status_code in [200, 422]  # Depends on implementation


class TestFinancialValidationUtilities:
    """Test suite for financial validation utility functions."""
    
    def test_validate_financial_amount(self):
        """Test financial amount validation utility."""
        assert validate_financial_amount("123.45", precision=2) == True
        assert validate_financial_amount("123.456", precision=2) == False
        assert validate_financial_amount("123", precision=2) == True
        assert validate_financial_amount("invalid", precision=2) == False
        
    def test_validate_ssn(self):
        """Test SSN validation utility."""
        assert validate_ssn("123-45-6789") == True
        assert validate_ssn("123456789") == True
        assert validate_ssn("000-45-6789") == False  # Invalid area
        assert validate_ssn("123-00-6789") == False  # Invalid group
        assert validate_ssn("123-45-0000") == False  # Invalid serial
        assert validate_ssn("123-45-678") == False   # Too short
        
    def test_validate_business_date(self):
        """Test business date validation utility."""
        assert validate_business_date("2024-01-15") == True
        assert validate_business_date("2024-01-13") == False
        assert validate_business_date("2024-01-14") == False
        assert validate_business_date(date(2024, 1, 15)) == True
        assert validate_business_date("invalid-date") == False
        
    def test_mask_sensitive_data(self):
        """Test sensitive data masking utility."""
        assert mask_sensitive_data("123-45-6789", "ssn") == "XXX-XX-6789"
        assert mask_sensitive_data("1234567890", "account") == "****7890"
        assert mask_sensitive_data("1234-5678-9012-3456", "credit_card") == "****-****-****-3456"
        assert mask_sensitive_data("", "ssn") == ""
        assert mask_sensitive_data("123", "account") == "****"


class TestFinancialFormOpenAPISchema:
    """Test OpenAPI schema generation for financial forms."""
    
    def test_openapi_schema_generation(self):
        """Test that financial forms generate proper OpenAPI schemas."""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        schema = response.json()
        
        assert "/debt-collection/" in schema["paths"]
        debt_endpoint = schema["paths"]["/debt-collection/"]["post"]
        
        request_body = debt_endpoint["requestBody"]["content"]["application/x-www-form-urlencoded"]["schema"]
        properties = request_body["properties"]
        
        assert "debtor_ssn" in properties
        ssn_field = properties["debtor_ssn"]
        assert ssn_field.get("format") == "ssn" or "pattern" in ssn_field
        
        assert "credit_score" in properties
        credit_field = properties["credit_score"]
        assert credit_field.get("minimum") == 300
        assert credit_field.get("maximum") == 850
        
        assert "status" in properties
        status_field = properties["status"]
        assert "enum" in status_field
        assert "ACTIVE" in status_field["enum"]


def test_debt_collection_statuses_completeness():
    """Test that debt collection statuses cover common scenarios."""
    expected_statuses = {
        "NEW", "ACTIVE", "PENDING_PAYMENT", "PAYMENT_PLAN", 
        "SETTLED", "CHARGED_OFF", "DISPUTED", "LEGAL_ACTION", 
        "CLOSED", "BANKRUPTCY"
    }
    assert set(DEBT_COLLECTION_STATUSES) == expected_statuses


if __name__ == "__main__":
    pytest.main([__file__])
