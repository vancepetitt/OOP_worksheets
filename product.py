class Product:
    
    def __init__(self, product_name_input, price_input, category_input, in_cart):
        self.product_name = product_name_input
        self.price = price_input
        self.category = category_input
        self.in_cart = in_cart

    def return_item_price(self):
        return self.price
    