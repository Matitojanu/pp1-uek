def f(array2D):
    row = 0
    column = 0

    for n in range(len(array2D)):
            for array in array2D:
                column += array[n]
            for digit in array2D[n]:
                row += digit
            if row != column:
                return False
            column = 0
            row = 0
    return True
        


if __name__ == "__main__":
    #check your program in this place
    print(f([[3,7,2],[4,2,5],[5,2,1]])) 
    print(f([[3,7,2],[4,2,5],[9,2,1]])) 