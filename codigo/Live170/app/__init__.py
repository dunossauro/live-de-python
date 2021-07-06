"""Factory da aplicação web."""

from flask import Flask

from .calc import soma


def create_app():
    """Constroi a aplicação."""
    app = Flask(__name__)

    @app.get("/soma/<int:x>/<int:y>")
    def home(x, y):
        return str(soma(x, y))

    return app
