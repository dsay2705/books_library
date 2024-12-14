#data generation
from faker import Faker
import csv
import random

fake = Faker()

genres = ["Fantasy", "Mystery", "Romance", "Historical", "Thriller"]
num_lines = 50


def create_book():
    data = []
    for i in range(num_lines):
        publication_date = fake.date_between(start_date='-100y', end_date='today')
        book = {
            "Author": fake.name(),
            "Title": fake.sentence(),
            "Genre": random.choice(genres),
            "PublicationDate": publication_date.strftime("%Y-%m-%d")

        }
        data.append(book)
    return data



books_data = create_book()

csv_file = "books_database.csv"
with open(csv_file,"w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Author", "Title", "Genre", "PublicationDate"])
    writer.writeheader()
    writer.writerows(books_data)



