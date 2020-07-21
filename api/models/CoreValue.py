"""
Core Value Model
"""
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

ma = Marshmallow()
db = SQLAlchemy()


class CoreValue(db.Model):
    """
    CoreValue DB model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(65))

    def __init__(self, name):
        self.name = name


class CoreValueSchema(ma.Schema):
    """
    CoreValue Schema
    """

    class Meta:
        fields = ("id", "name")


core_value_schema = CoreValueSchema()
core_values_schema = CoreValueSchema(many=True)
