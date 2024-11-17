from dataclasses import dataclass
from datetime import date


@dataclass
class Book:
    id:int
    title:str
    author:str
    published_date: date
    pin:str
    
    
    