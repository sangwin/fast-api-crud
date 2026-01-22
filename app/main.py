from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

# from app.routes import router
from app.routers import users, auth

from app.middleware import timing_middleware
from app.error_handler import (
    http_exception_handler,
    validation_exception_handler,
    starlette_http_exception_handler,
    global_exception_handler
)

app = FastAPI(title="Sangwin's - FastAPI CRUD Boilerplate")

# Register middleware
app.middleware("http")(timing_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # "https://mydomain.com"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
# app.include_router(router)
app.include_router(auth.router)
app.include_router(users.router)


# ======================
# Error Handlers
# ======================
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(StarletteHTTPException, starlette_http_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)