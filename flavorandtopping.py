flavors = ["vanilla", "chocolate", "strawberry", "salted caramel", "matcha", "cookies & cream", "rainbow sherbet", "bubblegum", "cotton candy"]
toppings = ["Sprinkles",  "Crushed Cookies", "Chocolate Chips","Crushed Nuts", "Fresh Strawberries", "Whipped Cream",  "Caramel Drizzle",   "Chocolate Drizzle",  "Toasted Coconut Flakes","Pop Rocks", "Tajín Spice + Lime Zest", "Gummy Bears", "Mini Marshmallows"]
print("combinations of one flavor with one topping")
for flavor in flavors:
    for topping in toppings:
        print(f"{flavor} and {topping}")