from rest_framework.views import exception_handler
import logging

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # Log unhandled exceptions
    if response is None or response.status_code >= 500:
        logger.error(f"Unhandled exception: {exc}", exc_info=True)

    return response
