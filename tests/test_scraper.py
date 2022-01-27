from candidates_data_search.scraper import (
    fetch,
    scrape_candidates,
    scrape_next_page_link,
    scrape_candidate_infos,
)
import requests


first_three_candidates_mock = ['/candidate/178.422.117-11', '/candidate/012.346.857-44', '/candidate/012.347.586-44']


def test_fetch():
    url = 'https://sample-university-site.herokuapp.com/approvals/1'
    response = requests.get(url)

    result = fetch(url)
    assert result["url"] == response.url
    assert result["content"] == response.text


def test_scrape_candidate():
    url = 'https://sample-university-site.herokuapp.com/approvals/1'
    response = fetch(url)

    assert scrape_candidates(response)[:3] == first_three_candidates_mock
    assert scrape_candidates(False) == None


def test_scrape_next_page():
    url = 'https://sample-university-site.herokuapp.com/approvals/1'
    response = fetch(url)

    assert scrape_next_page_link(response) == '/approvals/2'


def test_scrape_candidate_infos():
    url = 'https://sample-university-site.herokuapp.com/candidate/178.422.117-11'
    response = fetch(url)

    assert scrape_candidate_infos(response).name == 'JOHN SMITH'
    assert scrape_candidate_infos(response).cpf == '17842211711'
    assert scrape_candidate_infos(response).score == '99.77'
