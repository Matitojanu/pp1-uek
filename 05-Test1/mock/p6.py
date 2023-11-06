def f(number, even):
    sum = 0
    if even == True:
        for i in str(number):
            if int(i) % 2 == 0:
                sum += int(i)
    else:
        for i in str(number):
            if int(i) % 2 != 0:
                sum += int(i)
    return sum
if __name__ == "__main__":
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))
