from fastapi import FastAPI

from app.pages.routers import pages_router


app = FastAPI()
app.include_router(pages_router)
