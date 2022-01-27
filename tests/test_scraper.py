from candidates_data_search.scraper import (
    fetch,
    scrape_candidates,
    scrape_next_page_link,
    scrape_candidate_infos,
)
import requests


first_three_candidates_mock = ['/candidate/178.422.117-11', '/candidate/012.346.857-44', '/candidate/012.347.586-44']


def test_fetch():
    url = "https://sample-university-site.herokuapp.com/approvals/1"
    response = requests.get(url)

    result = fetch(url)
    assert result["url"] == response.url
    assert result["content"] == response.text


def test_scrape_candidate():
    url = "https://sample-university-site.herokuapp.com/approvals/1"
    response = requests.get(url)

    result = fetch(url)

    assert scrape_candidates(result)[:3] == first_three_candidates_mock
    assert scrape_candidates(False) == None
