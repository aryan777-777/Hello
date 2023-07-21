print("MUlti value container")
numbers=10,20,30,40,50 #homogeneous             #if we will not mention () or [] , by default it will be a tuple where we cannot delete , update or add new element
print(numbers,id(numbers),type(numbers))

#by default indexing is done in multi value container (tuple)
print(numbers[1])
print(numbers[3],id(numbers[3]))

data=[10,"jim",20,"jenny","zomato"] #hetrogeneous       #[] shows list in which we can modify our data
print(data)

#Delete operation
del data[2]
print(data)

#adding data in our list
data[2]="awesome"
print(data)
