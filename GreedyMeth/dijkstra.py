import random as rd

def sh(g):
    for x in g:
        print(x)

def randomAdjacency(n):
    g =  []
    for i in range(n):
        lineg = [0]*n
        g.append(lineg)
    for i in range(0,n):
        g[i][i] = 0
        for j in range(i+1,n,2):
            x = rd.randint(1,6)
            g[i][j] = x
            g[j][i] = x
    return g

def dijkstra(a):
    n = len(a)
    mb = 1000000
    aa = list(range(n))
    for i in range(n):
        aa[i] = 0
    bb = [[0,0,0]]
    cc = [[0,0,0,1]]
    for i in range(1,n-1):
        aa[i] = i
        cc.append([i,-1,mb,0])
    startN = aa.pop()
    j = 0
    m = 0
    while len(aa) > 0 and m < 10:
        i = bb[startN][0]
        for j in range(len(cc)):
            if cc[j][3] != 1:
                xlen = a[cc[j][0]][i]
                if (xlen == 0):
                    xlen = mb
                else :
                    xlen += bb[startN][2]
                if xlen < cc[j][2]:
                    cc[j][1] = i
                    cc[j][2] = xlen
        minx = mb
        posj = -1
        for j in range(len(cc)):
            if cc[j][3]!= 1:
                if cc[j][2] < minx:
                    minx = cc[j][2]
                    posj = j
        bb.append([cc[posj][0],cc[posj][1],cc[posj][2]])
        cc[posj][3] = 1
        startN += 1
        aa.pop()
    return bb

n = int(input("Enter node : "))
g = randomAdjacency(n)
sh(g)
print(dijkstra(g))

