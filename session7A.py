class Dish:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~")
        print("Name :", self.name)
        print("Name :", self.price)
        print("Name :", self.rating)
        print("~~~~~~~~~~~~~~~~~~~~~~")


class Menu:
    def __init__(self, name, num_of_dishes, dishes):
        self.name = name
        self.num_of_dishes = num_of_dishes
        self.dishes = dishes


    def show(self):
        print("~ ~ ~ ~ ~ ~ ~")
        print("Name :", self.name)
        print("Number of dishes :", self.num_of_dishes)
        print("~ ~ ~ ~ ~ ~ ~")

        for idx in range(len(self.dishes)):
            self.dishes[idx].show()


class Restaurant:
    def __init__(self, name, address, phone_no, rating, menu):
        self.name = name
        self.address = address
        self.phone_no = phone_no
        self.rating = rating
        self.menu = menu


    def show(self):
        print("Name :", self.name)
        print("address :", self.address)
        print("Phone number :", self.phone_no)
        print("Rating :", self.rating)
        self.menu.show()
