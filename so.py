import requests
from bs4 import BeautifulSoup

URL = 'https://stackoverflow.com/jobs?q=python'

def extract_max_page():
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, 'html.parser')
    pages = soup.find('div', {'class': 's-pagination'}).find_all('a')
    print(pages)

def get_jobs():
    max_page = extract_max_page()
#    jobs = extract_jobs(max_page)
    return []