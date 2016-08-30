import configparser
import os

config_env = os.getenv('DATAPOINT_CONFIG', 'config.ini')
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), config_env))