from fastapi import FastAPI
from .core.config import settings

def init_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

    return app


app = init_application()


@app.get("/")
def working():
    return {"msg": "It's WORKING"}