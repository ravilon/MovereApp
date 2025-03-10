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
    
    """
    # Test DB
    # db = get_db()
    # collection_ref = db.collection("users")
    # docs = collection_ref.stream()
    for doc in docs:
        print(f"Document ID: {doc.id}")
        print(f"Data: {doc.to_dict()}")
    """ 
    
    return app
