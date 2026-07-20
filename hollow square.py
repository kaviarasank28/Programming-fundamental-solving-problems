
number = int(input())
print("* " * number)
for i in range(1, number - 1):
    middle_spaces = "  " * (number - 2)
    row = "* " + middle_spaces + "*"
    print(row)
print("* " * number)
