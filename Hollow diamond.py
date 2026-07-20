
n = eval(input())
alph = 65 
for i in range(n):
    left_spaces = " " * (n-i-1)
    hollow_spaces = " " * (2*i-1)
    if i == 0:
        each_row = left_spaces + chr(alph)
        alph += 1
    else:
        each_row = left_spaces + chr(alph) + hollow_spaces + chr(alph)
        alph += 1
    print(each_row)
    
alph -= 2
for j in range(1,n): 
    left_spaces = " " * j
    hollow_spaces = " " * (2*(n-j-1)-1)
    if j == n-1:
        each_row = left_spaces + chr(alph)
    else:
        each_row = left_spaces + chr(alph) + hollow_spaces + chr(alph)
        alph -= 1
    print (each_row)