num_rows = int(input())
print("* " * (2 * num_rows - 1))
for i in range(1, num_rows):
    left_spaces = " " * (i)
    stars = "* " * (num_rows - i)
    middle_spaces = "  " * (i - 1)           
    print(left_spaces + stars + middle_spaces + stars)

last_row_left_space = ' '*(num_rows-1)
last_row_right_space = ' '*(num_rows-2)
print(last_row_left_space+last_row_right_space)
 