import database
from get_candidates import get_candidates

database.create_database()
database.create_table()
get_candidates()