produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = list()
groceries.append(produce)
groceries.append(dairy)

print (groceries)

for section in groceries:
    for item in section:
        print (f"Item name: {item}")