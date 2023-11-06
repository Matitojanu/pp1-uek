fatherIncome = float(input("Enter father’s income:"))
motherIncome = float(input("Enter mother’s income:"))
familySize = int(input("Enter number of people in family:"))
total = fatherIncome+motherIncome
incomePerPerson = total/familySize
print(f"Total income: {total}") 
print(f"Income per person: {incomePerPerson}")
