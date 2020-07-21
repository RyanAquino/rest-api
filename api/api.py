from flask import Flask
from flask_restful import Api
from .db import db, ma
from .principles_api import PrincipleResource
from .core_values_api import CoreValueResource


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/rest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db.init_app(app)
ma.init_app(app)

api.add_resource(PrincipleResource, '/principles')
api.add_resource(CoreValueResource, '/values')
