"""
Author: Ryan
Description: REST API that exposes 4 values and 12 principles of Agile Software Development
"""

from api import app, db
from flask_migrate import Migrate

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
