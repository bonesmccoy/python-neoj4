from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import app, db

application = app.app

migrate = Migrate(application, db)
manager = Manager(application)
manager.add_command('db', MigrateCommand)

from model import *

if __name__ == '__main__':
    manager.run()

