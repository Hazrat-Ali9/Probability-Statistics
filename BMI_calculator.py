# Hazrat Ali
# ID : 221010050




height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
under = height / 100;
bmi = weight / (under * under)

if bmi <= 0:
    print("Wrong Inputs!")

else:
    print(bmi)
    print(round(bmi, 2))
    if bmi <= 16:
        print("You are Over underweight")
    elif bmi <= 18.5:
        print("You are Underweight")
    elif bmi <= 25:
        print("You are Healthy")
    elif bmi <= 30:
        print("You are Overweight")
    else:
        print("You are  Over overweight")
