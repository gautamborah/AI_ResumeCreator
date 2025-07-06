from fastapi import FastAPI
from .api.v1.endpoints import users, profile_routes
from .auth import login_routes

app = FastAPI()

app.include_router(users.router)
app.include_router(profile_routes.router)
app.include_router(login_routes.router)

