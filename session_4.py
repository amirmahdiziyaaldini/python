import random


number = random.randint(1,20)

x = 1
while x <= 3 :
    user = int(input("Number"))
    if user == number:
        print("a")
    # elif user < number:
    #     print("b")
    #     break
    elif user > number and x < 3:
        print("c")
    else:
        print("d")
        if x < 3:
         print("66")
    x = x + 1
