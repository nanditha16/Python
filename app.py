import datetime

# CS50 Intro to Python s
print("Nanditha") # String
print("o----")
print(" ||||")
price=10 # integers
print(price)
price=20.4 # float
print(price)
is_newPatient = True #boolean - key words
print(is_newPatient)

# scan from user:
# remove whitespace from str and capitalize just 1st letter
name = input('What is your name? ').strip().title()
first,last = name.split(" ")

color = input('What is your fav colour? ').strip().capitalize()
print("Hi " + first + ". Your fav colour is :", color)

#
"""
- str to int
- datetime library 
- print function handling str vs int, multiple usage
"""
today = datetime.date.today()
print(today)
year = today.year

birth_year = input('What is your birth year? ')
print(type(birth_year))

age = year - int(birth_year)
print(type(age))
# Will not work: print("You are "+ age)  # can only concatenate str (not "int") to str
# named parameters:  end , sep sent to print function
print("You are ", end="") # override print new line to continue
print(age)
print(f"hello, {first}")
print("\"age\"", age, sep=":")
print('"Just a number!"')

"""
- datatype :int 
- Arithmetic  (+-*/%)
- interactive mode 
""" 

