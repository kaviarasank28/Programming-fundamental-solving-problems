
n = int(input())
for i in range(1, n+1):
    a = " " * (n -i)
    is_lase = (i == n)
    if is_lase:
        has = "#" * i
        print(a+has)
    else:
        star = "*" * i
        print(a+star)
        