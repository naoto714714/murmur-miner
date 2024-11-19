import logging
import time
from functools import wraps

logger = logging.getLogger(__name__)


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        logger.info(f"{func.__name__}: {elapsed_time:.2f}秒")
        return result

    return wrapper
