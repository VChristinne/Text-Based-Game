from firebase_admin import firestore
from firebase_setup import conect_firebase

conect_firebase()
db = firestore.client()

def get_all_data(collection):
    docs = db.collection(collection).stream()
    data = {}
    for doc in docs:
        data[doc.id] = doc.to_dict()
    return data

skills = None
elements = None
roles = None

def load_game_data():
    global skills, elements, roles
    elements = get_all_data('elements')
    roles = get_all_data('roles')

if __name__ == "__main__":
    load_game_data()
    print("Elements:")

    for key, value in elements.items():
        print(f"{key}: {value}")
    print("\nRoles:")

    for key, value in roles.items():
        print(f"{key}: {value}")
