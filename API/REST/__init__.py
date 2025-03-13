from flask import Flask
from flasgger import Swagger
from REST import database
from REST.database import get_db
from REST.routes import blueprint as api_bp

# Import the blueprint from routes.py

def create_app():
    app = Flask(__name__)

    # Register the Blueprint
    app.register_blueprint(api_bp)

    # Initialize Swagger
    Swagger(app)
    
    return app
