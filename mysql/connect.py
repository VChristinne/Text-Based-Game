import os

from mysql.connector import connect
from dotenv import load_dotenv


load_dotenv()

def connect_mysql():
    return connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )
