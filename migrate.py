from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api.api import app, db
import api.models

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
