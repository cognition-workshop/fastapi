# Financial Data Validation

FastAPI provides specialized form validation capabilities for financial applications, particularly useful for debt collections, portfolio management, and banking systems.

## Financial Form Extensions

The `fastapi.financial` module extends FastAPI's standard form validation with financial industry-specific patterns and validation rules.

### Basic Financial Form

```python
from typing import Annotated
from fastapi import FastAPI
from fastapi.financial import FinancialForm

app = FastAPI()

@app.post("/debt-record/")
def create_debt_record(
    debt_amount: Annotated[float, FinancialForm(
        currency_precision=2,
        min_amount=0.01,
        max_amount=1000000.00,
        title="Debt Amount",
        description="Outstanding debt amount in USD"
    )]
):
    return {"debt_amount": debt_amount}
```

## Currency Amount Validation

For precise financial calculations, use the `CurrencyAmount` helper:

```python
from fastapi.financial import CurrencyAmount
from decimal import Decimal

@app.post("/payment/")
def process_payment(
    amount: Annotated[Decimal, CurrencyAmount(
        precision=2,
        min_amount=Decimal("0.01"),
        max_amount=Decimal("50000.00")
    )]
):
    return {"payment_processed": str(amount)}
```

## Account Number Validation

Validate financial account numbers with format patterns:

```python
from fastapi.financial import AccountNumber

@app.post("/account/")
def create_account(
    account_number: Annotated[str, AccountNumber(
        title="Account Number",
        description="8-17 digit account identifier"
    )]
):
    return {"account": account_number}
```

## SSN Validation with Masking

Handle Social Security Numbers with built-in validation and masking:

```python
from fastapi.financial import SSNField, mask_sensitive_data

@app.post("/customer/")
def create_customer(
    ssn: Annotated[str, SSNField(title="Social Security Number")]
):
    # Automatically masks SSN in logs and responses
    masked_ssn = mask_sensitive_data(ssn, "ssn")
    return {"customer_ssn": masked_ssn}  # Returns: XXX-XX-1234
```

## Credit Score Validation

Validate FICO credit scores with proper range checking:

```python
from fastapi.financial import CreditScore

@app.post("/credit-check/")
def credit_assessment(
    score: Annotated[int, CreditScore(
        title="FICO Credit Score",
        description="Credit score between 300-850"
    )]
):
    return {"credit_score": score, "rating": get_credit_rating(score)}
```

## Debt Collection Status

Manage debt collection workflows with predefined status values:

```python
from fastapi.financial import DebtStatus, DEBT_COLLECTION_STATUSES

@app.post("/debt-status/")
def update_debt_status(
    status: Annotated[str, DebtStatus(
        title="Collection Status",
        description=f"Valid statuses: {', '.join(DEBT_COLLECTION_STATUSES)}"
    )]
):
    return {"status_updated": status}
```

## Business Date Validation

Ensure dates fall on business days for settlement and processing:

```python
from fastapi.financial import BusinessDate

@app.post("/settlement/")
def schedule_settlement(
    settlement_date: Annotated[str, BusinessDate(
        title="Settlement Date",
        description="Must be a business day (Monday-Friday)"
    )]
):
    return {"settlement_scheduled": settlement_date}
```

## Complete Debt Collection Example

Here's a comprehensive example for a debt collection system:

```python
from typing import Annotated
from fastapi import FastAPI
from fastapi.financial import (
    CurrencyAmount, AccountNumber, SSNField, CreditScore, 
    DebtStatus, BusinessDate, mask_sensitive_data
)
from decimal import Decimal

app = FastAPI(title="Debt Collection API")

@app.post("/debt-collection/create/")
def create_debt_record(
    debtor_ssn: Annotated[str, SSNField(
        title="Debtor SSN",
        description="Social Security Number of the debtor"
    )],
    debt_amount: Annotated[Decimal, CurrencyAmount(
        precision=2,
        min_amount=Decimal("0.01"),
        max_amount=Decimal("1000000.00"),
        title="Outstanding Debt",
        description="Total amount owed by debtor"
    )],
    original_creditor_account: Annotated[str, AccountNumber(
        title="Original Creditor Account",
        description="Account number from original creditor"
    )],
    debtor_credit_score: Annotated[int, CreditScore(
        title="Debtor Credit Score",
        description="Most recent FICO score"
    )],
    collection_status: Annotated[str, DebtStatus(
        title="Collection Status",
        description="Current status in collection workflow"
    )],
    next_contact_date: Annotated[str, BusinessDate(
        title="Next Contact Date",
        description="Next scheduled contact date (business days only)"
    )]
):
    """
    Create a new debt collection record with comprehensive validation.
    
    This endpoint demonstrates financial data validation patterns commonly
    used in debt collection and portfolio management systems.
    """
    return {
        "record_created": True,
        "debtor_ssn": mask_sensitive_data(debtor_ssn, "ssn"),
        "debt_amount": str(debt_amount),
        "account": mask_sensitive_data(original_creditor_account, "account"),
        "credit_score": debtor_credit_score,
        "status": collection_status,
        "next_contact": next_contact_date
    }

@app.get("/debt-collection/statuses/")
def get_valid_statuses():
    """Get all valid debt collection status values."""
    from fastapi.financial import DEBT_COLLECTION_STATUSES
    return {"valid_statuses": DEBT_COLLECTION_STATUSES}
```

## Validation Utilities

The financial module also provides utility functions for custom validation:

```python
from fastapi.financial import (
    validate_financial_amount,
    validate_ssn,
    validate_business_date,
    mask_sensitive_data
)

# Validate currency amounts
is_valid = validate_financial_amount("123.45", precision=2)  # True
is_valid = validate_financial_amount("123.456", precision=2)  # False

# Validate SSN format and rules
is_valid = validate_ssn("123-45-6789")  # True
is_valid = validate_ssn("000-45-6789")  # False (invalid area code)

# Validate business dates
is_valid = validate_business_date("2024-01-15")  # True (Monday)
is_valid = validate_business_date("2024-01-13")  # False (Saturday)

# Mask sensitive data
masked = mask_sensitive_data("123-45-6789", "ssn")  # "XXX-XX-6789"
masked = mask_sensitive_data("1234567890", "account")  # "****7890"
```

## OpenAPI Documentation

Financial forms automatically generate enhanced OpenAPI documentation with:

- Format specifications for financial data types
- Validation ranges for amounts and scores  
- Enumerated values for status fields
- Pattern validation for account numbers and SSNs
- Business rules documentation

The generated API documentation will show proper validation rules and examples for each financial field type, making it easy for frontend developers and API consumers to understand the expected data formats.

## Business Value

These financial validation extensions provide several benefits for financial services applications:

### Compliance and Risk Management
- Automatic SSN format validation and masking for PII protection
- Credit score range validation ensures data integrity
- Business date validation prevents weekend processing errors

### Data Quality and Consistency
- Standardized currency precision handling prevents rounding errors
- Account number format validation ensures consistent data entry
- Predefined status values prevent invalid workflow states

### Developer Experience
- Type-safe financial data handling with clear validation rules
- Automatic OpenAPI documentation generation
- Reusable validation patterns across financial applications

### Integration with Debt Collection Systems
- Purpose-built for debt collection and portfolio management workflows
- Supports common financial data patterns and validation rules
- Enables secure handling of sensitive financial information
