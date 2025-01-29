


def summarize_items(name, *args, **kwargs):
    
    print(f"name of the person: {name}")
    print(f"arbitary number of items: {len(args)}")

    return kwargs
print(summarize_items("john", 1, 2, 3, 4, date = "01-27-2025", location = "saint louis"))