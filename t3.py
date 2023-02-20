import random as rd

def warshall(a):
    r = [i[:] for i in a]
    n = len(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                r[i][j] = r[i][j] or (r[i][k] and r[k][j])
    return r



n = int(input())
a = []
for i in range(n):
    b = [0]*n
    a.append(b)
for i in range(n):
    j = rd.randint(0,n-1)
    while i == j:
        j = rd.randint(0,n-1)
    a[i][j] = 1

for x in a:
    print(x)
print("*************************")
r = warshall(a)
for x in r :
    print(x)