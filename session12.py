# cafe_name = "aryan's cafe"
# print(cafe_name)
#
# print("cafe_name is :", type(cafe_name), id(cafe_name))

names = "aryan, naman, sunny, bobby, rishu, rahul"
print(names, id(names))
print(names[0])
hello = names * 2
print(hello, id(hello))

print("aryan" in names)
print("aryan" not in names)

names = names.upper()
print("names now is :", names, id(names))