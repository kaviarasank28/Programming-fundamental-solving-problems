
n = int(input())
last = "  " * (n-1)
for i in range(2*n-1):
    if i == 0 or i == n-1 or i == (2* n-2):
        each_row = "* " * n
    
    else:
        each_row = last + "*"
    print(each_row)