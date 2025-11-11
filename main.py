from fastapi import FastAPI,Query
from pydantic import BaseModel
from typing import Annotated


app = FastAPI()

class Item(BaseModel):
    id : int
    name : str
    price : float
    descr : str
    type  : str


@app.get("/")
def home():
    return "Home Page for items"

@app.get("/searchProduct/{id}")
def search(id : int):
    return id

@app.get("/getProducts")
def recommendation(name : Annotated[str , Query(min_length=1,max_length=20)]):
    return name

@app.post("/item")
def addProdcut(item : Item):
    return "ok"