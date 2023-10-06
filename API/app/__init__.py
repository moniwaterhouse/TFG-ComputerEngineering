from flask import Flask
from neo4j import GraphDatabase
from app.config import Config

driver = GraphDatabase.driver(Config.URI, auth=(Config.USERNAME, Config.PASSWORD))
app = Flask(__name__)
territory_file_path = Config.TERRITORY_FILE_PATH

from app.routes.territory_routes import territory_bp

#app.register_blueprint(dpw_bp, url_prefix='/dpw')
app.register_blueprint(territory_bp, url_prefix='/territory')



