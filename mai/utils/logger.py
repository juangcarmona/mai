import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter

# Constants
DEFAULT_LOG_DIR = Path("logs")
DEFAULT_LOG_FILE = DEFAULT_LOG_DIR / "app.log"
DEFAULT_LOG_NAME = "mai"

# Logger instance (singleton)
_logger_instance = None

def configure_logger(
    name: str = DEFAULT_LOG_NAME,
    log_dir: Path = DEFAULT_LOG_DIR,
    log_file: Path = DEFAULT_LOG_FILE,
) -> logging.Logger:
    """Configure and return a logger with both file and console handlers (singleton)."""
    global _logger_instance

    if _logger_instance:
        # Return the existing logger if already configured
        return _logger_instance

    # Create the logger
    logger = logging.getLogger(f"mai::{name}")
    logger.setLevel(logging.DEBUG)  # Capture all levels (DEBUG and higher)

    # Ensure the log directory exists
    log_dir.mkdir(exist_ok=True)

    # File handler (rotating logs)
    file_handler = RotatingFileHandler(
        log_file, maxBytes=1024 * 1024, backupCount=5, encoding="utf-8"
    )
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    file_handler.setLevel(logging.DEBUG)

    # Console handler (colored output)
    console_handler = logging.StreamHandler(sys.stdout)
    console_formatter = ColoredFormatter(
        "%(log_color)s%(levelname)s - %(name)s - %(message)s",
        log_colors={
            "DEBUG": "white",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.INFO)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Store the singleton instance
    _logger_instance = logger

    return logger


def get_logger(name: str = DEFAULT_LOG_NAME) -> logging.Logger:
    """Get a configured logger instance (singleton)."""
    return configure_logger(name=name)
