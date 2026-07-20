temperature = input()
unit = temperature[-1]
value = float(temperature[:-1])

if unit == "C":
    celsius = value
elif unit == "F":
    celsius = (value - 32) * 5 / 9
else:
    celsius = value - 273

print(str(round(celsius,2)) + "C")
print(str(round((celsius*9/5)+32,2)) + "F")
print(str(round(celsius+273,2)) + "K")