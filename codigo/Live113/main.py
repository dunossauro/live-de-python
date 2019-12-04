from fastapi import FastAPI
from a_fazer import router as a_fazer_router

app = FastAPI()


@app.get("/")
def ola_mundo():
    """
    View raiz, retorna {"ola": "mundo"}
    """
    return {"ola": "mundo"}


app.include_router(a_fazer_router, prefix="/a-fazer", tags=["todo"])
