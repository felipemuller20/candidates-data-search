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


def scrape_candidates(html_content):
    selector = Selector(html_content)
    candidates_list = []
    for candidate in selector.css("li a::attr(href)").getall():
        candidates_list.append(candidate)
    
    return candidates_list


fetched = fetch("https://sample-university-site.herokuapp.com/approvals/1")
candidates = scrape_candidates(fetched)

print(candidates)