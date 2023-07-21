# Explore set
john_followers = {"aryan", "naman", "sia", "sonu", "paras"}
print(john_followers, type(john_followers))

numbers = list(range(10, 101, 10))
print(numbers, type(numbers))

numbers = set(numbers)
print("number is now :", numbers)
print("number type is :", type(numbers))

numbers.add(14)
numbers.add(20)
numbers.add(30)
print("numbers after add is :", numbers)

numbers.pop()
numbers.pop()
print("numbers after pop :", numbers)


numbers.remove(90)
print("numbers after remove :", numbers)
numbers.discard(80)
print("numbers after discard is :", numbers)




john_followers = {"fionna", "sia", "jack", "joe", "harry"}
naman_followers = {"aryan", "sonu", "suman", "sia", "joe"}
aryan_followers = {"fionna", "sonu", "suman", "carry", "paras"}

followers = john_followers.intersection(aryan_followers)
print(followers)
followers = naman_followers.intersection(aryan_followers)
print(followers)

print("issubset :", john_followers.issubset(aryan_followers))
print("issuperset :", john_followers.issubset(aryan_followers))


a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

c = a-b
print(c)

c = a & b
print(c)

c = a.symmetric_difference(b)

