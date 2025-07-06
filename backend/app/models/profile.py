from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from app.models.address import Address
from app.models.education import Education

from app.models.skills import Skills

class Profile(BaseModel):
    first_name: Optional[str] = Field(default=None, alias="firstName")
    last_name: Optional[str] = Field(default=None, alias="lastName")
    contact_email: Optional[EmailStr] = Field(default=None, alias="contactEmail")
    phone: Optional[str] = Field(
        default=None,
        pattern=r'^\+?[1-9]\d{1,14}$',
        description="E.164 format phone number",
        alias="phone"
    )

    address: Optional[Address] = Field(default=None, alias="address")
    education: Optional[Education] = Field(default=None, alias="education")
    skills: Optional[Skills] = Field(default=None, alias="skills")
