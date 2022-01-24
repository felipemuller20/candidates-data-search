import requests
import utils.get_infos
import database
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


def scrape_candidates(html_content): # Exemplo de retorno: ['/candidate/178.422.117-11', '/candidate/012.346.857-44']
    selector = Selector(html_content["content"])
    candidates_list = []
    for candidate in selector.css("li a::attr(href)").getall():
        candidates_list.append(candidate)
    
    return candidates_list


def scrape_next_page_link(html_content): #  Exemplo de retorno: "/approvals/2"
    selector = Selector(html_content["content"])
    next_page = selector.css("div a::attr(href)").get()

    if next_page:
        return next_page
    return None


def scrape_candidate_infos(html_content): # content = https://sample-university-site.herokuapp.com/candidate/178.422.117-11
    selector = Selector(html_content["content"])
    infos = utils.get_infos.get_name_and_score(selector)
    return {
        "name": infos["name"],
        "score": infos["score"],
        "cpf": utils.get_infos.get_candidate_cpf(html_content["url"])
    }
