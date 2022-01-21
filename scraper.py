import requests


def fetch(url):
    try:
        response = requests.get(url, timeout=5)
    except requests.Timeout:
        return None
    if response.status_code != 200:
        return None
    
    return response.text