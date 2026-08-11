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
        return f"The total price is :{sum_of_products}"
class Store:
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