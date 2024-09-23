from sqlalchemy.orm import Session
from sqlalchemy import func
from database import Author, Book

def get_most_pages_book(session):
    return session.query(Book).order_by(Book.pages.desc()).first()

def get_average_pages(session):
    return session.query(func.avg(Book.pages)).scalar()

def get_youngest_author(session):
    return session.query(Author).order_by(Author.birthdate.desc()).first()

def get_authors_without_books(session):
    return session.query(Author).outerjoin(Book).filter(Book.book_id == None).all()


def get_authors_with_three_or_more_books(session):
    return (
        session.query(Author)
        .join(Book)
        .group_by(Author.author_id)
        .having(func.count(Book.book_id) >= 3)
        .all()
    )