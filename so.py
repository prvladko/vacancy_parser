import requests
from bs4 import BeautifulSoup

URL = 'https://stackoverflow.com/jobs?q=python'

def extract_max_page():
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, 'html.parser')
    pages = soup.find('div', {'class': 's-pagination'}).find_all('a')
    last_page = int(pages[-2].get_text(strip=True))
    return last_page

def extract_job(html):
    title = html.find('h2').find('a').text
    company_row = html.find('h3').find_all('span', recursive=False)
    company = company_row[0].get_text(strip=True)
    location = company_row[1].get_text(strip=True)
#   так тоже можно упростить, если точно знать сколько элементов будет в массиве, можно сразу записать их в нужные переменные в одной строке
#   company, location = html.find('h3').find_all('span')
#   company = company.get_text(strip=True)
#   location = location.get_text(strip=True)
    print(company, location)
    return {'title': title, 'company': company}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f'{URL}&pg={page+1}')
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all('div', {'class': '-job'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    max_page = extract_max_page()
    jobs = extract_jobs(max_page)
    return []