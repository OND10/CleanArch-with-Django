from dataclasses import dataclass
from datetime import date

@dataclass
class BookDto:
    title:str
    author:str
    published_date:date
    pin:str
    

    
      
