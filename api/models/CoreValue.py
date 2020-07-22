"""
Core Value Model
"""
from api import db, ma


class CoreValue(db.Model):
    """
    CoreValue DB model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(65))

    def __init__(self, name, id):
        self.id = id
        self.name = name

    @classmethod
    def get_single(cls, id):
        values = cls.query.get(id)

        return core_value_schema.jsonify(values)

    @classmethod
    def view(cls):
        values = cls.query.all()
        results = core_values_schema.dump(values)

        return core_values_schema.jsonify(results)

    @classmethod
    def add(cls, **kwargs):
        name = kwargs["name"]
        id = kwargs["id"] if kwargs["id"] else None
        new_value = cls(name, id)
        db.session.add(new_value)
        db.session.commit()

        return core_value_schema.jsonify(new_value)

    @classmethod
    def change(cls, **kwargs):
        core_value = cls.query.get(kwargs["id"])
        core_value.name = kwargs["name"]
        db.session.commit()

        print(core_value)
        return core_value_schema.jsonify(core_value)

    @classmethod
    def delete(cls, **kwargs):
        value = cls.query.get(kwargs["id"])
        db.session.delete(value)
        db.session.commit()

        return core_value_schema.jsonify(value)


class CoreValueSchema(ma.Schema):
    """
    CoreValue Schema
    """

    class Meta:
        fields = ("id", "name")


core_value_schema = CoreValueSchema()
core_values_schema = CoreValueSchema(many=True)
