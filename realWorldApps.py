restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Water": 1.00, "Coke": 3.50}    # Add beverages

restaurant_menu["Main Course"]["Steak"] = 17.99     # Adjust Steak

del restaurant_menu["Starters"]["Bruschetta"]       # Delete Bruschetta

print("Updated Menu:")
for category, items in restaurant_menu.items():
    print("\nCategory:", category)
    for item, price in items.items():
        print(item," $%.2f" % price)                # Thanks to StackOverflow for telling me how to print rounded :)
