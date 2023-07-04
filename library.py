def main():
    get_positive_number()
    print(get_input("yes or no? : "))


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


if __name__ == "__main__":
    main()
