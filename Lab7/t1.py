def compareCountSort(a) :
    n = len(a)
    s = []
    c = []
    for i in range(n):
        c.append(0)
        s.append(0)
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i] > a[j] :
                c[j] += 1
            else :
                c[i] += 1
    for i in range(n):
        s[c[i]] = a[i]
    return s

a = [2,4,1,3,3,5,8]
print(compareCountSort(a))
