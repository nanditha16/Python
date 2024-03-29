import datetime
import random
import statistics

from utility.library import get_positive_number, get_input


# CS50 Intro to Python

def main():
    print("Pick what basics to revise: \n"
          "print Revise: 1\n"
          "calling functions with name, color, age Revise: 2\n"
          "float Revise: 3\n"
          "conditional Revise: 4\n"
          "parity Revise: 5\n"
          "match Revise: 6\n"
          "loop Revise: 7\n"
          "list Revise: 8\n"
          "dictionary Revise: 9\n"
          "list_of_dictionary Revise: 10\n"
          "random Revise: 11\n"
          "statistics Revise: 12\n"
          "array Revise: 13\n"
          "fileIO Revise: 14\n"
          )

    revisetopic = get_input("1/2/3/4/5/6/7/8/9/10/11/12/13/14: ")
    match revisetopic:
        case "1":
            try:
                printsomething()
            except ValueError:
                print("Demo purpose only.")
        case "2":
            callingfunctionsomething()
        case "3":
            floatsomething()
        case "4":
            conditionalsomething()
        case "5":
            paritysomething()
        case "6":
            harrypottersomething()
        case "7":
            loopsomething()
        case "8":
            listsomething()
        case "9":
            dictionarysomething()
        case "10":
            list_of_dictionarysomething()
        case "11":
            randomsomething()
        case "12":
            statisticssomething()
        case "13":
            arraysomething()

def callingfunctionsomething():
    first = getfirstname()
    color = getcolor()
    birth_year = get_input('What is your birth year? ')
    # print(type(birth_year)) Input returns str
    print("Hi " + first + ". Your fav colour is ", color)

    # named parameters:  end , sep sent to print function
    age = getage(birth_year)
    print("You are ", end="")  # override print new line to continue
    print(age)

    print(f"Hello, {first}")
    print("\"Age\"", age, sep=":")

    # Will not work: print("You are "+ age)  # can only concatenate str (not "int") to str
    print('"Just a number!"')


def printsomething():
    try:
        print("Nanditha")  # String
        print("o----")
        print(" ||||")
        price = 10  # integers
        print(price)
        price = 20.4  # float
        print(price)
        is_newpatient = True  # boolean - keywords
        print(is_newpatient)
        print("echo \n" * 2, end="")  # loop the same word
    except Exception:  # Not to be used with broad scope, demo purpose only
        pass


def getfirstname():
    # scan from user:
    # remove whitespace from str and capitalize just 1st letter
    name = get_input('What is your name? ').strip().title()
    if len(name.split(' ')) > 1:
        first, last = name.split(" ")
    else:
        first = name
    return first


def getcolor():
    color = get_input('What is your fav colour? ').strip().capitalize()
    return color


def getage(birth_year):
    """
    - str to int
    - datetime library
    - print function handling str vs int, multiple usage
    """
    today = datetime.date.today()
    print("Today is: ", today)
    year = today.year

    age = year - int(birth_year)
    # print(type(age)) you return int value by taking str
    return age


def floatsomething():
    # round(number[, ndigits])
    floatnum = round(float(get_input("Give me a float number: ")), 4)
    print(f"{floatnum}")
    print(f"{floatnum:.2f}")


def conditionalsomething():
    # conditional [ >, >=, <, <=, ==, != ]
    x = get_input("What's x? ")
    y = get_input("What's y? ")
    score = int(get_input("What's your score to grade? "))

    compare(float(x), float(y))
    isequal(int(x), int(y))
    getgrade(score)


def compare(x, y):
    epsilon = 1e-8  # Define a small tolerance for floating-point equality comparison
    if abs(x - y) < epsilon:
        print("x is equal to y")
    elif x < y:
        print("x is less than y")
    else:
        print("x is greater than y")


def isequal(x, y):
    if x != y:
        print("x is not equal to y")
    else:
        print("x is equal to y")


def getgrade(score):
    if score >= 90:  # same as -  90 <= score and score <= 89: chain
        print("Grade: A")
    elif score >= 80:  # same as - score >= 80 and score <= 89:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 69:  # same as - 60 <= score <= 69:
        print("Grade: D")
    else:
        print("Grade: F")


def paritysomething():
    # parity [ +, -, *, /, % ]
    x = get_input("What's x? ")
    try:
        if is_even(int(x)):
            print("x is even")
        else:
            print("x is odd")
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        exit(1)


def is_even(n):
    """
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False
    :param n:
    :return:
    """
    # return True if n % 2 == 0 else False
    try:
        return n % 2 == 0
    except ValueError:
        pass


def harrypottersomething():
    name = get_input("What character's house do you want to check? ")
    match name:
        case "Harry" | "Ron" | "Hermione":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("who?")


def loopsomething():
    echosomething = get_input("What do you want to echo? : ")
    echotimes = get_positive_number()
    whilesomething(echosomething, echotimes)
    forsomething(echosomething, echotimes)


def whilesomething(echosomething, echotimes):
    while echotimes != 0:
        print("while: ", echosomething)
        echotimes -= 1


def forsomething(echosomething, echotimes):
    # for i in [0, 1, 2]: (list)
    # for i in range(echotimes):
    for _ in range(echotimes):  # _ acts as a variable that is never used
        print("for: ", echosomething)


def listsomething():
    string_list()
    int_list()


def string_list():
    students = ["Harry", "Ron", "Hermione"]
    # print(students[0])
    for student in students:  # no need to initialise
        print(student)


def int_list():
    students = ["Harry", "Ron", "Hermione"]
    for i in range(len(students)):
        print(i + 1, students[i])


def dictionarysomething():
    students_houses = {"Harry": "Gryffindor",
                       "Ron": "Gryffindor",
                       "Hermione": "Gryffindor",
                       "Draco": "Slytherin"}

    print(students_houses)  # to get the key and value from dictionary
    print(students_houses["Harry"])  # to get the value

    for student in students_houses:  # iterate over dictionary, it gives keys
        print(student)

    for student in students_houses:  # iterate over dictionary, it gives keys
        print(student, students_houses[student], sep=": ")  # over dictionary, to get key along with values


def list_of_dictionarysomething():
    hogwarts_students = [
        {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None},
    ]

    for student in hogwarts_students:
        print(student["name"], student["house"], student["patronus"], sep="- ")


def randomsomething():
    print(random.choice(["heads", "tails"]))
    print(random.randint(1, 10))  # random number generation inclusive of both
    # shuffle from a list randomly in place
    cards = ["jack", "queen", "king"]
    print("Before shuffle", cards)
    random.shuffle(cards)
    print("After shuffle", cards)


def statisticssomething():
    print(statistics.mean([100, 90]))


def arraysomething():
    names = []
    # save it in array
    for _ in range(3):
        names.append(get_input("What's your name? "))

    for name in sorted(names):
        print(f"hello, {name}")


"""
   Main function starts from here
"""
if __name__ == "__main__":
    main()
