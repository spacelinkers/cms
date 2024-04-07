from fastapi import FastAPI

from app.core.config import settings
from app.apis.route_base import api_router


def include_router(app):
    app.include_router(api_router)

def init_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    return app


app = init_application()


@app.get("/")
def working():
    return {"msg": "It's WORKING"}