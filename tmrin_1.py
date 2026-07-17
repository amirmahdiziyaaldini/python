# User_1 = input("Enter your name: ")
# User_2 = input("Enter your name: ")
# password_user = eval (input("Enter your password: "))
# password_user_2 = eval (input("Enter your password: "))

# mobale_number_user = '09912345678'
# mobale_number_user_2 = '09912345678'

# if User_1 == 'amir' and password_user == mobale_number_user:
#     print("Welcome", User_1)
# elif User_2 == 'mahdi' and password_user_2 == mobale_number_user_2:
#     print("Welcome", User_2)
# else:
#     print("Invalid credentials")


gender = eval(input("Enter your gender: "))
age = eval(input("Enter your age: "))
# روش اول
if gender == 1 and 10 <= age <= 20:
    print("You are boy")
elif gender == 2 and 10 <= age <=20 :
    print("You are girl")
else:
    print("Invalid input")

# دوم

if gender == 1 :
    if age < 15:
        print("You are a young boy")
    else:
        print("You are a teenage boy")
elif gender == 2:
    if age < 15:
        print("You are a young girl")
    else:
        print("You are a teenage girl")
else:
    print("Invalid input")
