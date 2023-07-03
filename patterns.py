def main():
    height = get_positive_number()
    print("column_pattern: ")
    column_pattern(height)
    print("row_pattern:")
    row_pattern(height)
    print("grid_pattern: ")
    grid_pattern(height)
    print("right_triangle_pattern: ")
    right_triangle_pattern(height)
    print("right_reverse_triangle_pattern: ")
    right_reverse_triangle_pattern(height)


def column_pattern(height):
    print("#\n" * height, end="")


def row_pattern(width):
    print("#" * width, end="")
    print()


def grid_pattern(size):
    # for each row in square
    for i in range(size):
        # print brick in row
        row_pattern(size)


def right_triangle_pattern(size):
    # for each row in square
    for i in range(size):
        row_pattern(size - i)


def right_reverse_triangle_pattern(size):
    # for each row in square
    for i in range(size):
        row_pattern(i + 1)


def get_positive_number():
    while True:
        try:
            number = int(input("Please enter a non-negative integer : "))
            if number <= 0:
                print("Please enter a non-negative integer for number.")
            else:
                # break
                return number  # same as break and then return
        except ValueError:
            print("Invalid input. Please enter a valid integer for number.")
    # return number


"""
   Main function starts from here
"""
main()
