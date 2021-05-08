from fastapi import FastAPI, Query, Path
import uvicorn
from schemas import Book
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
def create_book(item:Book):
    return item

@app.get('/book')
def get_book(q: List[str] = Query(["test", "test2"], description="search book")):
    return q 

@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20)):
    return {"pk": pk}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
