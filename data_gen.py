import csv
from faker import Faker

fake = Faker('en_AU')


countries = []
for _ in range(500):
    countries.append([fake.country()])

with open("countries.csv", "w") as f:
    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    wr.writerows(countries)