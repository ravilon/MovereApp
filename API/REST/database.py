import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dotenv import load_dotenv


# Global variable for Firestore client
_db_client = None

def get_db():
    global _db_client
    load_dotenv()

    if _db_client is None:

        json_key_path = json.loads(os.getenv('FIRESTORE'))
        # Initialize Firebase only once
        cred = credentials.Certificate(json_key_path)

        firebase_admin.initialize_app(cred)

        # Create Firestore client
        _db_client = firestore.client()

    return _db_client