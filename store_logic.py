from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class OutOfStockError(Exception):
    pass
class InvalidQuantityError(Exception):
    pass
class ThereIsNoItemError(Exception):
    pass
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def reduce_stock(self, amount):
        if amount <= 0:
            raise InvalidQuantityError("Product quantity must be positive")
        if self.quantity >= amount and self.quantity > 0:
            self.quantity -= amount
        else:
            raise OutOfStockError ("Product is out of stock")
    def add_stock(self, amount):
        if amount <= 0:
            raise InvalidQuantityError("Product quantity must be positive")
        self.quantity += amount
    def __str__(self):
        return f"Product Name: {self.name}, Product Price: {self.price}, Product Stock: {self.quantity}"
class Cart:
    def __init__(self):
        self.items = {}
    def add_item(self, product, quantity):
        if quantity <= 0:
            raise InvalidQuantityError("Product quantity must be positive")
        if product not in self.items:
            self.items[product] = quantity
        else:
            self.items[product] += quantity
    def remove_item(self, product):
        if product not in self.items:
            raise ThereIsNoItemError("There is no item in the cart")
        else:
            self.items.pop(product)
    def total_price(self):
        sum_of_products = 0.0
        for product , quantity in self.items.items():
            sum_of_products += (product.price * quantity)
        return sum_of_products
class StoreLogic:
    def __init__(self):
        self.products = {}
    def add_product(self, product):
        if product.name not in self.products:
            self.products[product.name] = product
        else:
            print("This item is already in stock")
    def find_product(self, name):
        if name not in self.products:
            return None
        else:
            return self.products[name]
    def checkout(self, cart):
        for product , quantity in cart.items.items():
            product.reduce_stock(quantity)
        return cart.total_price()
store = StoreLogic()

class ProductRequest(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    quantity:int = Field(gt=0)
class ProductResponse(BaseModel):
    name:str
    price:float
    quantity:int
@app.post("/products")
def product_request(request:ProductRequest):
    product = Product(request.name, request.price, request.quantity)
    store.add_product(product)
    return {"message": "Item added to inventory",
            "product name": request.name}
@app.get("/products", response_model=list[ProductResponse])
def get_all_products():
    return list(store.products.values())
cart_db = {}
next_cart_id = 1
@app.post("/carts")
def next_cart():
    global next_cart_id
    current_id = next_cart_id
    cart_db[next_cart_id] = Cart()
    next_cart_id += 1
    return {"message":f"New cart id created, cart id{current_id}"}
class AddItemRequest(BaseModel):
    product_name: str
    quantity: int = Field(gt=0)
@app.post("/carts/{cart_id}/items")
def add_item_cart(cart_id:int, request:AddItemRequest):
    product = store.find_product(request.product_name)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    cart = cart_db.get(cart_id)
    if cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")
    else:
        try:
            cart.add_item(product,request.quantity)
        except InvalidQuantityError as e:
            raise HTTPException(status_code=400, detail=str(e))
    return {"message":"Item added to the cart",
            "product name": request.product_name,
            "quantity":request.quantity}
@app.get("/carts/{cart_id}")
def get_all_cart_products(cart_id:int):
    cart = cart_db.get(cart_id)
    if cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")
    items_list = []
    for product, quantity in cart.items.items():
        items_list.append({"product_name":product.name, "quantity":quantity})
    return {"cart_id":cart_id,
            "items":items_list,
            "total price":cart.total_price()}
@app.post("/carts/{cart_id}/checkout")
def check_out(cart_id:int):
    cart = cart_db.get(cart_id)
    if cart is None:
        raise HTTPException(status_code=404, detail="Cart not found")
    try:
        total = store.checkout(cart)
    except OutOfStockError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except InvalidQuantityError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"total price": total}