from dataclasses import dataclass
from datetime import date

@dataclass
class BookResponseDto:
    id:int
    title:str
    author:str
    published_date:date
    pin:str
    

    
      
