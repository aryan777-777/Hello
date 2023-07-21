# for each or Enhaced for loop

data = list(range(10, 101, 10))
print("data :", data)

# for idx in range(len(data)):
#     print(data[idx])


# elements can be any name of your choice
# work for list ,tuple, set

for elements in data:
    print(elements)


student = {
    "rolling": 101,
    "name": "fionna",
    "age": 23
}

items = student.items()
for item in items:
    print(item)
    print(item[0], item[1])