import random as rd
import sys

def optimalBST(p):
    kmin = 0
    for i in range(n):
        c[i][i-1] = 0
        c[i][i] = p[i]
        r[i][i] = i
    c[n+1][n] = 0
    for d in range(n-1):
        for i in range(n-d):
            j = i+d
            minval = 999999
            for k in range(i,j):
                if c[i][k-1]+c[k+1][j] < minval:
                    minval = c[i][k-1]+c[k+1][j]
                kmin = k
            r[i][j] = kmin
            sumx = p[i]
            for s in range(i+1,j):
                sumx += p[s]
            c[i][j] = minval + sumx


maxSize = sys.maxsize
minSize = -sys.maxsize - 1
n = int(input("Number of Keys :"))
f = [0]
c = []
r = []

for i in range(n):
    f.append(rd.randint(5,40))
    tempc = [0] * (n+1)
    tempr = [0] * (n+1)
    c.append(tempc)
    r.append(tempr)
sumf = sum(f)
print(f)
f[:] = [x / sumf for x in f]
tempc = [0] * (n+1)
tempr = [0] * (n+1)
c.append(tempc)
r.append(tempr)
tempc = [0] * (n+1)
tempr = [0] * (n+1)
c.append(tempc)
r.append(tempr)
optimalBST(f)
for x in r:
    print(x)