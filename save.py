import csv

def save_to_csv(jobs):
    file = open('test.csv', mode='w', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(['title', 'company', 'location', 'link'.encode("cp1251")])
    for job in jobs:
        writer.writerow(list(job.values()))
    return