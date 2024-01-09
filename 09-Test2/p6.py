import json

def f(years, course):
    average = 0
    count = 0
    result = 0  

    with open('data.json') as json_file:
        student_details = json.load(json_file)
    for student in student_details:
        studies_details = student["studies"]
        age = student["age"]
        if age >= years:
            courseList = studies_details["courses"]
            for courseInfo in courseList:
                if courseInfo["name"] == course:
                    for grade in courseInfo["grades"]:
                        average += grade
                        count += 1
                    if average/count >= 4:
                        result += 1
                    average = 0
                    count = 0
    return result
                


 
if __name__ == "__main__":
    #check your program in this place
    print(f(21, "statistics"))