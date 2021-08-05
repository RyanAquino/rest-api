"""
Test principles API endpoints
"""
import ast
from api.tests.factories.principle_factory import PrincipleFactory
from api.models.Principle import Principle
from api import app, db


class TestPrinciple:
    url = "/principles"

    @classmethod
    def setup_method(cls):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
        db.create_all()

    @classmethod
    def teardown_method(cls):
        db.drop_all()

    def test_view_all_principles(self, client):
        """
        test viewing all principles
        """
        principles = PrincipleFactory.create_batch(5)
        db.session.add_all(principles)
        db.session.commit()

        response = client.get(self.url)
        assert response.status_code == 200
        assert response.headers["Content-type"] == "application/json"
        assert db.session.query(Principle).count() == 5

    def test_add_new_principle(self, client):
        """
        Test when adding a new principle
        """
        expected = {"name": "This is a new principle"}

        response = client.post(self.url, json=expected)
        assert response.status_code == 201

        response = ast.literal_eval(response.data.decode())
        assert response["name"] == expected["name"]
        assert Principle.query.count() == 1

    def test_change_principle(self, client):
        """
        Test when editing a principle
        """
        principle = PrincipleFactory()
        db.session.add(principle)
        db.session.commit()

        url = f"{self.url}/{principle.id}"
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
        principle = PrincipleFactory()
        db.session.add(principle)
        db.session.commit()

        assert Principle.query.count() == 1

        url = f"{self.url}/{principle.id}"

        response = client.delete(url)
        assert response.status_code == 204
        assert Principle.query.count() == 0
