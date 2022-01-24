import database
import scraper
from decouple import config


BASE_URL = config("BASE_URL")

def store_candidates(candidates_urls):
    for candidate in candidates_urls:
            candidate_content = scraper.fetch(BASE_URL + candidate)
            candidate_info = scraper.scrape_candidate_infos(candidate_content)
            if candidate_info.cpf:
                database.add_student(candidate_info)


def get_current_page(next_page):
    return int(next_page.split('/approvals/')[1]) - 1

def get_candidates():
    database.create_database()
    database.create_table()

    content = scraper.fetch(BASE_URL) 
    candidates_urls = scraper.scrape_candidates(content) # ['/candidate/178.422.117-11', '/candidate/012.346.857-44']
    next_page = scraper.scrape_next_page_link(content) # "/approvals/2"
    current_page = get_current_page(next_page)
    while(next_page and candidates_urls):
        print("Buscando candidatos página " + str(current_page))
        store_candidates(candidates_urls)

        next_page_content = scraper.fetch(BASE_URL + next_page)
        candidates_urls = scraper.scrape_candidates(next_page_content)
        next_page = scraper.scrape_next_page_link(next_page_content)
        current_page = get_current_page(next_page)

get_candidates()