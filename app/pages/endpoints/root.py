from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get(
    '/',
    response_class=HTMLResponse
)
async def reed_root():
    return '<h1>Hello, world!<h1>'
