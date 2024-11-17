from abc import ABC,abstractmethod
from people.Domain.Entities.Book import Book
from typing import List



class IBookRepository(ABC):

    @abstractmethod
    def get_all_books(self)->List[Book]:
        pass

    @abstractmethod
    def add_book(self, book:Book)->Book:
        pass

