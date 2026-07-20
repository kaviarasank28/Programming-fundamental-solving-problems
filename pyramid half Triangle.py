
number = int(input())
for each_number in range(number):
    star = "* " * (each_number +1)
    print(star)
for each_number in range(number):
    star = "* " * (number-each_number-1)
    print(star)
    