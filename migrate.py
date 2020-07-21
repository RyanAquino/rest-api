"""
DB Migrations
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api.api import app
from api.db import db


manager = Manager(app)
manager.add_command('db', MigrateCommand)
migrate = Migrate(app, db)


class CoreValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(65))

    def __init__(self, name):
        self.name = name


class Principle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(65))

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    manager.run()
