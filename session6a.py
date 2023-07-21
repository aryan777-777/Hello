# Standardization in OOPS
class dish:
    def __init__(self, name="samosa", price=40, ratings=4.5):
        self.name = name
        self.price = price
        self.ratings = ratings

    def show(self):
        print("~~~~~~~~~~~~~~~~~")
        print("name :", self.name)
        print("price :", self.price)
        print("ratings :", self.ratings)
        print("~~~~~~~~~~~~~~~~~~")

dish1=dish("maggie",12,4.5)
dish2=dish("pizza",350,5.0)
dish1.show()
dish2.show()
print(vars(dish1))  # we should avoid this method