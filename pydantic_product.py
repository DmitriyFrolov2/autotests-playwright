from pydantic import BaseModel, Field


class Market(BaseModel):
    id: int
    name: str

class Product(BaseModel):
    name: str
    price: float = Field(...,gt=0, description="Цена должна быть больше 0")
    tags: list[str] = []
    market: Market

product_data= {
    "name": "Product 1",
    "price": 10.99,
    "tags": ["electronic", "smartphone"],
    "market": {
        "id": 1,
        "name": "Market 1"
}
}
product = Product(**product_data)
print(product)