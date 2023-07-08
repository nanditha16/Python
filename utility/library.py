import os


def main():
    get_positive_number()
    print(get_input("quit yes or no? : "))


def get_positive_number():
    while True:
        try:
            number = int(input("Please enter a non-negative integer : "))
        except ValueError:
            print("Invalid input. Please enter a valid integer for number.")
        else:
            if number <= 0:
                print("Please enter a non-negative integer for number.")
            else:
                # break
                return number  # same as break and then return
    # return number


def get_input(prompt):
    while True:
        try:
            return input(prompt)
        except ValueError:
            print("Invalid input...")


def validate_list_of_file_from_directory(directory, list_of_files):
    try:
        # Validate directory input
        if not os.path.isdir(directory):
            print("Error: Invalid directory path.")
            return False

        # Validate list of files count
        if not isinstance(list_of_files, list) or len(list_of_files) == 0:
            print("Error: Invalid list of image names.")
            return False

        return True
    except IOError:
        print("An error occurred while Error reading from a directory.")
    except ValueError:
        print("Error: Invalid list of file count.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
