from flask_restful import Resource
from flask import request
from .models.Principle import Principle, principle_schema
from .db import db


class PrincipleResource(Resource):

    def get(self):
        pass

    def post(self):
        if not request.json['name']:
            return 'Error'

        name = request.json['name']
        new_principle = Principle(name)
        db.session.add(new_principle)
        db.session.commit()

        return principle_schema.jsonify(new_principle)

    def put(self):
        pass

    def delete(self):
        pass
