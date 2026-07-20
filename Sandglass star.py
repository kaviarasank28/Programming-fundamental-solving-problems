
n = int(input())
for i in range(1,n+1):
    stars = "* "* (n-i+1)
    spaces = " " * (i-1)
    print(spaces+stars)
    
for i in range(2,n+1):
    spaces = " "* (n-i)
    stars = "* " * (i)
    print(spaces + stars) 