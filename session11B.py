 # Explore dictionary

my_data = {101: "john", 102: "aryan", 103: "naman", 104: "suman"}
print("my data :", my_data)
print("min :", min(my_data))
print("max :", max(my_data))
print("sum :", sum(my_data))


# there are two ways to find the indexing
print(my_data[102])
print(my_data.get(102))

my_data.pop(102)
print(my_data)


my_data[999] = "mahesh"
print(my_data)

my_data[999] = "dalle"
print(my_data)

del my_data[999]

columns = ['from', 'to']
flight = {}.fromkeys(columns, "delhi")
print(flight)





columns = ["ludhiana", "chandigarh", "patiala", "delhi"]
# item() # list of tuples
population = {}.fromkeys(columns, 1200)
print(population)
population["delhi"] = 3100
print(population)


# convert dictionary into list of tuples :
items = list(population.item())
print("items :", items)