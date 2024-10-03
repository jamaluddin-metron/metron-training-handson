from flask import Flask
from .routes import register_routes
import os

def create_app() -> Flask:
    app_name = os.getenv('APP_NAME', 'Metron Training Server')
    app = Flask(app_name)
    
    register_routes(app)
    
    return app

