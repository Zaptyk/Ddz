class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - {self.price} грн (В наявності: {self.stock})"


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            self.items[product] = self.items.get(product, 0) + quantity
            product.stock -= quantity
        else:
            print("Недостатньо товару!")

    def total_price(self):
        return sum(product.price * qty for product, qty in self.items.items())

    def show_cart(self):
        for product, qty in self.items.items():
            print(f"{product.name} x{qty} - {product.price * qty} грн")


# Приклад використання
milk = Product("Молоко", 30, 10)
cart = Cart()
cart.add_product(milk, 2)
cart.show_cart()