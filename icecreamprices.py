icecream_prices = {
    "Single Scoop": 3.00,
    "Double Scoop": 5.50,
    "Triple Scoop": 7.50,
    "Ice Cream Bar": 2.50,
    "Popsicle": 2.00,
    "Mini Tub": 3.50
}
customer_order = {

    "Single Scoop": 1,
    "Ice Cream Bar": 2
}
total_price = 0
print("Receipt:")
for item, quantity in customer_order.items():
    price = icecream_prices[item]
    total_items = price * quantity
    total_price += total_items
    print(f"{item}: {quantity} x ${price:.2f} = ${total_items:.2f}")

print(f"Total Price: ${total_price:.2f}")
