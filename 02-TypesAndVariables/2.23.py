from math import sqrt


a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))

p = float((a+b+c)/2)
area = float(sqrt(p(p-a)(p-b)(p-c)))

print(f"Triangle area: {area} \nTriangle circumference: {a+b+c}")