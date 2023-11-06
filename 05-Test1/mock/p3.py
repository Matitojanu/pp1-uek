def f(name):
    acronym = ""
    for i in range(len(name)):
        if i == 0:
            acronym += name[i]
        if name[i] == " ":
            acronym += name[i+1]
    return acronym
if __name__ == "__main__":
    #check your program in this place
    print(f("Internet of Things"))
    print(f("For Your Information"))
    print(f("Python"))
