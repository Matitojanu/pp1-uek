# asks user to input temperature in celsius
celsius = float(input("Enter Celsius temperature: "))
fahrenheit = (celsius * 1.8) + 32
kelvin = (celsius + 273.15)

# printing the result
print(f"The temperature in Fahrenheit is: {fahrenheit} \nand the temperature in Kelvin is: {kelvin}")