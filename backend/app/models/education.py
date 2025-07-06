from pydantic import BaseModel, Field
from typing import Optional

class Education(BaseModel):
    school: Optional[str] = Field(default=None, alias="school")
    grade: Optional[str] = Field(default=None, alias="grade")
    gpa: Optional[str] = Field(default=None, alias="gpa")