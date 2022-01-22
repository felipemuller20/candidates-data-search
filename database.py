from decouple import config


USER = config("DB_USER")
HOST = config("DB_HOST")
PASSWORD = config("DB_PASSWORD")