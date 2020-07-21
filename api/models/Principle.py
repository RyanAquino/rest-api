"""
Principles Model
"""
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

ma = Marshmallow()
db = SQLAlchemy()


class Principle(db.Model):
    """
    Principle DB Model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(65))

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_single(cls, principle_id):
        values = cls.query.get(principle_id)

        return principle_schema.jsonify(values)

    @classmethod
    def view(cls):
        values = cls.query.all()
        results = principles_schema.dump(values)

        return results

    @classmethod
    def add(cls, **kwargs):
        name = kwargs["name"]
        new_value = cls(name)
        db.session.add(new_value)
        db.session.commit()

        return principle_schema.jsonify(new_value)

    @classmethod
    def change(cls, **kwargs):
        core_value = cls.query.get(kwargs["id"])
        core_value.name = kwargs["name"]
        db.session.commit()

        return principle_schema.jsonify(core_value)

    @classmethod
    def delete(cls, **kwargs):
        value = cls.query.get(kwargs["id"])
        db.session.delete(value)
        db.session.commit()

        return principle_schema.jsonify(value)


class PrincipleSchema(ma.Schema):
    """
    Principle Schema
    """

    class Meta:
        fields = ("id", "name")


principle_schema = PrincipleSchema()
principles_schema = PrincipleSchema(many=True)
