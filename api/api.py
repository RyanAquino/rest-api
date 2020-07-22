"""
Main API
"""
from flask import Flask
from flask_restful import Api
from .db import db, ma
from .config import USERNAME, PASSWORD, DB, HOST
from .principles_api import PrincipleResource, PrinciplesResource
from .core_values_api import CoreValueResource, CoreValuesResource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{USERNAME}:{PASSWORD}@{HOST}/{DB}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

errors = {
    "UserAlreadyExistsError": {
        "message": "A user with that username already exists.",
        "status": 409,
    },
    "ResourceDoesNotExist": {
        "message": "A resource with that ID no longer exists.",
        "status": 410,
        "extra": "Any extra information you want.",
    },
}

api = Api(app, errors=errors)
db.init_app(app)
ma.init_app(app)

api.add_resource(PrinciplesResource, "/principles")
api.add_resource(PrincipleResource, "/principles/<principle_id>")
api.add_resource(CoreValuesResource, "/values")
api.add_resource(CoreValueResource, "/values/<value_id>")
