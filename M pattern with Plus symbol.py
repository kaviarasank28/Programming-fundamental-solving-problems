
no_of_rows = int(input())
for each_number in range(1, no_of_rows + 1): 
    first_triangle_stars = "+ "* each_number
    first_triangle_spaces = " " * (no_of_rows - each_number)
    first_triangle = first_triangle_stars + first_triangle_spaces
    second_triangle_spaces = "   " * (no_of_rows - each_number)
    second_triangle_stars = "+ " * each_number 
    second_triangle = second_triangle_spaces + second_triangle_stars
    print(first_triangle+second_triangle)
    