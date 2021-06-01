from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


class Message(BaseModel):
    message: str


dynamic_router = APIRouter()
templates = Jinja2Templates(directory='templates')


@dynamic_router.get('/dinamico')
def route(request: Request, response_classe=HTMLResponse):
    return templates.TemplateResponse(
        'dynamic.html', {'request': request}
    )


@dynamic_router.get('/dinamico/dado')
def route_b(request: Request, response_model=Message):
    from random import randint
    return {'message': randint(1, 100)}


@dynamic_router.get('/polling')
def route_c(request: Request, response_classe=HTMLResponse):
    return templates.TemplateResponse(
        'polling.html', {'request': request}
    )
