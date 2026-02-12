from fastapi import FastAPI, staticfiles
from app.configuration import settings
from app.routes.routes import app as router
from app.configuration import init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="FastAPI CRUD", debug=settings.debug, docs_url="/api/docs", lifespan=lifespan
)


app.include_router(router)

app.mount(
    "/",
    staticfiles.StaticFiles(directory=settings.static_dir, html=True),
    name="static",
)
