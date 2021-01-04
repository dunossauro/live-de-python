import uvicorn
from starlette.applications import Starlette

from app.routes import routes
from app.database import sqlalchemy, database, metadata


engine = sqlalchemy.create_engine(str(database.url))
metadata.create_all(engine)


app = Starlette(
    debug=True,
    routes=routes,
    on_startup=[database.connect],
    on_shutdown=[database.disconnect],
)


if __name__ == "__main__":
    uvicorn.run("run:app", reload=True, port=5000)
