
n = int(input())
print("* ")
for i in range(1, n - 1):
    middle_spaces = " " * (2 * (i - 1))
    row = "* " + middle_spaces + "* "
    print(row)

print("* " * n)