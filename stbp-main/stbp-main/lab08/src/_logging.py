from loguru import logger

logger.remove()
logger.add('./file.log',
           format='{time:YYYY-MM-DD HH:mm:ss} | {level} - {message} (function = {function})')