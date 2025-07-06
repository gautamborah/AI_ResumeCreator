from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, EmailStr
from typing import List

from app.models.user import User
from app.models.role import Role
from app.services.user_service import list_users, create_user, get_user, update_user

from app.auth.session import get_session_user

router = APIRouter()

@router.get("/users/", response_model=List[User])
def read_users_route(request: Request):
    sessionUser = get_session_user(request)
    role = sessionUser.role
    if role != Role.admin:
        raise HTTPException(status_code=403, detail="Admins only")
    return list_users()

@router.post("/users/", response_model=User)
def create_user_route(user: User):
    user_data = user.dict()
    user_data["role"] = str(user.role.value)

    return create_user(user)

@router.get("/users/{user_id}", response_model=User)
def get_user_route(request: Request, user_id: str):
    sessionUser = get_session_user(request)
    if sessionUser.user_id != user_id:
        raise HTTPException(status_code=403, detail="User not matching")

    return get_user(user_id)


@router.put("/users/{user_id}", response_model=User)
def update_user(email: str, user: User):
    return update_user(user)
