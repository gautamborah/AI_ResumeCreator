from fastapi import APIRouter, Form, Response, HTTPException, Request
from .session import create_session_token, get_session_user, SESSION_COOKIE_NAME
from app.firebase.firebase_app import firestore_db

from app.models.sessionUser import SessionUser

router = APIRouter()

def authenticate(user_id: str, password: str) -> SessionUser:
    # Replace with your real auth logic or Firebase Auth
    doc_ref = firestore_db.collection("users").document(user_id)
    doc = doc_ref.get()
    
    if not doc.exists:
        raise HTTPException(status_code=404, detail="User not found")
    
    data = doc.to_dict()
    if data["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    print("data=", data)
    return SessionUser(**data)

@router.post("/login")
def login(response: Response, user_id: str = Form(...), password: str = Form(...)):
    sessionUser = authenticate(user_id, password)
    token = create_session_token({"user_id": sessionUser.user_id, "role": sessionUser.role})
    response.set_cookie(key=SESSION_COOKIE_NAME, value=token, httponly=True, max_age=3600)
    return {"message": "Login successful", "role": sessionUser.role}

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(SESSION_COOKIE_NAME)
    return {"message": "Logged out"}

@router.get("/me")
def read_me(request: Request):
    user = get_session_user(request)
    return {"user": user}
