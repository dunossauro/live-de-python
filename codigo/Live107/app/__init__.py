from flask import Flask, render_template
import os
from config import basedir

def create_app():
    app = Flask(__name__, 
        template_folder=os.path.join(basedir, "resources", "templates"), 
        static_folder=os.path.join(basedir, "resources", "static")
    )
    app.config["SECRET_KEY"] = 'secret'

    from app import routes
    routes.load(app)

    from app.filters import truncate
    app.jinja_env.filters["textTruncate"] = truncate

    def show_upper(text: str):
        return text.upper()

    @app.context_processor
    def inject_tempalte_function_and_variable():
        return dict(
            show_upper=show_upper,
            testing='testing variable created in __init__.py files'
        )

    return app
