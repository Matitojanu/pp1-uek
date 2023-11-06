def f(card_number):
    censoredNumber = ""
    for i in range(len(card_number)):
        if i <= 1:
            censoredNumber += card_number[i]
        elif (i<=11) and (i>1):
            censoredNumber += '*'
        else:
            censoredNumber += card_number[i]
    return censoredNumber
if __name__ == "__main__":
    print(f("5290312400019022"))