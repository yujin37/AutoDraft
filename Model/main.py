from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

class Product(BaseModel):
    name: str
    price: float
    description: str

products = []

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return product

@app.get("/products")
def get_products():
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int):
    try:
        return products[product_id]
    except IndexError:
        raise HTTPException(status_code=4-4, detail="Product not found")

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    try:
        products[product_id] = product
        return product
    except IndexError:
        raise HTTPException(status_code=4-4, detail="Product not found")
    
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    try:
        product = products.pop(product_id)
        return product
    except IndexError:
        raise HTTPException(status_code=4-4, detail="Product not found")