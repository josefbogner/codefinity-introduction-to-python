# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for key in products:
    # print (key)
    # print (products[key])
    products[key][0] = float(products[key][0])
    price = products[key][0]
    products[key][1] = int(products[key][1])
    quantity_sold = products[key][1]
    total_sales = price * quantity_sold
    total_sales_list.append(total_sales)
    # print (key)
    # print (products[key])
    print (F"Total sales for {key}: ${total_sales}")

total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)
print (F"Total sum of all sales: ${total_sum}")
print (F"Minimum sales: ${min_sales}")
print (F"Maximum sales: ${max_sales}")