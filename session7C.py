# lets code a amazon scenerio
class Menu:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories


class Product:
    def __init__(self, name, brand, price, ratings):
        self.name = name
        self.brand = brand
        self.price = price
        self.ratings = ratings

class Categories:
    def __init__(self, title, num_of_products, min_discount):
        self.title = title
        self.num_of_products = num_of_products
        self.min_discount = min_discount

    def show(self):
        print("~ ~ ~ ~ ~ ~ ~ ~ ~~ ")
        print("Title :", self.title)
        print("number of products :", self.num_of_products)
        print("minimum discount :", self.min_discount)
        print("~ ~ ~ ~ ~ ~ ~ ~ ~~")

