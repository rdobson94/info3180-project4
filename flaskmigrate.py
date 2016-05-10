from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import app
from app import db

migrate = Migrate(app, db)
management = Manager(app)
management.add_command('db', MigrateCommand)

if __name__ == '__main__':
    management.run()