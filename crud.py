from models import Book, Member
from database import session

def add_book(title, author, isbn, count):
    # print("Adding book to db")
    book = Book(title=title, author=author, isbn=isbn, count=count)
    session.add(book)
    session.commit()

def get_book():
    return session.query(Book).all()

def add_member(name, email):
    # print("Adding new Member")
    new_member = Member(name=name, email=email)
    session.add(new_member)
    session.commit()

def get_member():
    return session.query(Member).all()