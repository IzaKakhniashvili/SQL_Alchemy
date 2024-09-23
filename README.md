# Books And Authors Database


## Description
In this project the main goal is to create a SQLite database to store books and their authors
uing SQLAlchemy. It generates fake authors and their owned fake books using Faker.

## Features
- Generates random authors using Faker with details like firstname, lastname, birthdate and birthplace.
- Generates random books using Faker with details like name, author name, category, pages and publication date.
- Performs queries to find:
    - The book with the most pages.
    - The average number of pages.
    - The youngest author.
    - Authors without any book.
    - Authors with 3 or more books.
    