"""
Initialize App, DB and serializer, Swagger UI
"""
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask import Flask
from .config import USERNAME, PASSWORD, DB, HOST, PORT
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Simple REST API'
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

from api import routes
