import database
import scraper
from decouple import config


BASE_URL = config("BASE_URL")


def store_candidates(candidates_urls):
    for candidate in candidates_urls:
            candidate_content = scraper.fetch(BASE_URL + candidate)
            candidate_info = scraper.scrape_candidate_infos(candidate_content)
            if candidate_info.cpf:
                already_registered = database.get_candidate(candidate_info.cpf)
                if not already_registered:
                    print(f"CPF {candidate_info.cpf} registrado com sucesso")
                    database.add_candidate(candidate_info)
                else:
                    print(f"CPF {candidate_info.cpf} já registrado anteriormente.")


def get_current_page(next_page):
    if next_page:
        return int(next_page.split('/approvals/')[1]) - 1


def get_candidates():
    content = scraper.fetch(BASE_URL)
    candidates_urls = scraper.scrape_candidates(content)
    next_page = scraper.scrape_next_page_link(content)
    current_page = get_current_page(next_page)
    while(next_page and candidates_urls):
        print(f"Buscando candidatos - Página {str(current_page)}")
        store_candidates(candidates_urls)

        next_page_content = scraper.fetch(BASE_URL + next_page)
        candidates_urls = scraper.scrape_candidates(next_page_content)
        next_page = scraper.scrape_next_page_link(next_page_content)
        current_page = get_current_page(next_page)
    print("Todos os dados foram coletados.")
