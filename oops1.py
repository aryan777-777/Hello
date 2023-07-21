class Dish:
    def __init__(self, name="", price=0, ratings=4.0):
        self.name = name
        self.price = price
        self.ratings = ratings

    def show(self):

        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Name :", self.name)
        print("Price :", self.price)
        print("Ratings :", self.ratings)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")




dish1 = Dish("noodles", 70, 4.3)
dish2 = Dish("burger", 30, 4.6)
dish3 = Dish()
dish1.show()
dish2.show()
dish3.show()

# dish1=dish()
# dish2=dish()
#
#
# dish1.name="maggie"
# dish1.price=30
# dish1.ratings=4.5
#
#
# dish2.name="noodles"
# dish2.price=70
# dish2.ratings=4.6

