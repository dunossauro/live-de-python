from starlette.routing import Route, Mount

from app.controllers import home_controller, user_controller

routes = [
    Route("/", endpoint=home_controller.home),
    Route("/echo", endpoint=home_controller.echo),
    Mount(
        "/users",
        routes=[
            Route("/", endpoint=user_controller.users),
            Route("/", endpoint=user_controller.create, methods=["POST"]),
        ],
    ),
]
