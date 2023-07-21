

# def f(x):
#     return x*x+1
#
# result = f(100)
# print("your result is :", result)

def get_max(data):
    max = data[0]

    for idx in range(1,len(data)):
        if data[idx]>max:
            max=data[idx]

    return max

product_prize = [123,100,134,364,235,600,500]
roll_no = [2,4,5,6,1,9,7]
sales = [2000,5000,4000,1000,9000,6000,8000]

print("maximum prize is: ",get_max(product_prize))
print("maximum roll number is :" , get_max(roll_no))
print("maximum sales is :" , get_max(sales))




