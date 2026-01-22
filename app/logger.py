import logging
from logging.handlers import RotatingFileHandler
import json
import os
from datetime import datetime, timezone

# Create logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "api_timing.log")


class JsonFormatter(logging.Formatter):
    """
    Custom JSON formatter for structured logging
    """

    def format(self, record: logging.LogRecord) -> str:
        log_record = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
        }

        # Include extra fields if present
        if hasattr(record, "extra"):
            log_record.update(record.extra)

        return json.dumps(log_record)


logger = logging.getLogger("api_timing_logger")
logger.setLevel(logging.INFO)

# Prevent duplicate handlers
if not logger.handlers:
    formatter = JsonFormatter()

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File handler with rotation
    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=5_000_000, backupCount=5
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
