"""
Principles API module
"""
from flask_restful import Resource
from flask import request, jsonify
from .models.Principle import Principle, principle_schema, principles_schema
from api.models.Principle import db


class PrinciplesResource(Resource):
    """
    Principles API Resource
    """

    def get(self):
        """
        Get all principles
        :return: list of all principles
        """
        principles = Principle.query.all()
        results = principles_schema.dump(principles)

        return results

    def post(self):
        """
        Add a new principle
        :return: added principle json
        """
        if not request.json['name']:
            return {'error' : 'name is required'}

        name = request.json['name']
        new_principle = Principle(name)
        db.session.add(new_principle)
        db.session.commit()

        return principle_schema.jsonify(new_principle)


class PrincipleResource(Resource):

    def get(self, principle_id):
        """
        Get single principle

        :param principle_id: principle id
        :return: single principle json
        """
        principle = Principle.query.get(principle_id)

        return principle_schema.jsonify(principle)

    def delete(self, principle_id):
        """
        Delete a single Principle

        :param principle_id: core value id
        :return: deleted principle json
        """
        principle = Principle.query.get(principle_id)
        db.session.delete(principle)
        db.session.commit()

        return principle_schema.jsonify(principle)

    def put(self, principle_id):
        """
        Update single Principle Value

        :param principle_id: core value id
        :return: updated principle json
        """
        if not request.json['name'] or request.json['name'] == '':
            return jsonify({'error': 'name is required'})

        principle = Principle.query.get(principle_id)
        principle.name = request.json['name']
        db.session.commit()

        return principle_schema.jsonify(principle)
