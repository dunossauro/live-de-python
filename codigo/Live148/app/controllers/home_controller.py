from starlette.responses import PlainTextResponse


async def home(request):
    return PlainTextResponse("ola")


async def echo(request):
    return PlainTextResponse("echo man!")
