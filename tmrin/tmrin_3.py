user = input("Choose food or drink: ")

if user == "food":
    print("Food menu:")
    print("kebab = 5")
    print("chicken = 2")
    print("stew = 6")

    food = input("Choose your food: ")
    number = int(input("How many people are you? "))
    if food == "kebab":
        if number <= 5:
            print("Your kebab order is available.")
            print("Your order will be ready in 15 minutes.")
   
        elif food == "chicken":
            if number <= 2:
                print("Your chicken order is available.")
                print("Your order will be ready in 10 minutes.")
            else:
                print("There is not enough chicken.")
                print("The waiter kicked you out of the restaurant!")

        elif food == "stew":
            if number <= 6:
                print("Your stew order is available.")
                print("Your order will be ready in 20 minutes.")
            else:
                print("There is not enough stew.")
                print("The waiter kicked you out of the restaurant!")

elif user == "drink":
    print("Drink menu:")
    print("orange = 3")
    print("carrot = 2")
    print("pineapple = 4")

    drink = input("Choose your drink: ")
    number = int(input("How many people are you? "))
    if drink == "orange":
        if number <= 3:
            print("Your orange juice order is available.")
            print("Your order will be ready in 5 minutes.")
        else:
            print("There is not enough orange juice.")
            print("The waiter kicked you out of the restaurant!")

    elif drink == "carrot":
        if number <= 2:
            print("Your carrot juice order is available.")
            print("Your order will be ready in 5 minutes.")
        else:
            print("There is not enough carrot juice.")
            print("The waiter kicked you out of the restaurant!")

    elif drink == "pineapple":
        if number <= 4:
            print("Your pineapple juice order is available.")
            print("Your order will be ready in 5 minutes.")
        else:
            print("There is not enough pineapple juice.")
            print("The waiter kicked you out of the restaurant!")

else:
    print("Invalid selection. Please choose either 'food' or 'drink'.")