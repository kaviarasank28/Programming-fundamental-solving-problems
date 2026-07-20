
string = input()

length = len(string)
result_string = string[0]

for each_number in range(1, length):
    each_character = string[each_number]
    upper_case = each_character.upper()
    lower_case = each_character.lower()

    if each_character == upper_case:
        result_string = result_string + "-" + lower_case
    else:
        result_string = result_string + each_character

print(result_string) 