import os
import sys
import csv

from PIL import Image

from utility.library import get_input, validate_list_of_file_from_directory


def main():
    print("Pick what basics to revise: \n"
          "fileIO write Revise: 1\n"
          "fileIO read Revise: 2\n"
          "fileIO read collect to manipulate Revise: 3\n"
          "fileIO write to specific path Revise: 4\n"
          "fileIO read csv_list Revise: 5\n"
          "fileIO read csv_dictionary Revise: 6\n"
          "fileIO read csv_list_of_dictionary Revise: 7\n"
          "fileIO read csv_package Revise: 8\n"
          "fileIO read binary file(images) Revise: 9\n"
          )

    revise_topic = get_input("1/2/3/4/5/6/7/8/9: ")
    match revise_topic:
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
            filename = get_input("What csv file are you manipulating?: ")
            fileio_hogwarts_list_manipulate_something(filename)
        case "6":
            # file should be available in current path
            filename = get_input("What csv file are you manipulating?: ")
            fileio_hogwarts_dictionary_manipulate_something(filename)
        case "7":
            # file should be available in current path
            filename = get_input("What csv file are you manipulating?: ")
            fileio_hogwarts_list_of_dictionary_manipulate_something(filename)
        case "8":
            # file should be available in current path
            filename = get_input("What csv file are you manipulating?: ")
            fileio_hogwarts_csv_manipulate_something(filename)
        case "9":
            directory = input("What is the full path where the images should be placed? ")
            try:
                image_count = int(input("How many images are you sending? "))
            except ValueError:
                print("Error: Invalid image count.")
                exit(1)

            images = []
            while image_count != 0:
                image = input("What is the image file name? ")
                images.append(image)
                image_count -= 1

            fileio_image_gif_something(images, directory)


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
    try:
        with open(filename) as file:  # hogwarts.csv
            for line in file:
                try:
                    name, house = line.rstrip().split(",")  # py thing - dic
                    print(f"{name.title()} is in {house}")
                except ValueError:
                    print("Error: Invalid format in line. Skipping line. too many ',' seperated")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Permission denied. Unable to read the file.")
    except IOError:
        print(f"An error occurred while reading the file.")


def fileio_hogwarts_list_of_dictionary_manipulate_something(filename):
    students = []  # hogwarts.csv
    try:
        with open(filename) as file:
            for line in file:
                try:
                    name, house = line.rstrip().split(",")  # py thing - dic
                    print(f"{name.title()} is in {house}")
                except ValueError:
                    print("Error: Invalid format in line. Skipping line. too many ',' seperated")
                else:
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
        print("sort by house in reverse order ".title())
        # py thing - allows to pass functions as arguments into another function
        # using lambda anonymous function
        for student_data in sorted(students, key=lambda s: s['house'], reverse=True):
            # note the single quote and double quote usage
            print(f"{student_data['name']} is in {student_data['house']}")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Permission denied. Unable to read the file.")
    except IOError:
        print(f"An error occurred while reading the file.")


def fileio_hogwarts_csv_manipulate_something(filename):
    # hogwarts.csv
    option = get_input("do you want to read or write? ")
    if option == "read":
        fileio_hogwarts_csv_dict_reader_something(filename)
    elif option == "write":
        fileio_hogwarts_csv_writer_something(filename)
    else:
        print("Error: you can only read or write.")


def fileio_hogwarts_csv_writer_something(filename):
    try:
        name = get_input("Whats is your name? ")
        house = get_input("whats is your house? ")

        # Validate name and house inputs
        if not name or not house:
            print("Error: Name and house cannot be empty.")
            return

        with open(filename, "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "house"])
            # Check if the file is empty

            file.seek(0, os.SEEK_END)
            if file.tell():  # if current position is true (i.e != 0)
                file.seek(0)  # rewind the file for later use
                print("file is not empty.")
            else:
                print("file is empty. Header is added")
                file.write("Name,house\n")

            writer.writerow({"name": name, "house": house})
        print("Data has been written successfully.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Permission denied. Unable to write to the file.")
    except IOError:
        print(f"An error occurred while writing to the file.")


def fileio_hogwarts_csv_dict_reader_something(filename):
    students = []  # hogwarts.csv
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            # read csv file by header names and same
            if "Name" not in reader.fieldnames or "House" not in reader.fieldnames:
                print("Error: CSV file does not contain required headers 'Name' and 'House'.")
                return

            for row in reader:
                name = row["Name"]  # type: ignore
                house = row["House"]  # type: ignore
                if name and house:
                    students.append({"name": name, "house": house})

        print("Sort by house".title())

        sorted_students = sorted(students, key=lambda student: student["house"])
        for student_info in sorted_students:
            print(f"{student_info['name']} is in {student_info['house']}")

    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Permission denied. Unable to read the file.")
    except IOError:
        print(f"An error occurred while reading the file.")


def fileio_image_gif_something(images, directory):
    if validate_list_of_file_from_directory(directory, images):
        # Perform further processing or saving of the images
        test_images = []
        for image in images:
            # Process or save each image in the specified directory
            image_path = os.path.join(directory, image)
            print(f"Processing image: {image_path}")
            image_info = Image.open(image_path)
            test_images.append(image_info)

        test_images[0].save(
            os.path.join(directory, "Road1.gif", ), save_all=True, append_images=[test_images[1]], duration=200, loop=0
        )


def get_name(student):
    return student["name"]


"""
   Main function starts from here
"""
if __name__ == "__main__":
    main()
