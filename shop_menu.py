import time

print("Chicken Shop Takeaway")
print("Oxford Street, Westminster")
print("London, W1A 1AA")
print("------------------------")
print("Mon 25 Dec 2025  20:45PM")
print("------------------------")

# Menus
normal_mains = ["Strip Burger", "Fillet Burger", "Zinger Burger", "Spicy Chicken Wrap"]
vegetarian_mains = ["Vegetable Burger", "Salad Wrap", "Cheese & Onion Pastry"]
normal_sides = ["Spicy Wings", "Peri Wings", "Peri Fries", "Regular Fries"]
vegetarian_sides = ["Regular Fries", "Coleslaw", "Salad", "Corn On Cob"]
drinks = ["Coca Cola", "Pepsi Max", "7UP", "Capri-Sun", "Water"]

def choose_item(menu_list, category_name):
    print(f"Here is a list of {category_name}:")
    for i, item in enumerate(menu_list, start=1):
        print(f"{i}. {item}")
    while True:
        try:
            choice = int(input(f"Select your {category_name} (1-{len(menu_list)}): "))
            if 1 <= choice <= len(menu_list):
                selected = menu_list[choice - 1]
                print(f"You have selected: {selected}")
                return selected
            else:
                print("Invalid number, try again.")
        except ValueError:
            print("Please enter a valid number.")

while True:
    user_diet = input("Please enter your diet ('Normal' or 'Vegetarian'): ").strip().capitalize()

    if user_diet == "Normal":
        mains = normal_mains
        sides = normal_sides
    elif user_diet == "Vegetarian":
        mains = vegetarian_mains
        sides = vegetarian_sides
    else:
        print("Please enter a valid diet type.")
        continue

    print("Perfect, let's get you started with your order!")
    print("************************************************")
    time.sleep(1)

    main_choice = choose_item(mains, "Main")
    side_choice = choose_item(sides, "Side")
    drink_choice = choose_item(drinks, "Drink")

    order = [main_choice, side_choice, drink_choice]
    print("-------------------------------")
    print(f"Items: {len(order)}")
    print(f"Order Summary: {', '.join(order)}")
    print("-------------------------------")

    another = input("Would you like to make another order? (yes/no): ").strip().lower()
    if another != "yes":
        print("Thank you for ordering from Chicken Shop Takeaway!.")
        break





