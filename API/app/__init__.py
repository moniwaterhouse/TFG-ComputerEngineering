from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.routes import cell_bp, territory_bp

app.register_blueprint(cell_bp, url_prefix='/cell')
app.register_blueprint(territory_bp, url_prefix='/territory')
