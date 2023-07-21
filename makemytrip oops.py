class travel:
    def __init__(self, source_location, destination, date, no_of_travellers):
        self.source_location = source_location
        self.destination = destination
        self.date = date
        self.no_of_travellers = no_of_travellers

    def show(self):
        print("~~~~~~~~~~$$$~~~~~~~~~~")
        print("Source location is : ", self.source_location)
        print("destination is : ", self.destination)
        print("date of travelling is :", self.date)
        print("number of travellers are :", self.no_of_travellers)
        print("~~~~~~~~~~$$$~~~~~~~~~~~")

travel1 = travel("Ludhiana", "Patna", "23_july", 7)
travel2 = travel("Patna", "Ludhiana", "6_august",4)

travel1.show()
travel2.show()

