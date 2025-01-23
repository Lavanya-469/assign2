classic_flavors = ["vanilla", "chocolate", "strawberry"]
trendy_flavors = ["salted caramel", "matcha", "cookies & cream"]
kid_friendly = ["rainbow sherbet", "bubblegum", "cotton candy"]

flavor = input("Enter ther ice cream flavor: ")

if flavor in classic_flavors:
    print(f"{flavor} is classified as classic_flavor")

elif flavor in trendy_flavors:
    print(f"{flavor} is classified as trendy_flavor ")

elif flavor in kid_friendly:
    print(f"{flavor} ia classified as kid_friendly")
    
else:
    print(f"sorry, we dont have {flavor} flavor")


