
rows = int(input())

for row in range(1, rows + 1):
    spaces = " " * (rows - row)
    
    if row == 1:
        each_row = spaces + (chr(row + 64 ) + " ") 
    else:
        hollow_spaces = "  " * (row - 2)
        each_row = spaces + (chr(row + 64) + " ") + hollow_spaces + (chr(row + 64) + " ")

    spaces_between_triangles = " " * (rows - row)
    
    print(each_row + spaces_between_triangles + each_row) 