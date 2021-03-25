import requests
from bs4 import BeautifulSoup

headers = {
        'Host': 'hh.ru',
        'User-Agent': 'Safari',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

def extract_max_page():
    headers = {
        'Host': 'hh.ru',
        'User-Agent': 'Safari',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    hh_request = requests.get('''https://hh.ru/search/vacancy?schedule=remote&items_on_page=100&search_field=name&
    st=searchVacancy&text=%D1\'%80%D0%B5%D0%BA%D1\'%80%D1\'%83%D1\'%82%D0%B5%D1%80+OR+recruiter+OR+
    Recruitment+%28talent+aqusition%29+OR+\'%28%D0%BF%D0%BE%D0%B4%D0%B1%D0%BE%D1\'%80%D1%83+%D0%
    BF%D0%B5%D1\'%80%D1\'%81%D0%BE%D0%BD%D0%B0%D0%BB%D0%B0%29+OR+Researcher''', headers = headers)

    hh_soup = BeautifulSoup(hh_request.text, 'html.parser')

    pages = []

    paginator = hh_soup.find_all('span', {'class': 'pager-item-not-in-short-range'})

    for page in paginator:
        pages.append(int(page.find('a').text))


    return pages[-1] 

def extract_hh_jobs(last_page):
    for page in range(last_page):
        result = requests.get('''https://hh.ru/search/vacancy?schedule=remote&items_on_page=100&search_field=name&
    st=searchVacancy&text=%D1\'%80%D0%B5%D0%BA%D1\'%80%D1\'%83%D1\'%82%D0%B5%D1%80+OR+recruiter+OR+
    Recruitment+%28talent+aqusition%29+OR+\'%28%D0%BF%D0%BE%D0%B4%D0%B1%D0%BE%D1\'%80%D1%83+%D0%
    BF%D0%B5%D1\'%80%D1\'%81%D0%BE%D0%BD%D0%B0%D0%BB%D0%B0%29+OR+Researcher''', headers = headers)
        print(result.status_code)