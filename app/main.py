from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Sangwin's - FastAPI CRUD Boilerplate")

app.include_router(router)