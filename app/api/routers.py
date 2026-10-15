from fastapi import APIRouter

from app.api.endpoints import root_router

main_router = APIRouter()
main_router.include_router(
    root_router,
    prefix='',
    tags=['Main']
)
