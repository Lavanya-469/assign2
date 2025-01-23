sales_transaction  = [
    ("Vanilla",3.00),
    ("Chocolate",3.50),
    ("Strawberry",3.50),
    ("Salted Caramel",4.50),
    ("Matcha",4.50),
    ("Cookies & Cream",4.50),
    ("Rainbow Sherbet",4.00),
    ("Bubblegum",3.50),
    ("Cotton Candy",4.00),]
total_revenue = 0

for item, price in sales_transaction:
    total_revenue += price

print(f"Total revenue of the day: ${total_revenue:.2f}")
