"""
Shared pytest fixtures for TaskFlow test suite.
"""

import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    """Unauthenticated API client."""
    return APIClient()


@pytest.fixture
def auth_client(api_client, user):
    """Authenticated API client using the 'user' fixture."""
    api_client.force_authenticate(user=user)
    return api_client
