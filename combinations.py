icecream_prices  = {
    "Vanilla": 3.00,
    "Chocolate": 3.50,
    "Strawberry": 3.50,
    "Salted Caramel": 4.50,
    "Matcha": 4.50,
    "Cookies & Cream": 4.50,
    "Rainbow Sherbet": 4.00,
    "Bubblegum": 3.50,
    "Cotton Candy": 4.00}
topping_prices = {
    "Sprinkles": 0.50,
    "Crushed Cookies": 0.60,
    "Chocolate Chips": 0.50,
    "Crushed Nuts": 0.50,
    "Fresh Strawberries": 0.75,
    "Whipped Cream": 0.75,
    "Caramel Drizzle": 0.75,
    "Chocolate Drizzle": 0.75,
    "Toasted Coconut Flakes": 0.75,
    "Pop Rocks": 1.00,
    "Tajín Spice + Lime Zest": 1.00,
    "Gummy Bears": 1.00,
    "Mini Marshmallows": 1.00
}
for flavor, base_price in icecream_prices.items():
    for topping, topping_price in topping_prices.items():
        total_price = base_price + topping_price
        print(f"{flavor} + {topping}: ${total_price:.2f}")