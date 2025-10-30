# /// script
# dependencies = ["uvicorn", "timing-asgi"]
# ///
from pprint import pp
import uvicorn
from timing_asgi import TimingMiddleware, TimingClient

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


class PrintTimings(TimingClient):
    def timing(self, metric_name, timing, tags):
        print(metric_name, timing, tags)

appt = TimingMiddleware(app, PrintTimings())


uvicorn.run(appt)
