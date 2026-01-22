import time
from datetime import datetime, timezone
from fastapi import Request
from app.logger import logger

async def timing_middleware(request: Request, call_next):
    start_time = time.time()
    start_timestamp = datetime.now(timezone.utc).isoformat()

    response = await call_next(request)

    end_time = time.time()
    end_timestamp = datetime.now(timezone.utc).isoformat()
    process_time_ms = (end_time - start_time)

    # Structured log payload
    logger.info(
        "API request completed",
        extra={
            "extra": {
                "http_method": request.method,
                "path": request.url.path,
                "start_time": start_timestamp,
                "end_time": end_timestamp,
                "duration_ms": round(process_time_ms, 5),
                "status_code": response.status_code,
            }
        }
    )

    # Response headers
    response.headers["X-API-Start-Time"] = start_timestamp
    response.headers["X-API-End-Time"] = end_timestamp
    response.headers["X-Process-Time-ms"] = f"{process_time_ms:.2f}"

    return response
