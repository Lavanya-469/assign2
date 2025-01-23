toppings = {"Sprinkles" : 0.50, 
"Crushed Cookies" : 0.60,  
"Chocolate Chips" : 0.50, 
"Crushed Nuts" : 0.50,
"Fresh Fruit" : 0.75,  
"Whipped Cream" : 0.75,
"Caramel Drizzle" : 0.75, 
"Chocolate Drizzle" : 0.75,
"Toasted Coconut Flakes" : 0.75,  
"Pop Rocks" : 1.00,
"Tajín Spice + Lime Zest" : 1.00,  
"Gummy Bears" : 1.00,
"Mini Marshmallows" : 1.00}
selected_toppings = ["Chocolate Chips", "Whipped Cream", "Gummy Bears"]
total_cost = 0
for topping in selected_toppings:
    total_cost += toppings[topping]
print(f"total cost of all selected topping: ${total_cost:.2f}")