class restaurant:
    pass
# restaurant1 is a reference variable
restaurant1 = restaurant()
restaurant2 = restaurant()
restaurant3 = restaurant1
print("restaurant 1 is ", restaurant1, id(restaurant1), hex(id(restaurant1)), type(restaurant1))
print("data inside the object is :", vars(restaurant1))


# operations on  object
restaurant1.name = "khalsa food "
restaurant1.phone_number = 9876543210
restaurant1.email = "khalsa@gamil.com"
restaurant1.ratings = 4.6

print("data inside the restaurant1 is now :", vars(restaurant1))



restaurant2.name = "foodie point"
restaurant2.phone_number = 1234567890
restaurant2.email = "foodiepoint@gmail.com"
restaurant2.ratings = 4.4
print("data inside the restaurant2 is :", vars(restaurant2))



# update operation
restaurant2.name = "burgerking"
print("data inside the restaurant2 is :", vars(restaurant2))


#delete operation
del restaurant1.phone_number
print("data inside the restaurant1 is now :", vars(restaurant1))

print("data inside the restaurant3 is :", vars(restaurant3))

del restaurant1
print("data inside the restaurant3 is : ",vars(restaurant3))
