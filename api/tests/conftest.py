"""
Pytest shared fixtures
"""
import pytest
from api import app


@pytest.fixture
def delete_after_post(request, url):
    def cleanup():
        client = app.test_client()
        urlf = f"{url}/{request.node.id}"
        client.delete(urlf)

    request.addfinalizer(cleanup)


@pytest.fixture
def create_after_deleted(request, url):
    def cleanup():
        client = app.test_client()
        data = {"id": request.node.id, "name": "this is new model 5!"}
        client.post(url, json=data)

    request.addfinalizer(cleanup)
