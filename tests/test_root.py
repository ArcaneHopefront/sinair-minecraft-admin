import pytest

from http import HTTPStatus

ROOT_URL = '/'


@pytest.mark.anyio
async def test_get_root(client):
    response = await client.get(ROOT_URL)
    assert response.status_code == HTTPStatus.OK, (
        f'GET-запрос обычного пользователя к эндпоинту "{ROOT_URL}" '
        'должен возвращать статус-код 200.'
    )
