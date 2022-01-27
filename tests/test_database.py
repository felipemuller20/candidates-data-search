from candidates_data_search.database import (
    create_database,
    create_table,
    add_candidate,
    get_candidate,
)
from candidates_data_search.Candidate import Candidate


def test_add_candidate():
    create_database()
    create_table()

    candidate = Candidate('TEST NAME 12399', '99999999999', '99.99')
    add_candidate(candidate)
    candidate_exists = get_candidate("99999999999")
    assert candidate_exists is not None