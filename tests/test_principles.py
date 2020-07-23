"""
Test core value API endpoints
"""
import os
import sys
import ast
import pytest

sys.path.insert(0, os.path.join("..", ""))
from app import app


@pytest.fixture
def url():
    return "/principles"


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
        data = {"id": request.node.id, "name": "reverted"}
        client.post(url, json=data)

    request.addfinalizer(cleanup)


# Begin test
def test_view_all_principles_status_code(url):
    """
    test status code of viewing all principles
    """
    client = app.test_client()
    response = client.get(url)

    assert response.status_code == 200


def test_view_all_principles_content_type(url):
    """
    test content type of viewing all principles
    """
    client = app.test_client()
    response = client.get(url)

    assert response.headers["Content-type"] == "application/json"


def test_add_new_principle_status_code(url):
    """
    Test when adding a new principle
    """
    client = app.test_client()
    expected = {"name": "This is a new Principle!"}

    response = client.post(url, json=expected)
    assert response.status_code == 201


def test_add_new_principle(url, delete_after_post, request):
    """
    Test when adding a new principles
    """
    client = app.test_client()
    expected = {"name": "This is a new principle"}

    response = client.post(url, json=expected)
    assert response.status_code == 201

    response = ast.literal_eval(response.data.decode())
    assert response["name"] == expected["name"]
    request.node.id = response["id"]


def test_change_principle(url):
    """
    Test when editing a principle
    """
    client = app.test_client()
    id = 1
    url = f"{url}/{id}"
    data = {"name": "Updating principle"}

    response = client.put(url, json=data)
    assert response.status_code == 200
    response = response.data.decode()
    response = ast.literal_eval(response)
    assert response["name"] == data["name"]


def test_delete_principle(url, create_after_deleted, request):
    """
    Test when deleting a core value
    """
    client = app.test_client()
    id = 1
    url = f"{url}/{id}"
    response = client.delete(url)
    assert response.status_code == 204
    request.node.id = id
