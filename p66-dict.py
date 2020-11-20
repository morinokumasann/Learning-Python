
items = ["fruits","books","others"]
prices = [96,98,95]

d = {item.upper():price for item, price in zip(items,prices)}
print(d)
