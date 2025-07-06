from pydantic import BaseModel, EmailStr
from typing import Optional

from app.models.role import Role

class User(BaseModel):
    user_id: str
    password: str
    role: Role
