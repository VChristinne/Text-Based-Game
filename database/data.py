import os
from mysql.connector import connect
from dotenv import load_dotenv


load_dotenv()

db = connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)


def fetch_all(query, params=None):
    cursor = db.cursor(dictionary=True)
    cursor.execute(query, params)
    results = cursor.fetchall()
    cursor.close()
    return results

def fetch_one(query, params=None):
    cursor = db.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchone()
    cursor.close()
    return result

def get_all_roles():
    return fetch_all("SELECT * FROM roles")

def get_role_by_name(role_name):
    return fetch_one("SELECT * FROM roles WHERE name = %s", (role_name,))

def get_all_elements():
    return fetch_all("SELECT * FROM elements")

def get_element_by_name(element_name):
    return fetch_one("SELECT * FROM elements WHERE name = %s", (element_name,))

def get_element_name_by_id(element_id):
    query = "SELECT name FROM elements WHERE id = %s"
    result = fetch_one(query, (element_id,))
    return result['name'] if result else None

def get_all_skills(role_id):
    return fetch_all("SELECT * FROM skills WHERE role_id = %s", (role_id,))

def get_skill_by_name(skill_name):
    return fetch_one("SELECT * FROM skills WHERE name = %s", (skill_name,))
