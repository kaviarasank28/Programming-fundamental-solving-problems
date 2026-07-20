
d = str(input())
n = int(input())
if d == "Sunday":
    day = 0
if d == "Monday":
    day = 1
if  d == "Tuesday": 
    day = 2
if d == "Wednesday":
    day = 3
if d == "Thurday":
    day = 4
if d == "Friday":
    day = 5 
if d == "Saturday":
    day = 6

t_d = day + n - 1
t_d = t_d % 7


if t_d == 0:
    print("Sunday")
elif t_d == 1: 
    print("Monday")
elif t_d == 2:
    print("Tuesday") 
elif t_d == 3:
    print("Wednesday")
elif t_d == 4: 
    print("Thursday")
elif t_d == 5:
    print("Friday")
else:
    print("Saturday")
