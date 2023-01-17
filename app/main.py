from fastapi import FastAPI
from .core.config import settings
from .db.seesion import engine
from .db.base import Base
from .api.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app


app = start_application()
