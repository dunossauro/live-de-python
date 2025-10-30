# /// script
# dependencies = ["pytest", "pytest-asyncio", "httpx"]
# ///
async def app(scope, receive, send):
    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": [(b"Content-Type", b"text/plain")],
    })
    await send({
        "type": "http.response.body",
        "body": b"Ola mundo :)",
    })


from httpx import AsyncClient, ASGITransport
import pytest

@pytest.mark.asyncio
async def test_homepage():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://testserver"
    ) as client:
        breakpoint()
        response = await client.get('/')
    
    assert response.status_code == 200
    assert 'ola' in response.text
