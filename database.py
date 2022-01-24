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
    create_database = "CREATE DATABASE IF NOT EXISTS " + DB_NAME
    mydb.cursor().execute(create_database)
    mydb.commit()


def create_table():
    mydb.cursor().execute("USE " + DB_NAME)
    create_table = '''CREATE TABLE IF NOT EXISTS `candidates` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `name` varchar(255) NOT NULL,
        `cpf` varchar(11) NOT NULL,
        `score` float NOT NULL,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''
    mydb.cursor().execute(create_table)
    mydb.commit()


def add_student(student):
    name = student["name"]
    cpf = student["cpf"]
    score = student["score"]
    mydb.cursor().execute('INSERT INTO candidates (name, cpf, score) VALUES (%s, %s, %s)', (name, cpf, score))
    mydb.commit()
