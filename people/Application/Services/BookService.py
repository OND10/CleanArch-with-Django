from people.Domain.Interfaces.IBookRepository import IBookRepository
from people.Application.Interfaces.IBookService import IBookService
from people.Application.DTOs.BookDto import BookDto
from people.Application.DTOs.BookResponseDto import BookResponseDto

class BookService(IBookService):
    def __init__(self, book_repository: IBookRepository):
        self.book_repository = book_repository
     
    def get_all_books(self)->list[BookResponseDto]:
        books = self.book_repository.get_all_books()
        return [BookResponseDto(**book.__dict__) for book in books]
    
    def add_book(self, book_data:BookDto)->BookDto:
        book = self.book_repository.add_book(book_data)
        
        filtered_data = {
            key: value for key, value in book.__dict__.items()
            if key in ['title', 'author', 'published_date', 'pin']
        }
        return BookDto(**filtered_data)    
            
            