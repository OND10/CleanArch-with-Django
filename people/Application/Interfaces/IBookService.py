from abc import ABC, abstractmethod
from typing import List
from people.Application.DTOs.BookDto import BookDto
from people.Application.DTOs.BookResponseDto import BookResponseDto

class IBookService(ABC):
    
    @abstractmethod
    def get_all_books(self)->List[BookResponseDto]:
        pass
    
    @abstractmethod
    def add_book(self, book_date : BookDto)->BookDto:
        pass



