from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import hashlib

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []
# Pydantic model for the text field
class TextData(BaseModel):
    text: str

@app.post("/items/")
async def create_item(item: Item):
    return item
# Welcome Note
@app.get("/")
def read_root():
    return {"message": "Welcome to the API! Customized for [Your Name]"}

# FastAPI endpoint to accept POST request with a JSON body containing a single field "text"
@app.post("/generate/")
def generate(data: TextData):
    # Generate a checksum of the text
    checksum = hashlib.md5(data.text.encode()).hexdigest()
    return {"checksum": checksum}