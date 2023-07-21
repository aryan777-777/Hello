# Relationship mapping
# 1 restaurant has 1`menu
# 1 menu has many dishes


class Dish:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def show(self):
        print("~~~~~~~~~~~~~~")
        print("Name :", self.name)
        print("price :", self.price)
        print("rating :", self.rating)
        print("~~~~~~~~~~~~~~")


class Menu:
    def __init__(self, name, num_of_dishes, dishes):
        self.name = name
        self.num_of_dishes = num_of_dishes
        self.dishes = dishes



    def show(self):
        print("Name :", self.name)
        print("Number of dishes :", self.num_of_dishes)

        for idx in range(len(self.dishes)):
            self.dishes[idx].show()


class Restaurant:
    def __init__(self, name, address, phone_number, rating, menu):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.rating = rating
        self.menu = menu

    def show(self):
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
        print("Name :", self.name)
        print("address :", self.address)
        print("phone_number :", self.phone_number)
        print("rating :", self.rating)
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")
        self.menu.show()

def main():
    dish1 = Dish(name="noodles", price=70, rating=4.5)
    dish2 = Dish(name="burger", price=40, rating=4.6)
    dish3 = Dish(name="chaamp", price=50, rating=4.8)
    dish4 = Dish(name="pizza", price=100, rating=4.3)

    dishes = [dish1, dish2, dish3, dish4]

    menu = Menu(name="Indian food", num_of_dishes=len(dishes),  dishes=dishes)

    restaurant = Restaurant(name="Khalsa burger", address="33 feet road ldh",phone_number="+91 21233 34532",rating=4.6, menu=menu)

    restaurant.show()


if __name__ == "__main__":
    main()
