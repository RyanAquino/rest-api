"""
Core Values API module
"""
from flask_restful import Resource
from flask import request, jsonify
from .models.CoreValue import CoreValue, core_value_schema, core_values_schema
from api.models.CoreValue import db


class CoreValuesResource(Resource):
    """
    Core Values API Resource
    """

    def get(self):
        """
        Get all core values
        :return: list of all core values
        """
        values = CoreValue.query.all()
        results = core_values_schema.dump(values)

        return results

    def post(self):
        """
        Add new core value

        :return: added core value json
        """
        if not request.json['name'] or request.json['name'] == '':
            return 'Error'

        name = request.json['name']
        new_value = CoreValue(name)
        db.session.add(new_value)
        db.session.commit()

        return core_value_schema.jsonify(new_value)


class CoreValueResource(Resource):
    def get(self, value_id):
        """
        Get single Core Value

        :param value_id: core value id
        :return: single core value json
        """
        values = CoreValue.query.get(value_id)

        return core_value_schema.jsonify(values)

    def delete(self, value_id):
        """
        Delete a single core value

        :param value_id: core value id
        :return: deleted core value json
        """
        value = CoreValue.query.get(value_id)
        db.session.delete(value)
        db.session.commit()

        return core_value_schema.jsonify(value)

    def put(self, value_id):
        """
        Update single Core Value

        :param value_id: core value id
        :return: updated core value json
        """
        if not request.json['name'] or request.json['name'] == '':
            return jsonify({'error': 'name is required'})

        core_value = CoreValue.query.get(value_id)
        core_value.name = request.json['name']
        db.session.commit()

        return core_value_schema.jsonify(core_value)
