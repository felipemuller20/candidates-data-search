import database
import scraper
from decouple import config


BASE_URL = config("BASE_URL")


def get_candidates():
    database.create_database()
    database.create_table()
    content = scraper.fetch(BASE_URL) 
    candidates_urls = scraper.scrape_candidates(content) # ['/candidate/178.422.117-11', '/candidate/012.346.857-44']
    next_page = scraper.scrape_next_page_link(content) # "/approvals/2"
    # while(next_page and candidate_urls):
    while(next_page and candidates_urls):
        print(next_page)
        for candidate in candidates_urls:
            candidate_content = scraper.fetch(BASE_URL + candidate)
            candidate_info = scraper.scrape_candidate_infos(candidate_content)
            database.add_student(candidate_info)

        next_page_content = scraper.fetch(BASE_URL + next_page)
        candidates_urls = scraper.scrape_candidates(next_page_content)
        next_page = scraper.scrape_next_page_link(next_page_content)

get_candidates()