"""
Test principles API endpoints
"""
import ast
import pytest


@pytest.fixture
def url():
    return "/principles"


def test_view_all_principles_status_code(url, client):
    """
    test status code of viewing all principles
    """
    response = client.get(url)

    assert response.status_code == 200


def test_view_all_principles_content_type(url, client):
    """
    test content type of viewing all principles
    """
    response = client.get(url)

    assert response.headers["Content-type"] == "application/json"


def test_add_new_principle(url, delete_after_post, client, request):
    """
    Test when adding a new principles
    """
    expected = {"name": "This is a new principle"}

    response = client.post(url, json=expected)
    assert response.status_code == 201

    response = ast.literal_eval(response.data.decode())
    assert response["name"] == expected["name"]
    request.node.id = response["id"]


def test_change_principle(url, client):
    """
    Test when editing a principle
    """
    id = 1
    url = f"{url}/{id}"
    data = {"name": "Updating principle"}

    response = client.put(url, json=data)
    assert response.status_code == 200

    response = response.data.decode()
    response = ast.literal_eval(response)
    assert response["name"] == data["name"]


def test_delete_principle(url, create_after_deleted, client, request):
    """
    Test when deleting a core value
    """
    principle_id = 1
    url = f"{url}/{principle_id}"

    response = client.delete(url)
    assert response.status_code == 204
    request.node.id = principle_id
