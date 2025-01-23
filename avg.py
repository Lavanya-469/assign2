flavors = ["Vanilla", "Chocolate", "Strawberry", "Salted Caramel", "Matcha", "Cookies & Cream", "Rainbow Sherbet", "Bubblegum", "Cotton Candy", "Mango", "Pineapple-Coconut", "Key Lime Pie"]

total_length = 0

for flavor in flavors:
    total_length += len(flavor)
    average_length = total_length/len(flavors)

print(f"the average length of the flavor names: {average_length:.2f}")