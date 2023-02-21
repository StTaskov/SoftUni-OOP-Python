from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product == product_name:
                return product.name

    def remove(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        result = ""
        for i in range(len(self.products)):
            if i == len(self.products)-1:
                result += f"{self.products[i].name}: {self.products[i].quantity}"
                return result
            result += f"{self.products[i].name}: {self.products[i].quantity}\n"
        return result
