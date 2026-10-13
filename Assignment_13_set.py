



prices = {
    "rice": 20,
    "pulse": 40,
    "wheat": 50,
    "bread": 10,
    "turmeric": 80
}

out_of_stock = {"rice", "bread"}

items = ["chapati", "suzi", "rusk"]

total = 0

for i in items:
    if i in out_of_stock:
        print("unavailable")
    elif i in prices:
        total += prices[i]
    else:
        print(i, "is not available in the price list")

print("Final order value:", total )
