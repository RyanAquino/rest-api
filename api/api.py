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

api = Api(app)
db.init_app(app)
ma.init_app(app)

api.add_resource(PrinciplesResource, "/principles")
api.add_resource(PrincipleResource, "/principles/<principle_id>")
api.add_resource(CoreValuesResource, "/values")
api.add_resource(CoreValueResource, "/values/<value_id>")
