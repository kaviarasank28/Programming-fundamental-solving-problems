
n = int(input())
for each in range(1,n+1):
    stars = "+ " * each
    spaces = "  " * (2 *(n-each))
    each_row = stars+ spaces + stars 
    print(each_row )
    
for each in range(1, n):
    stars ="+ " * (n-each)
    spaces = "  " * (2 * each)
    each_row = stars + spaces + stars
    print(each_row )
    