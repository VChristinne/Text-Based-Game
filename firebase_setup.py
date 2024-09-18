import json
import os
import firebase_admin
from firebase_admin import credentials
from dotenv import load_dotenv


load_dotenv()
firebase_credentials_path = os.getenv("FIREBASE_CREDENTIALS_PATH")

def conect_firebase():
    with open(firebase_credentials_path, "r") as f:
        firebase_credentials_dict = json.load(f)

    cred = credentials.Certificate(firebase_credentials_dict)
    firebase_admin.initialize_app(cred)
    print("Firebase Connected")
