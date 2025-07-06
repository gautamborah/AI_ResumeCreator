from fastapi import HTTPException
from app.firebase.firebase_app import firestore_db
from app.models.profile import Profile  # Assuming model is in models/profile.py
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from typing import Optional

COLLECTION = "profiles"

def create_or_update_profile(user_id: str, profile: Profile) -> Profile:
    doc_ref = firestore_db.collection(COLLECTION).document(user_id)

    # Convert Pydantic model to dict and handle nested models
    profile_data = profile.dict(by_alias=True, exclude_unset=True)

    doc_ref.set(profile_data)
    return profile


def get_profile(user_id: str) -> Profile:
    doc_ref = firestore_db.collection(COLLECTION).document(user_id)
    doc: DocumentSnapshot = doc_ref.get()

    if not doc.exists:
        raise HTTPException(status_code=404, detail="Profile not found")

    data = doc.to_dict()
    return Profile(**data)


def delete_profile(user_id: str) -> dict:
    doc_ref = firestore_db.collection(COLLECTION).document(user_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="Profile not found")

    doc_ref.delete()
    return {"message": "Profile deleted"}


def update_profile(user_id: str, update_data: dict) -> Profile:
    doc_ref = firestore_db.collection(COLLECTION).document(user_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="Profile not found")

    doc_ref.update(update_data)
    updated_doc = doc_ref.get().to_dict()
    return Profile(**updated_doc)


def list_profiles() -> list[Profile]:
    docs = firestore_db.collection(COLLECTION).stream()
    return [Profile(**doc.to_dict()) for doc in docs]
