import mysql.connector
from decouple import config


DB_USER = config("DB_USER")
DB_HOST = config("DB_HOST")
DB_PASSWORD = config("DB_PASSWORD")
PORT = config("PORT")
DB_NAME = config("DB_NAME")


mydb = mysql.connector.connect(
  host=DB_HOST,
  user=DB_USER,
  password=DB_PASSWORD,
  port=PORT
)


def create_database():
    create_database = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"
    mydb.cursor().execute(create_database)
    mydb.commit()


def create_table():
    mydb.cursor().execute(f"USE {DB_NAME}")
    create_table = '''CREATE TABLE IF NOT EXISTS `candidates` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `name` varchar(255) NOT NULL,
        `cpf` varchar(11) NOT NULL,
        `score` float NOT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''
    mydb.cursor().execute(create_table)
    mydb.commit()


def add_candidate(candidate):
    mydb.cursor().execute(f"USE {DB_NAME}")
    name = candidate.name
    cpf = candidate.cpf
    score = candidate.score
    mydb.cursor().execute("""INSERT INTO candidates (name, cpf, score)
    VALUES (%s, %s, %s)""", (name, cpf, score))
    mydb.commit()


def get_candidate(cpf):
    cursor = mydb.cursor(buffered=True)
    cursor.execute(f"USE {DB_NAME}")
    cursor.execute(f"SELECT cpf FROM candidates WHERE cpf = {cpf}")
    return cursor.fetchone()


def remove_candidate(cpf):
    cursor = mydb.cursor(buffered=True)
    cursor.execute(f"USE {DB_NAME}")
    cursor.execute(f"DELETE FROM candidates WHERE cpf = {cpf}")
    mydb.commit()
