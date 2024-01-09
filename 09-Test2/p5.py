import re

def f(first_letter, last_letter):
    with open('data.txt', encoding="utf8") as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        occurences = re.findall(r"\b"+first_letter+r"\w*?"+last_letter+r"\b", content)
        result = len(occurences)
    return result

if __name__ == "__main__":
    #check your program in this place
    print(f("w","d"))