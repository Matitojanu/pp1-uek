def f(arr):
    num1 = 0
    num2 = 0
    occured = False

    for n in range(len(arr)):
        num1 = arr[0]
        if n < len(arr):
            if arr [n] != arr[n+1]:
                if occured:
                    return num2
                num2 = arr[n+1]
                occured = True

    return num1
        

if __name__ == "__main__":
    #check your program in this place
    print(f([7,7,7,7,7,5,7,7]))