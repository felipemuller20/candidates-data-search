import requests
from parsel import Selector


def fetch(url):
    try:
        response = requests.get(url, timeout=5)
    except requests.Timeout:
        return None
    if response.status_code != 200:
        return None
    
    return response.text


def scrape_candidates(html_content): # Exemplo de retorno: ['/candidate/178.422.117-11', '/candidate/012.346.857-44']
    selector = Selector(html_content)
    candidates_list = []
    for candidate in selector.css("li a::attr(href)").getall():
        candidates_list.append(candidate)
    
    return candidates_list


def scrape_next_page_link(html_content): #  Exemplo de retorno: "/approvals/2"
    selector = Selector(html_content)
    next_page = selector.css("div a::attr(href)").get()

    if next_page:
        return next_page
    return None

