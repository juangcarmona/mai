import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler

def configure_logger(name: str = "bluesky-poster") -> logging.Logger:
    """Configure and return a logger with both file and console handlers"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set to lowest level
    
    # Create logs directory if not exists
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    # File handler (rotating logs)
    file_handler = RotatingFileHandler(
        logs_dir / "app.log",
        maxBytes=1024 * 1024,  # 1MB
        backupCount=5,
        encoding="utf-8"
    )
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    ))
    file_handler.setLevel(logging.DEBUG)

    # Console handler (colored output)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(
        "%(levelname)s - %(message)s"
    ))
    console_handler.setLevel(logging.INFO)  # Default to INFO for console

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def get_logger(name: str = "bluesky-poster") -> logging.Logger:
    """Get a configured logger instance"""
    return logging.getLogger(name)