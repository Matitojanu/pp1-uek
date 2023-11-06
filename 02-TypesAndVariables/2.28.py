height = float(input("Enter your height in cm: "))/100
weight = int(input("Enter your weight in kg: "))
correct = False

BMI = weight/round(height*height, 2)
print(f"Your BMI index: {BMI}")

if (BMI > 18.5) and (BMI < 24.9):
    correct = True

print(f"Correct weight: {correct}")