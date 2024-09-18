import json
import os
import firebase_admin
from firebase_admin import credentials
from dotenv import load_dotenv


def connect_firebase():
    load_dotenv()
    firebase_credentials_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
    
    with open(firebase_credentials_path, "r") as f:
        firebase_credentials_dict = json.load(f)

    cred = credentials.Certificate(firebase_credentials_dict)
    firebase_admin.initialize_app(cred)
    print("Firebase Connected")
