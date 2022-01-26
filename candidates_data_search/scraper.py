import requests
import candidates_data_search.utils.get_infos as get_infos
from candidates_data_search.Candidate import Candidate
from parsel import Selector


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
    except requests.Timeout:
        return None
    if response.status_code != 200:
        return None

    return {
        "content": response.text,
        "url": response.url
    }


def scrape_candidates(html_content):
    if html_content:
        selector = Selector(html_content["content"])
        candidates_list = []
        for candidate in selector.css("li a::attr(href)").getall():
            candidates_list.append(candidate)

        return candidates_list
    return None


def scrape_next_page_link(html_content):
    if html_content:
        selector = Selector(html_content["content"])
        next_page = selector.css("div a::attr(href)").get()

        if next_page:
            return next_page
        return None


def scrape_candidate_infos(html_content):
    selector = Selector(html_content["content"])
    infos = get_infos.get_name_and_score(selector)
    name = infos["name"]
    score = infos["score"]
    cpf = get_infos.get_candidate_cpf(html_content["url"])
    candidate = Candidate(name, cpf, score)
    return candidate
