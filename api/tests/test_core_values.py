"""
Test core value API endpoints
"""
import ast
import pytest


@pytest.fixture
def url():
    return "/values"


def test_view_all_core_values_status_code(url, client):
    """
    Test status code of viewing all core values
    """
    response = client.get(url)
    assert response.status_code == 200


def test_view_all_core_values_content_type(url, client):
    """
    Test content type of viewing all core values
    """
    response = client.get(url)
    assert response.headers["Content-type"] == "application/json"


def test_add_new_core_value(url, delete_after_post, client, request):
    """
    Test when adding a new core value
    """
    expected = {"name": "Individuals and Interactions Over Processes and Tools edited"}

    response = client.post(url, json=expected)
    assert response.status_code == 201

    response = ast.literal_eval(response.data.decode())
    assert response["name"] == expected["name"]
    request.node.id = response["id"]


def test_change_core_value(url, client):
    """
    Test when editing a core value
    """
    id = 1
    url = f"{url}/{id}"
    data = {"name": "updated"}

    response = client.put(url, json=data)
    assert response.status_code == 200
    response = response.data.decode()
    response = ast.literal_eval(response)
    assert response["name"] == data["name"]


def test_delete_core_value(url, create_after_deleted, client, request):
    """
    Test when deleting a core value
    """
    id = 1
    url = f"{url}/{id}"
    response = client.delete(url)
    print(response)
    assert response.status_code == 204
    request.node.id = id
