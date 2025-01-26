from atproto import Client
from dotenv import load_dotenv
import os
from bluesky_poster.logger import get_logger

logger = get_logger("auth")

def authenticate() -> Client:
    """Authenticate with Bluesky using atproto client"""
    logger.debug("Starting authentication process")
    load_dotenv()
    
    try:
        client = Client()
        client.login(
            os.getenv("BLUESKY_HANDLE"),
            os.getenv("BLUESKY_APP_PASSWORD")
        )
        logger.info("Successfully authenticated with Bluesky")
        return client
    except Exception as e:
        logger.error("Authentication failed: %s", str(e))
        raise