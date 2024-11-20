from people.Domain.Interfaces.IBookRepository import IBookRepository
from people.Domain.Entities.Book import Book
from people.models import BookModel  # Django model
from typing import List

class BookRepository(IBookRepository):
    def get_all_books(self) -> List[Book]:
        books = BookModel.objects.all()
        return [Book(id=b.id, title=b.title, author=b.author, published_date=b.published_date, pin=b.pin) for b in books]

    def add_book(self, book: Book) -> Book:
        book_instance = BookModel.objects.create(
            title=book.title,
            author=book.author,
            published_date=book.published_date,
            pin=book.pin
        )
        return Book(
            id=book_instance.id,
            title=book_instance.title,
            author=book_instance.author,
            published_date=book_instance.published_date,
            pin=book_instance.pin
        )