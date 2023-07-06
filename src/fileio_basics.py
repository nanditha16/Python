import os
import sys

from utility.library import get_input


def main():
    print("Pick what basics to revise: \n"
          "fileIO write Revise: 1\n"
          "fileIO read Revise: 2\n"
          "fileIO read collect to manipulate Revise: 3\n"
          "fileIO write to specific path Revise: 4\n"
          "fileIO read csv_list Revise: 5\n"
          "fileIO read csv_dictionary Revise: 6\n"
          "fileIO read csv_list_of_dictionary Revise: 7\n"
          )

    revisetopic = get_input("1/2/3/4/5/6/7: ")
    match revisetopic:
        case "1":
            # file will be available in current path
            filename = get_input("What should the filename be?: ")
            fileio_write_something(filename)
        case "2":
            # file should be available in current path
            filename = get_input("What file are you reading?: ")
            fileio_read_something(filename)
        case "3":
            directory = get_input("What is full path where file is placed?: ")
            filename = get_input("What is the filename?: ")
            fileio_read_to_list_manipulate_something(directory, filename)
        case "4":
            directory = get_input("What is full path where file to be placed?: ")
            filename = get_input("What should the filename be?: ")
            data = get_input("What do you want to write?: ")
            fileio_write_to_path_something(directory, filename, data)
        case "5":
            # file should be available in current path
            filename = get_input("What csv file are you reading?: ")
            fileio_hogwarts_list_manipulate_something(filename)
        case "6":
            # file should be available in current path
            filename = get_input("What csv file are you reading?: ")
            fileio_hogwarts_dictionary_manipulate_something(filename)
        case "7":
            # file should be available in current path
            filename = get_input("What csv file are you reading?: ")
            fileio_hogwarts_list_of_dictionary_manipulate_something(filename)


def fileio_write_something(filename):
    name = get_input("What do you want to write? ")
    # save it in a file and close after writing
    try:
        with open(filename, "a") as file:
            file.write(f"{name.title()}\n")
    except IOError:
        print("An error occurred while writing to the file.")


def fileio_read_something(filename):
    try:
        with open(filename) as file:
            for line in sorted(file.readlines()):
                print("Hello", line.rstrip())
    except FileNotFoundError:
        print("The file 'names.txt' does not exist.")
    except PermissionError:
        print("Permission denied. Unable to read the file.")
    except IOError:
        print("An error occurred while reading the file.")


def fileio_read_to_list_manipulate_something(directory, filename):
    # file written in abspath
    if os.path.isdir(directory):
        filepath = os.path.join(directory, filename)
        try:
            names = []
            with open(filepath) as file:
                for line in file:
                    names.append(line.rstrip())  # list
        except IOError:
            print("Error reading the file.")
            return
    else:
        print('no such directory. '
              '# Usage example: directory = "path/to/directory"; filename = "example.txt"')
        sys.exit(1)

    # to sort or manipulate the collected data
    for name in sorted(names, reverse=True):
        print(f"Hello, {name}")


def fileio_write_to_path_something(directory, filename, data):
    if os.path.isdir(directory):
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, "a") as file:
                file.write(f"{data.title()}\n")
        except IOError:
            print("Error writing to the file.")
    else:
        print('no such directory. '
              '# Usage example: directory = "path/to/directory"; filename = "example.txt"; data = "example data"')


def fileio_hogwarts_list_manipulate_something(filename):
    with open(filename) as file:  # hogwarts.csv
        for line in file:
            row = line.rstrip().split(",")  # list
            print(f"{row[0]} is in {row[1]}")


def fileio_hogwarts_dictionary_manipulate_something(filename):
    with open(filename) as file:  # hogwarts.csv
        for line in file:
            name, house = line.rstrip().split(",")  # py thing - dic
            print(f"{name.title()} is in {house}")


def fileio_hogwarts_list_of_dictionary_manipulate_something(filename):
    students = []  # hogwarts.csv
    with open(filename) as file:
        for line in file:
            name, house = line.rstrip().split(",")
            student = {"name": name, "house": house}  # store temporarily in a dic , notice colon
            students.append(student)  # list of dictionary

    # listed dictionary
    print()
    print("reverse sort by name".title())
    # py thing - allows to pass functions as arguments into another function
    # pass teh function name, so sorted function can call
    for student in sorted(students, key=get_name, reverse=True):
        print(f"{student['name']} is in {student['house']}")  # note the single quote and double quote usage
    print()
    print("sort by house".title())
    # py thing - allows to pass functions as arguments into another function
    # using lambda anonymous function
    for student in sorted(students, key=lambda student: student["house"], reverse=True):
        print(f"{student['name']} is in {student['house']}")  # note the single quote and double quote usage


def get_name(student):
    return student["name"]


"""
   Main function starts from here
"""
if __name__ == "__main__":
    main()
