from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.logger import logger
from datetime import datetime, timezone


def error_response(message: str, status_code: int, path: str):
    """
    Standard error response structure
    """
    return {
        "success": False,
        "error": {
            "message": message,
            "status_code": status_code,
            "path": path,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }


# ============================
# HTTP Exceptions (manual raise)
# ============================
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(
        "HTTPException",
        extra={
            "extra": {
                "path": request.url.path,
                "method": request.method,
                "status_code": exc.status_code,
                "detail": exc.detail,
            }
        }
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=error_response(str(exc.detail), exc.status_code, request.url.path)
    )


# ============================
# Validation Errors (Pydantic)
# ============================
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(
        "ValidationError",
        extra={
            "extra": {
                "path": request.url.path,
                "method": request.method,
                "errors": exc.errors(),
            }
        }
    )

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": {
                "message": "Validation failed",
                "details": exc.errors(),
                "status_code": 422,
                "path": request.url.path,
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }
    )


# ============================
# Starlette HTTP Errors
# ============================
async def starlette_http_exception_handler(request: Request, exc: StarletteHTTPException):
    logger.error(
        "StarletteHTTPException",
        extra={
            "extra": {
                "path": request.url.path,
                "method": request.method,
                "status_code": exc.status_code,
                "detail": exc.detail,
            }
        }
    )

    return JSONResponse(
        status_code=exc.status_code,
        content=error_response(str(exc.detail), exc.status_code, request.url.path)
    )


# ============================
# Global Fallback (500 errors)
# ============================
async def global_exception_handler(request: Request, exc: Exception):
    logger.critical(
        "UnhandledException",
        extra={
            "extra": {
                "path": request.url.path,
                "method": request.method,
                "error": str(exc),
                "type": type(exc).__name__,
            }
        }
    )

    return JSONResponse(
        status_code=500,
        content=error_response(
            "Internal server error",
            500,
            request.url.path
        )
    )
