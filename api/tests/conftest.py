"""
Pytest shared fixtures
"""
import pytest
from api import app


db_uri = "sqlite://"


@pytest.fixture(scope='session')
def client():
    client = app.test_client()
    return client
