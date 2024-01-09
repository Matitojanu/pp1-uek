import re

def f(arr):
    regex = re.compile('[@!#$%^&*()<>?/\|}{~:].,')
    count = 0

    for username in arr:
        if(regex.search(username) == None):
            count += 1
    return count

if __name__ == "__main__":
    #check your program in this place
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))