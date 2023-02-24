import random as rd

def floyd(a):
    d = a
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d


n = int(input())
a = []
for i in range(n):
    b = [0]*n
    a.append(b)
for i in range(n):
    j = rd.randint(0,n-1)
    while i == j:
        j = rd.randint(0,n-1)
    a[i][j] = 999999
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 0
        elif a[i][j] != 999999:
            a[i][j] = rd.randint(1,9)

for x in a:
    print(x)
print("*******************")
d = floyd(a)
for x in d:
    print(x)
