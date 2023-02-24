def a(n) :
    if n == 0 :
        return 5
    else :
        return a(n-1)*2

print(a(3))

# 5,10,20,40,...