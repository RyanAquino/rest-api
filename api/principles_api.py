"""
Principles API module
"""
from flask_restful import Resource
from flask import request
from .models.Principle import Principle


class PrinciplesResource(Resource):
    """
    Principles API Resource
    """

    def get(self):
        """
        Get all principles
        :return: list of all principles
        """
        return Principle.view()

    def post(self):
        """
        Add a new principle
        :return: added principle json
        """
        if not request.data or not request.json["name"]:
            return {"error": "name is required"}, 400

        return Principle.add(name=request.json["name"])


class PrincipleResource(Resource):
    def get(self, principle_id):
        """
        Get single principle

        :param principle_id: principle id
        :return: single principle json
        """
        if not principle_id:
            return {"error": "id is required"}
        return Principle.get_single(principle_id)

    def delete(self, principle_id):
        """
        Delete a single Principle

        :param principle_id: core value id
        :return: deleted principle json
        """
        return Principle.delete(id=principle_id)

    def put(self, principle_id):
        """
        Update single Principle Value

        :param principle_id: core value id
        :return: updated principle json
        """
        if not request.data or not request.json["name"]:
            return {"error": "name is required"},400

        return Principle.change(id=principle_id, name=request.json["name"])
