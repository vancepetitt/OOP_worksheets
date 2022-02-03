from product import Product

class ShoppingCart:

    def __init__(self, products_in_cart):
        self.products_in_cart = []
     
    def total_in_cart(self):
        total_value = 0
        for product in self.products_in_cart:
            product = Product(product)
            item_value = product_value


