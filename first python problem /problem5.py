# Taking the amount of money as input
money = int(input())

# Determining what she will buy based on the amount of money
if money >= 20000:
    print("Gucci Bag")
    print("Gucci Belt")
elif money >= 10000:
    print("Gucci Bag")
elif money >= 5000:
    print("Levis Bag")
else:
    print("Something from New Market")
