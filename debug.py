from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.author import Author
from models.category import Category
from models.book import Book
from models import Base

DATABASE_URL = "sqlite:///library.db"  

def create_session():
    engine = create_engine(DATABASE_URL, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

def initialize_database():
    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(engine)  
    print("Database tables created!")

if __name__ == '__main__':
    initialize_database()

    
