import connexion
from config import config
from flask_sqlalchemy import SQLAlchemy


app_port = config.getint('APP', 'PORT')
app_debug = config.getboolean('APP', 'DEBUG')

app = connexion.App(__name__, specification_dir='swagger/')
app.app.config['SQLALCHEMY_DATABASE_URI'] = config['RELATIONAL']['URL']
app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app.app)

app.add_api('api-definition.yml')

if __name__ == '__main__':
    app.run(port=app_port, debug=app_debug)
