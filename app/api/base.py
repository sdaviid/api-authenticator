from fastapi import APIRouter
from app.api.routes import route_auth
from app.api.routes import route_user
from app.api.routes import route_roles



api_router = APIRouter()
api_router.include_router(route_auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(route_user.router, prefix="/user", tags=["user"])
api_router.include_router(route_roles.router, prefix="/roles", tags=["roles"])