from fastapi import HTTPException
from app.firebase.firebase_app import firestore_db

from google.cloud.firestore_v1.base_document import DocumentSnapshot
from app.models.user import User
from app.models.role import Role


COLLECTION = "users"


def create_user(user: User) -> User:
    doc_ref = firestore_db.collection(COLLECTION).document(user.user_id)
    if doc_ref.get().exists:
        raise HTTPException(status_code=400, detail="User already exists")

    user_data = user.dict()
    user_data["role"] = user.role.value  # 🔐 Store role as string
    doc_ref.set(user_data)
    return user


def get_user(user_id: str) -> User:
    doc: DocumentSnapshot = firestore_db.collection(COLLECTION).document(user_id).get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="User not found")

    data = doc.to_dict()
    return User(**data)


def update_user(user: User) -> User:
    doc_ref = firestore_db.collection(COLLECTION).document(user.user_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="User not found")

    user_data = user.dict()
    user_data["role"] = user.role.value
    doc_ref.set(user_data)
    return user


def delete_user(user_id: str) -> dict:
    doc_ref = firestore_db.collection(COLLECTION).document(user_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="User not found")

    doc_ref.delete()
    return {"message": "User deleted"}


def list_users() -> list[User]:
    docs = firestore_db.collection(COLLECTION).stream()
    return [User(**doc.to_dict()) for doc in docs]
