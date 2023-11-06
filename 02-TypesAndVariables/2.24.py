registration = input("Enter vehicle registration number: ")
isKrakow = False
if (registration[0] == 'K') and (registration[1] == 'K'or'R'):
    isKrakow = True
print(f"Car from Kraków: {isKrakow}")