# Explore list in python
numbers = list(range(10, 101, 10))
print(numbers)
print(type(numbers))
numbers.append(39)
numbers.append(30)
print(numbers)
print("sum :", sum(numbers))
print("Max :", max(numbers))
print("Min :", min(numbers))
print("length :", len(numbers))

reverse_numbers = list(reversed(numbers))
print("Reversed numbers are :", reverse_numbers)
print("index of 20 is : ", numbers.index(20))
print("count of 30 is : ", numbers.count(30))

data = [12,34,56,34,75,234]
print("data is : ", data)
data.sort()
print("now the data is :", data)

names = ["aryan","naman","anmol","sonu"]
names.sort()
print("names :", names)
print("min :", min(names))
print("max :", max(names))

names.remove("aryan")
data.remove(34)
print(names)
print(data)

data = [10,20,30,40,50]
# data.pop(0)
print(data)

data.insert(1,90)
print(data)
