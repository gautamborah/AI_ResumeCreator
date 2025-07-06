from pydantic import BaseModel

from app.models.role import Role

class SessionUser(BaseModel):
    user_id: str
    role: Role
