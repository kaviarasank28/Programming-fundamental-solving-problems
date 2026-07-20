m ,n= int(input())
count = 0
number_divisble_6 = ""
for i in range(m, n+1):
    if i % 6 == 0:
        count += 1
        number_divisble_6 += str(i) + " "
if count == 0:
    print("No Numbers Found")
else:
    print(number_divisble_6)