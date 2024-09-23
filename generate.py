from faker import Faker
import random
from database import Author, Book

fake = Faker()

def generate_authors(num=500):
    authors = []
    for _ in range(num):
        author = Author(
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            birthdate=fake.date_of_birth(minimum_age=18, maximum_age=100),
            birthplace=fake.city()
        )
        authors.append(author)
    return authors

def generate_books(authors, num=1000):
    books = []
    categories = ['Comedy', 'Romance', 'Science', 'Fiction', 'Fantasy', 'History', 'Horror', 'Biography']
    for _ in range(num):
        book = Book(
            book_name=fake.sentence(nb_words=2),
            category=random.choice(categories),
            pages=random.randint(100, 1500),
            public_date=fake.date_of_birth(minimum_age=18, maximum_age=100),
            author_id=random.choice([author.author_id for author in authors])  
        )
        books.append(book)
    return books


