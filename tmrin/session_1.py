first_number = eval(input("عدد اول را وارد کنید: "))
operator = input("عملگر را وارد کنید (+، -، *، /): ")
second_number = eval(input("عدد دوم را وارد کنید: "))

result = None

if operator == "+":
    result = first_number + second_number

elif operator == "-":
    result = first_number - second_number

elif operator == "*":
    result = first_number * second_number

elif operator == "/":
    if second_number == 0:
        print("خطا: تقسیم بر صفر امکان‌پذیر نیست.")
    else:
        result = first_number / second_number

else:
    print("خطا: عملگر واردشده معتبر نیست.")

print("نتیجه:", result)


#  2 tmrin 

weight_kg = float(input("وزن خود را به کیلوگرم وارد کنید: "))
height_cm = float(input("قد خود را به سانتی‌متر وارد کنید: "))

if weight_kg <= 0 or height_cm <= 0:
    print("خطا: وزن و قد باید بیشتر از صفر باشند.")

else:
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)

    print("BMI شما: {bmi}")

    if bmi < 16:
        body_status = "دارای کمبود وزن شدید"

    elif bmi < 18.5:
        body_status = "دارای کمبود وزن"

    elif bmi < 25:
        body_status = "وضعیت مطلوب و نرمال"

    elif bmi < 30:
        body_status = "دارای اضافه وزن"

    elif bmi < 35:
        body_status = "چاقی کلاس ۱"

    elif bmi < 40:
        body_status = "چاقی کلاس ۲"

    else:
        body_status = "چاقی کلاس ۳"

    print("وضعیت بدن:", body_status)



 # tmrin3

valid_password_1 = "Aa@#$"
valid_password_2 = "Ba123"

first_attempt = input("رمز را وارد کنید: ")

if first_attempt == valid_password_1 or first_attempt == valid_password_2:
    print("بمب خنثی شد.")

else:
    second_attempt = input("رمز اشتباه بود، دوباره تلاش کنید: ")

    if second_attempt == valid_password_1 or second_attempt == valid_password_2:
        print("بمب خنثی شد.")
    else:
        print("بمب منفجر شد.")