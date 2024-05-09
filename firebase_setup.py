import firebase_admin
from firebase_admin import credentials


def conect_firebase():
    cred = credentials.Certificate("credentials.json")
    firebase_admin.initialize_app(cred)
    print("Firebase Connected")
