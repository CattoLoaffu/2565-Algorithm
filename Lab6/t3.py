# CatLoaf

def forwardEliminate(a,b):
    n = len(a)
    for i in range(n) :
        a[i].append(b[i])
    for i in range(n-1):
        for j in range(i+1,n):
            temp = a[j][i]
            for k in range(i,n+1):
                a[j][k] = a[j][k]-a[i][k]*temp/a[i][i]
    return a

def backwardSub(a):
    n = len(a)
    x=[0]*(n)
    for i in range(n-1,-1,-1):
        s = a[i][n]
        for j in range(i+1,n):
            s = s - a[i][j]* x[j]
        x[i] = s / a[i][i]
    return x


a = [[2,-1,1,],[4,1,-1],[1,1,1]]
b = [1,5,0]

c = forwardEliminate(a,b)
print(backwardSub(c))
