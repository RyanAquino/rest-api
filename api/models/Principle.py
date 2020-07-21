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


class PrincipleSchema(ma.Schema):
    """
    Principle Schema
    """
    class Meta:
        fields = ('id', 'name')


principle_schema = PrincipleSchema()
principles_schema = PrincipleSchema(many=True)
