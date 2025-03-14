# lib/helpers.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.book import Book
from models.author import Author
from models.category import Category

DATABASE_URL = "sqlite:///library.db"

def create_session():
    engine = create_engine(DATABASE_URL, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

def add_book():
    title = input("Enter book title: ")
    author_name = input("Enter author name: ")
    category_name = input("Enter category: ")

    session = create_session()

    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
        session.add(author)

    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)

    # Add book
    book = Book(title=title, author=author, category=category)
    session.add(book)
    session.commit()
    print(f"Book '{title}' added successfully!")

def view_books():
    session = create_session()
    books = session.query(Book).all()
    for book in books:
        print(book)

def view_authors():
    session = create_session()
    authors = session.query(Author).all()
    for author in authors:
        print(author)

def view_categories():
    session = create_session()
    categories = session.query(Category).all()
    for category in categories:
        print(category)

def exit_program():
    print("Goodbye!")
    exit()
