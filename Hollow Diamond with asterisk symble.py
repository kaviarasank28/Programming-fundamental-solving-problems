
n = int(input())
left_spaces_count = n - 1
left_spaces = " " * left_spaces_count
first_row = left_spaces + "*"
print(first_row)

middle_spaces_count = -1
for i in range(2, n + 1):   
    left_spaces_count = n - i
    left_spaces = " " * left_spaces_count

    middle_spaces_count = middle_spaces_count + 2
    middle_spaces = " " * middle_spaces_count

    row = left_spaces + "*" + middle_spaces + "*"
    print(row)

for i in range(1, n - 1):  
    left_spaces_count = i
    left_spaces = " " * left_spaces_count

    middle_spaces_count = middle_spaces_count - 2
    middle_spaces = " " * middle_spaces_count

    row = left_spaces + "*" + middle_spaces + "*"
    print(row)

left_spaces_count = n - 1
left_spaces = " " * left_spaces_count
last_row = left_spaces + "*"
print(last_row)