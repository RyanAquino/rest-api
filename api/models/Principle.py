"""
Principles Model
"""
from api import db, ma


class Principle(db.Model):
    """
    Principle DB Model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name, id):
        self.name = name
        self.id = id

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
        id = kwargs["id"] if kwargs["id"] else None
        new_value = cls(name, id)
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
        value = principle_schema.jsonify(value)
        cls.query.filter_by(id=kwargs["id"]).delete()
        db.session.commit()
        return value


class PrincipleSchema(ma.Schema):
    """
    Principle Schema
    """

    class Meta:
        fields = ("id", "name")


principle_schema = PrincipleSchema()
principles_schema = PrincipleSchema(many=True)
