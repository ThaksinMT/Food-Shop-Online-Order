
print("Chicken Shop Takeaway")
print("OXford Street, Westminister")
print("London, W1A 1AA")
print("------------------------")
print("Mon 25 Dec 2025  20:45PM")
print("------------------------")

import time
# Menu For Mains
normal_mains = ["Strip Burger" ,"Fillet Burger" ,"Zinger Burger" ,"Spicy Chicken Wrap"]
vegetarian_mains = ["Vegetable Burger" ,"Salad Wrap" ,"Cheese & Onion Pastry"]
normal_dessert = [""]

# User Choice For Normal Mains
while True:
    user_diet = str(input("Please Enter If Your Diet is 'Normal' or 'Vegetarian': "))
    if user_diet.capitalize() == "Normal":
        print("Perfect, Lets Get You Started With Your Order!")
        time.sleep(1.5)
        print("Here Is A List Of Your Normal Mains: "
              "1- Strip Burger/"
              " 2- Fillet Burger/"
              " 3- Zinger Burger/"
              " 4- Spicy Chicken Wrap")





    elif user_diet.capitalize() == "Vegetarian":
        print("Perfect, Lets Get You Started With Your Order!")
        time.sleep(1.5)
        print("Here Is A List Of Your Vegetarian Mains: "
              "1- Vegetable Burger/"
              " 2- Salad Wrap/"
              " 3- Cheese & Onion Pastry")




