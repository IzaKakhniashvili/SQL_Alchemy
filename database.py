from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship



Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    birthdate = Column(Date, nullable=False)
    birthplace = Column(String, nullable=False)
    
    books = relationship('Book', back_populates='author')
    
    
    
class Book(Base):
    __tablename__ = 'books'
    
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    book_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    public_date = Column(Date, nullable=False)
    
    author_id = Column(Integer, ForeignKey('authors.author_id'), nullable=False)
    author = relationship('Author', back_populates='books')
    
    
    
engine = create_engine('sqlite:///book_authors.db', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)