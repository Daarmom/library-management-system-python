from models import Book, Member, Transaction
from database import session
from datetime import date

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

def issue_book(book_id, member_id):
    book = session.query(Book).filter_by(id = book_id).first()
    if book and book.count >0 :
        transaction = Transaction(book_id = book_id, member_id=member_id, issue_date = date.today())
        book.count -= 1
        session.add(transaction)
        session.commit()
        print("> Book issued")
    else:
        print("> Book not available for issue")

def return_book(transaction_id):
    transaction = session.query(Transaction).filter_by(id = transaction_id).first()
    if transaction and not transaction.return_date :
        transaction.return_date = date.today()
        book = session.query(Book).filter_by(id = transaction.book_id).first()
        book.count += 1
        session.commit()
        print("> Book returned")
    else:
        print("> Book not available for return")

def get_transactions_by_member(member_id):
    return session.query(Transaction).filter_by(member_id=member_id).all()

def delete_book(book_id):
    book = session.query(Book).filter_by(id = book_id).first()
    if book and book.count>0:
        # session.delete(book)
        book.count = 0
        session.commit()
        print("> Book in stock deleted")
    else:
        print("> Book not in stock ",book_id)
