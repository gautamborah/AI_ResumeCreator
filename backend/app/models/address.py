from pydantic import BaseModel, Field
from typing import Optional

class Address(BaseModel):
    street: str = Field(..., example="123 Main St")
    city: str = Field(..., example="San Francisco")
    state: Optional[str] = Field(None, example="CA")
    postal_code: str = Field(..., example="94105", alias="postalCode")
    country: str = Field(..., example="USA")