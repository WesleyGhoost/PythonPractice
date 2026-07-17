pizza = {
    "name": "Catupiry Pizza",
    "price": 50.00,
    "calories_per_slice": 300,
    "toppings": ["mussarela", "basil"]
}

print(pizza.get("price",[]))
print(pizza.keys())
print(pizza.values())
print(pizza.items())

pizza.pop("price")
pizza.update({"total_time": 25})

print(pizza)


products = {
    "Notebook": 3000,
    "Tablet": 1500,
    "Playstation 5": 5000,
    "Monitor": 2000
}

for index, product in enumerate(products.items(), 1):
    print(index, product)

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)