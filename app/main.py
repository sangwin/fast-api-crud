from fastapi import FastAPI
from app.routes import router
from app.middleware import timing_middleware

app = FastAPI(title="Sangwin's - FastAPI CRUD Boilerplate")

# Register middleware
app.middleware("http")(timing_middleware)

app.include_router(router)