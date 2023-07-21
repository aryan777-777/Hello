from session7A import Restaurant, Menu, Dish


def main():
    restaurant = Restaurant(
        name="Khalsa Food",
        address="33 feet road ",
        phone_no="+91 23543 53345",
        rating=4.5,
        menu=Menu(name="Indian angeethi",
                  num_of_dishes=3,
                  dishes=[
                        Dish("noodles", 50, 4.6),
                        Dish("manchurian", 70, 4.6),
                        Dish("pizza", 150, 5.0)

                  ])
    )
    restaurant.show()

if __name__ == "__main__":
    main()
