import csv

def save_to_csv(jobs):
    file = open('test.csv', mode='w')
    writer = csv.writer(file)
    writer.writerow(['title', 'company', 'location', 'link'])
    print(file)
    return