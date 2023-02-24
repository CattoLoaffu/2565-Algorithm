def a(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else :
        return a(n-1) + (2*a(n-2))

for i in range(1,10):
    print(a(i))