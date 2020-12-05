from starlette.requests import Request
from starlette.responses import JSONResponse
from app.models import User
from werkzeug.security import generate_password_hash


async def users(request: Request):
    contents = await User.objects.all()
    results = [
        {
            "id": content.id,
            "name": content.name,
            "email": content.email,
            "password": content.password,
        }
        for content in contents
    ]
    return JSONResponse(results)


async def create(request: Request):
    payload = await request.json()
    try:
        await User.objects.create(
            name=payload["name"],
            email=payload["email"],
            password=generate_password_hash(payload["password"]),
        )
        return JSONResponse(
            {"msg": "usuario inserido com sucesso!"}, status_code=201
        )
    except Exception as e:
        print(str(e))
        return JSONResponse(
            {"msg": "não foi possível inserir o usuário"}, status_code=500
        )
