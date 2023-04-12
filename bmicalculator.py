import math
userHeight = int(input("please enter your height: "))
userWeight = int(input("please enter your weigth: "))

cmTometer = userHeight / 100

bmi = userWeight / math.ceil(math.pow(cmTometer,2))
print(bmi)

if 0 < bmi < 18:
    print("low weight")
elif 18 > bmi < 24:
    print("normal weight")
elif 25 < bmi < 29:
    print("Awli weight")
else:
    print("Very fat")
