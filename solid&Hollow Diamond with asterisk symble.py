
n = int(input())


k = 2*n-5

 
for i in range (1,n+1):
    spaces = " "
    stars = "* "
    print(spaces * (n-i) + stars * i)
for j in range(1,n-1):
    spaces = " "
    stars = "* "
    print(" " * j + "*" + " " * k + "*")
    k = k-2
print(" " * (n-1) + "*")