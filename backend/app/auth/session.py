from itsdangerous import URLSafeTimedSerializer, BadSignature
from app.models.role import Role
from app.models.sessionUser import SessionUser
from fastapi import Request, HTTPException, Depends, Path

SECRET_KEY = "3sCzxaz_5tG4lqhv7gkwgdzFlKbxqHESDoo-LvUEXxQ"
SESSION_COOKIE_NAME = "resume_session"
SESSION_MAX_AGE = 3600  # seconds

serializer = URLSafeTimedSerializer(SECRET_KEY)

def create_session_token(data: dict) -> str:
    return serializer.dumps(data)

def get_session_user(request: Request) -> SessionUser:
    token = request.cookies.get(SESSION_COOKIE_NAME)
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        data = serializer.loads(token, max_age=SESSION_MAX_AGE)
        user_id = data["user_id"]
        role = Role(data["role"])
        return SessionUser(user_id=user_id, role=role)
    except BadSignature:
        raise HTTPException(status_code=401, detail="Invalid session token")


def authorize_user_or_admin() -> SessionUser:
    def dependency(
        user_id: str = Path(...),
        current_user: SessionUser = Depends(get_session_user)
    ) -> SessionUser:
        if current_user.role == Role.admin:
            return current_user
        if current_user.user_id != user_id:
            raise HTTPException(status_code=403, detail="Forbidden")
        return current_user
    return dependency

def require_admin(user: SessionUser = Depends(get_session_user)):
    if user.role != Role.admin:
        raise HTTPException(status_code=403, detail="Admins only")
    return user