import random 




# t =1000

# while t >= 1:
#     print(t)
#     t -= 1


x = 10 
while x >= 1:
    if x % 2 == 0 :
        print(x)
    # print(x)
    x -= 1

i = 1
while i<=3 :
    random_number = random.random()
    print("Random number:", random_number)
    if random_number<=0.33:
        print("amir")
    elif 0.33<random_number<=0.66:
        print("mbin")
    i = i+1