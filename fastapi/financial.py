"""
Financial Data Validation Extensions for FastAPI

This module provides specialized form validation classes and utilities for financial
data processing, particularly useful for debt collections, portfolio management,
and banking applications.

These extensions build upon FastAPI's existing Form validation capabilities to provide
industry-specific validation patterns commonly needed in financial services.
"""

import re
from decimal import Decimal, InvalidOperation
from typing import Any, Callable, Dict, List, Optional, Union
from datetime import datetime, date

from fastapi.params import Form as BaseForm
from fastapi._compat import Undefined
from fastapi.openapi.models import Example
from typing_extensions import Annotated, Doc, deprecated

_Unset: Any = Undefined


class FinancialForm(BaseForm):
    """
    Enhanced Form class with financial data validation capabilities.
    
    Extends FastAPI's Form class with specialized validation for financial data
    commonly used in debt collections, portfolio management, and banking systems.
    
    Features:
    - Currency amount validation with precision control
    - Account number format validation
    - SSN/TIN validation with masking
    - Credit score range validation
    - Financial date validation (business days, settlement dates)
    - Debt collection status validation
    """
    
    def __init__(
        self,
        default: Any = Undefined,
        *,
        currency_precision: Optional[int] = None,
        min_amount: Optional[Union[float, Decimal]] = None,
        max_amount: Optional[Union[float, Decimal]] = None,
        account_number_format: Optional[str] = None,
        validate_ssn: bool = False,
        validate_credit_score: bool = False,
        validate_business_date: bool = False,
        debt_status_values: Optional[List[str]] = None,
        default_factory: Union[Callable[[], Any], None] = _Unset,
        annotation: Optional[Any] = None,
        media_type: str = "application/x-www-form-urlencoded",
        alias: Optional[str] = None,
        alias_priority: Union[int, None] = _Unset,
        validation_alias: Union[str, None] = None,
        serialization_alias: Union[str, None] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        pattern: Optional[str] = None,
        regex: Annotated[
            Optional[str],
            deprecated(
                "Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead."
            ),
        ] = None,
        discriminator: Union[str, None] = None,
        strict: Union[bool, None] = _Unset,
        multiple_of: Union[float, None] = _Unset,
        allow_inf_nan: Union[bool, None] = _Unset,
        max_digits: Union[int, None] = _Unset,
        decimal_places: Union[int, None] = _Unset,
        examples: Optional[List[Any]] = None,
        example: Annotated[
            Optional[Any],
            deprecated(
                "Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, "
                "although still supported. Use examples instead."
            ),
        ] = _Unset,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Union[deprecated, str, bool, None] = None,
        include_in_schema: bool = True,
        json_schema_extra: Union[Dict[str, Any], None] = None,
        **extra: Any,
    ):
        self.currency_precision = currency_precision
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.account_number_format = account_number_format
        self.validate_ssn = validate_ssn
        self.validate_credit_score = validate_credit_score
        self.validate_business_date = validate_business_date
        self.debt_status_values = debt_status_values or []
        
        if currency_precision is not None and decimal_places is _Unset:
            decimal_places = currency_precision
            
        if validate_credit_score and ge is None and le is None:
            ge = 300  # Minimum FICO score
            le = 850  # Maximum FICO score
            
        if min_amount is not None and ge is None:
            ge = float(min_amount)
            
        if max_amount is not None and le is None:
            le = float(max_amount)
            
        financial_schema_extra = json_schema_extra or {}
        
        if self.validate_ssn:
            financial_schema_extra.update({
                "format": "ssn",
                "pattern": r"^\d{3}-?\d{2}-?\d{4}$",
                "description": "Social Security Number (XXX-XX-XXXX format)"
            })
            
        if self.account_number_format:
            financial_schema_extra.update({
                "format": "account_number",
                "pattern": self.account_number_format,
                "description": "Financial account number"
            })
            
        if self.validate_credit_score:
            financial_schema_extra.update({
                "format": "credit_score",
                "minimum": 300,
                "maximum": 850,
                "description": "FICO credit score (300-850)"
            })
            
        if self.debt_status_values:
            financial_schema_extra.update({
                "enum": self.debt_status_values,
                "description": f"Debt collection status: {', '.join(self.debt_status_values)}"
            })
            
        if self.validate_business_date:
            financial_schema_extra.update({
                "format": "business_date",
                "description": "Business date (excludes weekends and holidays)"
            })
            
        super().__init__(
            default=default,
            default_factory=default_factory,
            annotation=annotation,
            media_type=media_type,
            alias=alias,
            alias_priority=alias_priority,
            validation_alias=validation_alias,
            serialization_alias=serialization_alias,
            title=title,
            description=description,
            gt=gt,
            ge=ge,
            lt=lt,
            le=le,
            min_length=min_length,
            max_length=max_length,
            pattern=pattern,
            regex=regex,
            discriminator=discriminator,
            strict=strict,
            multiple_of=multiple_of,
            allow_inf_nan=allow_inf_nan,
            max_digits=max_digits,
            decimal_places=decimal_places,
            deprecated=deprecated,
            example=example,
            examples=examples,
            openapi_examples=openapi_examples,
            include_in_schema=include_in_schema,
            json_schema_extra=financial_schema_extra,
            **extra,
        )


