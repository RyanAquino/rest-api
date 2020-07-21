from flask_restful import Resource
from flask import request
from .models.CoreValue import CoreValue, core_value_schema
from .db import db


class CoreValueResource(Resource):

    def get(self):
        pass

    def post(self):
        if not request.json['name']:
            return 'Error'

        name = request.json['name']
        new_value = CoreValue(name)
        db.session.add(new_value)
        db.session.commit()

        return core_value_schema.jsonify(new_value)

    def put(self):
        pass

    def delete(self):
        pass
