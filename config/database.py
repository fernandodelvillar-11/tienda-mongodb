import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Carga las variables del archivo .env
load_dotenv()

def get_database():
    uri     = os.getenv("MONGO_URI")
    db_name = os.getenv("DB_NAME")

    if not uri or not db_name:
        raise Exception("❌ No se encontraron las variables MONGO_URI o DB_NAME en el archivo .env")

    client = MongoClient(uri)
    return client[db_name]