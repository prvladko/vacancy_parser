import requests
from bs4 import BeautifulSoup

URL = 'https://stackoverflow.com/jobs?q=python'

def extract_max_page():
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, 'html.parser')
    pages = soup.find('div', {'class': 's-pagination'}).find_all('a')
    last_page = int(pages[-2].get_text(strip=True))
    return last_page

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f'{URL}&pg={page+1}')
        soup = BeautifulSoup(result.text, 'html.parser')

def get_jobs():
    max_page = extract_max_page()
    jobs = extract_jobs(max_page)
    return []