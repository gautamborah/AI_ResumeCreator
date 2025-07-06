from fastapi import APIRouter, HTTPException, Path, Body
from typing import List
from app.models.profile import Profile
from app.services.profile_service import (
    create_or_update_profile,
    get_profile,
    update_profile,
    delete_profile,
    list_profiles,
)

router = APIRouter(prefix="/profiles", tags=["profiles"])

@router.post("/{user_id}", response_model=Profile)
def create_profile(
    user_id: str = Path(..., description="User ID to create profile for"),
    profile: Profile = Body(...),
):
    return create_or_update_profile(user_id, profile)

@router.get("/{user_id}", response_model=Profile)
def read_profile(user_id: str = Path(..., description="User ID to fetch profile")):
    return get_profile(user_id)

@router.put("/{user_id}", response_model=Profile)
def put_update_profile(
    user_id: str = Path(...),
    profile: Profile = Body(...),
):
    # Full update (overwrite)
    return create_or_update_profile(user_id, profile)

@router.patch("/{user_id}", response_model=Profile)
def patch_update_profile(
    user_id: str = Path(...),
    update_data: dict = Body(..., description="Fields to update"),
):
    # Partial update
    return update_profile(user_id, update_data)

@router.delete("/{user_id}")
def delete_profile_route(user_id: str = Path(...)):
    return delete_profile(user_id)

@router.get("/", response_model=List[Profile])
def list_all_profiles():
    return list_profiles()
