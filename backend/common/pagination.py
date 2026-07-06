"""
Standard pagination classes for TaskFlow API.
"""

from rest_framework.pagination import PageNumberPagination


class StandardPagination(PageNumberPagination):
    """Default pagination: 20 items per page, max 100."""
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class SmallPagination(PageNumberPagination):
    """Smaller pagination for lightweight lists (e.g., notifications)."""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class LargePagination(PageNumberPagination):
    """Larger pagination for admin/export views."""
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 200
