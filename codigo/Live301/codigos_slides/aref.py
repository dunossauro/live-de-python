# /// script
# dependencies = ["uvicorn"]
# ///
from pprint import pp
import uvicorn

async def app(scope, receive, send):
    pp(scope)

    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": [(b"Content-Type", b"text/plain")],
    })
    await send({
        "type": "http.response.body",
        "body": b"Ola mundo :)",
    })


uvicorn.run(app)
