from loguru import logger

# Configure logging
logger.add("logs/app.log", rotation="1 MB", retention="7 days", level="DEBUG")

def log_info(message: str):
    logger.info(message)

def log_error(message: str):
    logger.error(message)
