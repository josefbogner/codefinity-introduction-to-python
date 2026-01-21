grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}


if (grocery_inventory["Eggs"][1]) > 5:
    print (f"Eggs are too expensive, reducing the price by $1.")
    old_eggs = list(grocery_inventory["Eggs"])
    old_eggs[1] -= 1
    # print (old_eggs)
    new_eggs = tuple(old_eggs)
    # print (new_eggs)
    grocery_inventory["Eggs"] = new_eggs
    # (grocery_inventory["Eggs"][1]) = (grocery_inventory["Eggs"][1]) - 1
    # print (grocery_inventory["Eggs"][1])
else:
    print (f"The price of Eggs is reasonable.")

grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)

print (f"Inventory after adding Tomatoes: {grocery_inventory}")

if (grocery_inventory["Milk"][2]) < 10:
    print (f"Milk needs to be restocked. Increasing stock by 20 units.")
    old_milk = list(grocery_inventory["Milk"])
    old_milk[2] += 20
    new_milk = tuple(old_milk)
    grocery_inventory["Milk"] = new_milk
else:
    print (f"Milk has sufficient stock.")

if (grocery_inventory["Apples"][1]) > 2:
    grocery_inventory.pop["Apples"]
    print (f"Apples removed from inventory due to high price.")

print (f"Updated inventory: {grocery_inventory}")