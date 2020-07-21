"""
Core Values API module
"""
from flask_restful import Resource
from flask import request, jsonify
from .models.CoreValue import CoreValue


class CoreValuesResource(Resource):
    """
    Core Values API Resource
    """

    def get(self):
        """
        Get all core values
        :return: list of all core values
        """
        return CoreValue.view()

    def post(self):
        """
        Add new core value

        :return: added core value json
        """
        if not request.json["name"]:
            return {"error": "name is required"}

        return CoreValue.add(name=request.json["name"])


class CoreValueResource(Resource):
    def get(self, value_id):
        """
        Get single Core Value

        :param value_id: core value id
        :return: single core value json
        """
        if not value_id:
            return {"error": "id is required"}

        return CoreValue.get_single(value_id)

    def delete(self, value_id):
        """
        Delete a single core value

        :param value_id: core value id
        :return: deleted core value json
        """
        if not value_id:
            return {"error": "id is required"}

        return CoreValue.delete(id=value_id)

    def put(self, value_id):
        """
        Update single Core Value

        :param value_id: core value id
        :return: updated core value json
        """
        if not request.json["name"]:
            return jsonify({"error": "name is required"})

        return CoreValue.change(id=value_id, name=request.json["name"])
