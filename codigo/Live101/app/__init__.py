from flask import Flask


def create_app():
    app = Flask(__name__)

    from .hello import bp_hello

    app.register_blueprint(bp_hello)

    return app