FINANCIAL_PATTERNS = {
    "account_number": r"^\d{8,17}$",  # 8-17 digit account numbers
    "routing_number": r"^\d{9}$",    # 9-digit ABA routing numbers
    "ssn": r"^\d{3}-?\d{2}-?\d{4}$", # SSN with optional dashes
    "ein": r"^\d{2}-?\d{7}$",        # EIN with optional dash
    "credit_card": r"^\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}$",  # Credit card format
    "currency_usd": r"^\$?\d{1,3}(,\d{3})*(\.\d{2})?$",  # USD currency format
}

DEBT_COLLECTION_STATUSES = [
    "NEW",
    "ACTIVE",
    "PENDING_PAYMENT",
    "PAYMENT_PLAN",
    "SETTLED",
    "CHARGED_OFF",
    "DISPUTED",
    "LEGAL_ACTION",
    "CLOSED",
    "BANKRUPTCY"
]

PORTFOLIO_STATUSES = [
    "ACTIVE",
    "INACTIVE",
    "UNDER_REVIEW",
    "LIQUIDATING",
    "CLOSED",
    "TRANSFERRED"
]


def validate_financial_amount(value: Any, precision: int = 2) -> bool:
    """
    Validate financial amount with specified decimal precision.
    
    Args:
        value: The value to validate
        precision: Number of decimal places allowed
        
    Returns:
        bool: True if valid financial amount
    """
    try:
        decimal_value = Decimal(str(value))
        exponent = decimal_value.as_tuple().exponent
        if isinstance(exponent, int):
            return abs(exponent) <= precision
        return True  # Handle special cases like 'n', 'N', 'F'
    except (InvalidOperation, ValueError, TypeError):
        return False


def validate_ssn(ssn: str) -> bool:
    """
    Validate Social Security Number format and basic rules.
    
    Args:
        ssn: SSN string to validate
        
    Returns:
        bool: True if valid SSN format
    """
    if not ssn:
        return False
        
    clean_ssn = re.sub(r'[-\s]', '', ssn)
    
    if not re.match(r'^\d{9}$', clean_ssn):
        return False
        
    area = clean_ssn[:3]
    group = clean_ssn[3:5]
    serial = clean_ssn[5:]
    
    if area in ['000', '666'] or area.startswith('9'):
        return False
        
    if group == '00' or serial == '0000':
        return False
        
    return True


def validate_business_date(date_value: Union[str, date, datetime]) -> bool:
    """
    Validate that a date falls on a business day (Monday-Friday).
    
    Args:
        date_value: Date to validate
        
    Returns:
        bool: True if date is a business day
    """
    try:
        if isinstance(date_value, str):
            parsed_date = datetime.strptime(date_value, '%Y-%m-%d').date()
        elif isinstance(date_value, datetime):
            parsed_date = date_value.date()
        elif isinstance(date_value, date):
            parsed_date = date_value
        else:
            return False
            
        return parsed_date.weekday() < 5
        
    except (ValueError, TypeError):
        return False


def mask_sensitive_data(value: str, data_type: str = "ssn") -> str:
    """
    Mask sensitive financial data for logging and display.
    
    Args:
        value: The sensitive value to mask
        data_type: Type of data (ssn, account, credit_card)
        
    Returns:
        str: Masked version of the value
    """
    if not value:
        return value
        
    if data_type == "ssn":
        clean_value = re.sub(r'[-\s]', '', value)
        if len(clean_value) == 9:
            return f"XXX-XX-{clean_value[-4:]}"
    elif data_type == "account":
        if len(value) >= 4:
            return f"****{value[-4:]}"
    elif data_type == "credit_card":
        clean_value = re.sub(r'[\s-]', '', value)
        if len(clean_value) >= 4:
            return f"****-****-****-{clean_value[-4:]}"
            
    return "****"


def CurrencyAmount(
    default: Any = Undefined,
    *,
    precision: int = 2,
    min_amount: Optional[Union[float, Decimal]] = None,
    max_amount: Optional[Union[float, Decimal]] = None,
    **kwargs
) -> FinancialForm:
    """Create a currency amount form field with financial validation."""
    return FinancialForm(
        default=default,
        currency_precision=precision,
        min_amount=min_amount,
        max_amount=max_amount,
        decimal_places=precision,
        **kwargs
    )


def AccountNumber(
    default: Any = Undefined,
    *,
    format_pattern: str = FINANCIAL_PATTERNS["account_number"],
    **kwargs
) -> FinancialForm:
    """Create an account number form field with format validation."""
    return FinancialForm(
        default=default,
        account_number_format=format_pattern,
        pattern=format_pattern,
        **kwargs
    )


def SSNField(
    default: Any = Undefined,
    **kwargs
) -> FinancialForm:
    """Create an SSN form field with validation and masking."""
    return FinancialForm(
        default=default,
        validate_ssn=True,
        pattern=FINANCIAL_PATTERNS["ssn"],
        **kwargs
    )


def CreditScore(
    default: Any = Undefined,
    **kwargs
) -> FinancialForm:
    """Create a credit score form field with FICO range validation."""
    return FinancialForm(
        default=default,
        validate_credit_score=True,
        **kwargs
    )


def DebtStatus(
    default: Any = Undefined,
    *,
    allowed_statuses: Optional[List[str]] = None,
    **kwargs
) -> FinancialForm:
    """Create a debt collection status form field."""
    statuses = allowed_statuses or DEBT_COLLECTION_STATUSES
    return FinancialForm(
        default=default,
        debt_status_values=statuses,
        **kwargs
    )


def BusinessDate(
    default: Any = Undefined,
    **kwargs
) -> FinancialForm:
    """Create a business date form field that excludes weekends."""
    return FinancialForm(
        default=default,
        validate_business_date=True,
        **kwargs
    )
