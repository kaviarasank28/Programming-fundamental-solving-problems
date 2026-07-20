
N = int(input())
for i in range(N):
    
    for j in range(N-i-1):
        print(" ", end="")
    if i==0:                       # for the first row 
        print("/\\")
    else:                          # for remaining rows
        for j in range(2*i+1):
            if j == 0:
                print("/", end=" ")   # end with space here
            elif j == 2*i:
                print("\\", end="")
            else:
                print(" ", end="")
        print()   # add a new line after each row
        
for i in range(N-1, -1, -1):   # reverse loop to print bottom half
    
    for j in range(N-i-1): 
        print(" ", end="")
    if i==0:                       # for the last row 
        print("\\/")
    else:                          # for remaining rows
        for j in range(2*i+1):
            if j == 0:
                print("\\", end=" ")   # end with space here
            elif j == 2*i:
                print("/", end="")
            else:
                print(" ", end="")
        print()   # add a new line after each row