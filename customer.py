from shopping_cart import ShoppingCart
from product import Product

class Customer:

    def __init__(self, name_input, shopping_cart):
        self.name = name_input
        self.shopping_cart = shopping_cart

    def add_to_cart(self, product_input,):
        self.product = Product(product_input)
        for self.product in self.shopping_cart:
            print(self.product)

    def view_products_in_cart(self):
        self.shopping_cart = 



