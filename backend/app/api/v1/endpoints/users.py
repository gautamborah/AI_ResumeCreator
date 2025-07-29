from fastapi import APIRouter, HTTPException, Request, Depends
from pydantic import BaseModel, EmailStr
from typing import List

from app.models.user import User
from app.models.role import Role
from app.models.sessionUser import SessionUser
from app.services.user_service import list_users, create_user, get_user, update_user

from app.auth.session import get_session_user, require_admin, authorize_user_or_admin

router = APIRouter(prefix="/users", tags=["users"])



@router.get("/", response_model=List[User])
def read_users_route(_: SessionUser = Depends(require_admin)):
    return list_users()

@router.post("/", response_model=User)
def create_user_route(user: User, _: SessionUser = Depends(require_admin)):
    return create_user(user)


@router.get("/{user_id}", response_model=User)
def get_user_route(
    user_id: str,
    _: SessionUser = Depends(authorize_user_or_admin())
):
    return get_user(user_id)

@router.put("/{user_id}", response_model=User)
def update_user_route(
    user_id: str,
    user: User,
    _: SessionUser = Depends(authorize_user_or_admin())
):
    return update_user(user)