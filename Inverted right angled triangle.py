
rows = int(input())
for each_number in range(1, rows + 1):
    number = (rows + 1) - each_number
    spaces = "  " * (each_number - 1)
    numbers = (str(number)+ " ") * number 
    print(spaces + numbers)
    