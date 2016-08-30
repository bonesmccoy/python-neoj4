import connexion
from config import config


app_port = config.getint('APP', 'PORT')
app_debug = config.getboolean('APP', 'DEBUG')

app = connexion.App(__name__, specification_dir='swagger/')
app.add_api('api-definition.yml')
app.run(port=app_port, debug=app_debug)
