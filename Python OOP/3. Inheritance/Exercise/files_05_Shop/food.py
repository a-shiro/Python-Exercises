from files_05_Shop.product import Product


class Food(Product):
    def __init__(self, name):
        Product.__init__(self, name, 15)
