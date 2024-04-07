from fastapi import APIRouter

from .v2 import route_post


api_router = APIRouter()


api_router.include_router(route_post.router, prefix="/posts", tags=["posts"])
