from typing import List
from pydantic import BaseModel, validator, Field
from datetime import date

class Genre(BaseModel):
    name: str

class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    geners: List[Genre]
    pages: int

class Author(BaseModel):
    first_name: str = Field(..., max_length=25)
    last_name: str
    age: int = Field(..., gt=15, lt=90, description='Atuthot must be 15..90')
    
    '''
    @validator('age')
    def check_age(cls, v):
        if v<15: 
            raise ValueError('Author age must be more 15')
    '''