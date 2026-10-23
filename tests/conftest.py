import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from app.main import app

BASE_TEST_URL = "http://test"


@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(
        transport=transport,
        base_url=BASE_TEST_URL
    ) as client:
        yield client
