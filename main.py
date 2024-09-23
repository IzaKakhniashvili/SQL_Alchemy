from database import Session
from generate import generate_authors, generate_books
from queries import (
    get_most_pages_book,
    get_average_pages,
    get_youngest_author,
    get_authors_without_books,
    get_authors_with_three_or_more_books,
)

def main():
    session = Session()
    
    authors = generate_authors()
    session.add_all(authors)
    session.commit()

    books = generate_books(authors)
    session.add_all(books)
    session.commit()

    most_pages_book = get_most_pages_book(session)
    print(f"Book with the most pages: {most_pages_book.book_name}, Pages: {most_pages_book.pages}")

    average_pages = get_average_pages(session)
    print(f"Average number of pages: {round(average_pages)}")

    youngest_author = get_youngest_author(session)
    print(f"Youngest author: {youngest_author.firstname} {youngest_author.lastname}, Birthdate: {youngest_author.birthdate}")

    authors_without_books = get_authors_without_books(session)
    print(f"Authors without books: {[f'{author.firstname} {author.lastname}' for author in authors_without_books]}")

    authors_with_three_or_more_books = get_authors_with_three_or_more_books(session)
    print("Authors with three or more books:")
    for author in authors_with_three_or_more_books:
        print(f"{author.firstname} {author.lastname}")
    session.close()

if __name__ == "__main__":
    main()