
number_of_rows = int(input())

for row in range(number_of_rows):
    spaces = "  " * (number_of_rows - row - 1)
    stars = (str(row + 1) + " ") * ((2 * row) + 1)
    each_row = spaces + stars
    print(each_row) 