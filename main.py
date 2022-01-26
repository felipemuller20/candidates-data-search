import candidates_data_search.database as database
from candidates_data_search.get_candidates import get_candidates

database.create_database()
database.create_table()
get_candidates()
