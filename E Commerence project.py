products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Mobile", "price": 20000},
    3: {"name": "Headphones", "price": 2000},
    4: {"name": "Mouse", "price": 500}
}

cart = []
total = 0

print("----- Product List -----")
for pid, product in products.items():
    print(pid, product["name"], "-", product["price"])

while True:
    choice = int(input("Enter Product ID (0 to Exit): "))

    if choice == 0:
        break

    if choice in products:
        qty = int(input("Enter Quantity: "))
        amount = products[choice]["price"] * qty
        total += amount

        cart.append({
            "Product": products[choice]["name"],
            "Quantity": qty,
            "Amount": amount
        })

        print("Product Added Successfully")
    else:
        print("Invalid Product ID")

print("\n----- Shopping Cart -----")
for item in cart:
    print(item["Product"], "-", item["Quantity"], "x =", item["Amount"])

print("------------------------")
print("Total Bill =", total)
