import uvicorn
from fastapi import FastAPI

from app.pages.routers import pages_router
from app.core.config import settings


app = FastAPI(title=settings.app_title)
app.include_router(pages_router)

if __name__ == '__main__':
    uvicorn.run(
        'app.main:app',
        host=settings.host,
        port=settings.http_port,
        reload=True
    )
