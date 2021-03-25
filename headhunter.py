import requests
from bs4 import BeautifulSoup

ITEMS = 100
URL = '''https://hh.ru/search/vacancy?schedule=remote&search_field=name&
    st=searchVacancy&text=%D1\'%80%D0%B5%D0%BA%D1\'%80%D1\'%83%D1\'%82%D0%B5%D1%80+OR+recruiter+OR+
    Recruitment+%28talent+aqusition%29+OR+\'%28%D0%BF%D0%BE%D0%B4%D0%B1%D0%BE%D1\'%80%D1%83+%D0%
    BF%D0%B5%D1\'%80%D1\'%81%D0%BE%D0%BD%D0%B0%D0%BB%D0%B0%29+OR+Researcher'''

headers = {
        'Host': 'hh.ru',
        'User-Agent': 'Safari',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

def extract_max_page():
    hh_request = requests.get(f'{URL}&items_on_page={ITEMS}', headers = headers)
    hh_soup = BeautifulSoup(hh_request.text, 'html.parser')
    pages = []
    paginator = hh_soup.find_all('span', {'class': 'pager-item-not-in-short-range'})
    for page in paginator:
        pages.append(int(page.find('a').text))
    return pages[-1] 

def extract_job(html):
    title = html.find('a').text
    link = html.find('a')['href']
    company = html.find('div', {'class': 'vacancy-serp-item__meta-info-company'}).find('a').text
    company = company.strip()
    location = html.find('span', {'data-qa': 'vacancy-serp__vacancy-address'}).text
    location = location.partition(',')[0]
    return{'title': title, 'company': company, 'location': location, 'link': link}

def extract_hh_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f'Парсинг страницы {page}')
        result = requests.get(f'{URL}&page = {page}', headers = headers)
        print(result.status_code)
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class': 'vacancy-serp-item'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)        
    return jobs