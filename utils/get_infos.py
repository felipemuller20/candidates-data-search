import re
from unidecode import unidecode


def get_name_and_score(selector):
    infos = selector.css("div::text").getall()
    name = infos[0].strip()
    score = infos[1].strip()
    return {
        "name": unidecode(re.sub(r'[^\w\s]','',name)).upper(),
        "score": score
    }


def get_candidate_cpf(url):
    candidate_cpf = url.split('candidate/')[1].replace('.', '').replace('-', '')
    return candidate_cpf
