from fastapi import FastAPI
from core.config import Settings

def init_application():
    app = FastAPI(title=Settings.PROJECT_TITLE, version=Settings.PROJECT_VERSION)

    return app


app = init_application()
