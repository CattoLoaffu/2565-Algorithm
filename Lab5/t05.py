def a(n,p):
    if n == 1:
        print(p+'[1]')
    elif n == 2:
        p1 = p
        print(p1 + '[1][1]')
        p2 = p
        print(p2 +'[2/1]')
    else :
        a(n-1,p +'[1]')
        a(n-2,p +'[2/1]')

for i in range(1,6):
    a(i,'')
    print("===============================")