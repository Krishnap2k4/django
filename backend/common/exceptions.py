"""
Custom exception handler for TaskFlow API.
Provides consistent error response format across all endpoints.
"""

import logging

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger('apps')


def custom_exception_handler(exc, context):
    """
    Custom exception handler that returns consistent JSON error responses.

    Response format:
    {
        "success": false,
        "error": {
            "code": "error_code",
            "message": "Human-readable message",
            "details": {}  // optional field-level errors
        }
    }
    """
    response = exception_handler(exc, context)

    if response is not None:
        error_data = {
            'success': False,
            'error': {
                'code': _get_error_code(response.status_code),
                'message': _get_error_message(response),
                'details': response.data if isinstance(response.data, dict) else {'detail': response.data},
            }
        }
        response.data = error_data
    else:
        # Unhandled exception — log it and return 500
        logger.exception(
            f"Unhandled exception in {context.get('view', 'unknown')}: {exc}"
        )
        error_data = {
            'success': False,
            'error': {
                'code': 'internal_server_error',
                'message': 'An unexpected error occurred. Please try again later.',
                'details': {},
            }
        }
        response = Response(error_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response


def _get_error_code(status_code):
    """Map HTTP status codes to error code strings."""
    code_map = {
        400: 'bad_request',
        401: 'unauthorized',
        403: 'forbidden',
        404: 'not_found',
        405: 'method_not_allowed',
        409: 'conflict',
        429: 'throttled',
        500: 'internal_server_error',
    }
    return code_map.get(status_code, 'error')


def _get_error_message(response):
    """Extract a human-readable message from the response data."""
    if isinstance(response.data, dict):
        if 'detail' in response.data:
            return str(response.data['detail'])
        # Return first field error
        for field, errors in response.data.items():
            if isinstance(errors, list) and errors:
                return f"{field}: {errors[0]}"
            elif isinstance(errors, str):
                return f"{field}: {errors}"
    elif isinstance(response.data, list) and response.data:
        return str(response.data[0])
    return 'An error occurred.'


class TaskFlowException(Exception):
    """Base exception for TaskFlow business logic errors."""
    def __init__(self, message, code='error', status_code=400):
        self.message = message
        self.code = code
        self.status_code = status_code
        super().__init__(message)


class InvalidStatusTransition(TaskFlowException):
    """Raised when a task status transition is not allowed."""
    def __init__(self, from_status, to_status):
        super().__init__(
            message=f"Cannot transition from '{from_status}' to '{to_status}'.",
            code='invalid_status_transition',
            status_code=400,
        )


class PermissionDeniedError(TaskFlowException):
    """Raised when a user doesn't have permission for an action."""
    def __init__(self, message='You do not have permission to perform this action.'):
        super().__init__(
            message=message,
            code='permission_denied',
            status_code=403,
        )
