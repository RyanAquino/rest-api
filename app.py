"""
Author: Ryan
Description: REST API that exposes 4 values and 12 principles of Agile Software Development
"""

from api.api import app
from api.db import db
from api.models import CoreValue

@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = CoreValue.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return '',204


if __name__ == '__main__':
    app.run(debug=True)
