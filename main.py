from fastapi import FastAPI, Query, Path, Body
import uvicorn
from schemas import Book, Author
from typing import List

app = FastAPI()

@app.get('/')
def home():
    return {"key": "hellow"}

@app.get('/{pk}')
def get_item(pk: int, q: int = None):
    return {"key": pk, "q": q}

@app.get('/user/{pk}/items/{item}')
def get_user_item(pk: int, item: str):
    return {"user": pk, "items": item}

@app.post('/book')
def create_book(item:Book, author: Author, quanitity: int = Body(...)):
    return {"item": item, "author": author, "quanitity": quanitity}

@app.post('/author')
def create_book(author: Author = Body(...)):
    return {"author": author}

@app.get('/book')
def get_book(q: List[str] = Query(["test", "test2"], description="search book")):
    return q 

@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):
    return {"pk": pk}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
