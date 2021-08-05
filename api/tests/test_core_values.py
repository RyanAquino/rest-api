"""
Test core value API endpoints
"""
import ast
from api import app, db
from api.tests.factories.core_values_factory import CoreValueFactory
from api.models.CoreValue import CoreValue


class TestCoreValue:
    url = "/values"

    @classmethod
    def setup_method(cls):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        db.create_all()

    @classmethod
    def teardown_method(cls):
        db.drop_all()

    def test_view_all_core_values(self, client):
        """
        test status code of viewing all principles
        """
        core_values = CoreValueFactory.create_batch(5)
        db.session.add_all(core_values)
        db.session.commit()

        response = client.get(self.url)
        assert response.status_code == 200
        assert response.headers["Content-type"] == "application/json"
        assert db.session.query(CoreValue).count() == 5

    def test_add_new_core_value(self, client):
        """
        Test when adding a new core value
        """
        expected = {"name": "This is a new core value"}

        response = client.post(self.url, json=expected)
        assert response.status_code == 201

        response = ast.literal_eval(response.data.decode())
        assert response["name"] == expected["name"]
        assert CoreValue.query.count() == 1

    def test_change_principle(self, client):
        """
        Test when editing a core value
        """
        core_value = CoreValueFactory()
        db.session.add(core_value)
        db.session.commit()

        url = f"{self.url}/{core_value.id}"
        data = {"name": "Updating principle"}

        response = client.put(url, json=data)
        assert response.status_code == 200

        response = response.data.decode()
        response = ast.literal_eval(response)
        assert response["name"] == data["name"]

    def test_delete_principle(self, client):
        """
        Test when deleting a core value
        """
        core_value = CoreValueFactory()
        db.session.add(core_value)
        db.session.commit()

        assert CoreValue.query.count() == 1

        url = f"{self.url}/{core_value.id}"

        response = client.delete(url)
        assert response.status_code == 204
        assert CoreValue.query.count() == 0
