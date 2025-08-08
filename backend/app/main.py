from fastapi import FastAPI
from .api.v1.endpoints import users, profile_routes
from .auth import login_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # your React frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(profile_routes.router)
app.include_router(login_routes.router)

