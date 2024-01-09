def f(subjects):
    highestAverage = 0
    bestSubject = ''

    for key in subjects:
        count = 0
        sumOfNumbers = 0
        for grade in subjects[key]:
            count +=1
            sumOfNumbers += grade
        average = sumOfNumbers/count
        if average > highestAverage:
            highestAverage = average
            bestSubject = key
    return bestSubject



if __name__ == "__main__":
    #check your program in this place
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))  