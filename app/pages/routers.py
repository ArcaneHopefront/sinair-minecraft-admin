from fastapi import APIRouter

from app.pages.endpoints import root_router

pages_router = APIRouter()
pages_router.include_router(
    root_router,
    prefix='',
    tags=['Root']
)
