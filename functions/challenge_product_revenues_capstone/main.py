# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

# Example of expected output line (do not remove):
# print(f"{revenue[0]} has total revenue of ${revenue[1]}")


def calculate_revenue(prices,quantities_sold):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])
    return revenue

revenue = calculate_revenue(prices,quantities_sold)
revenue_per_product = list(zip(products,revenue))
print (revenue_per_product)

def formatted_output(revenues=revenue_per_product):
    # revenues = revenues.sorted()
    new_revenues = sorted(revenues)
    for i in range(len(revenue_per_product)):
        print(f"{revenues[i][0]} has total revenue of ${revenues[i][1]}")

formatted_output(revenue_per_product)

    