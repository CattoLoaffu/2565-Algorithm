import random as rd

def sh(g):
    for x in g:
        print(x)

def randomAdjacency(n):
    g =  []
    for i in range(n):
        lineg = [100000]*n
        g.append(lineg)
    for i in range(0,n):
        g[i][i] = 0
        for j in range(i+1,n,2):
            x = rd.randint(1,6)
            g[i][j] = x
            g[j][i] = x
    return g

def findmin(E):
    minx =  1000000
    minkey = '-'
    for x in E.keys():
        if E[x][1] < minx:
            minx = E[x][1]
            minkey = x
    return minkey

def prim(g):
    n = len(g)
    Te = []
    Vt = []
    Et = {}
    Rv = list(range(n))
    Vt.append(Rv.pop(0))
    Te.append([Vt[0],'-',0])
    for i in range(1,n):
        curv = Vt[len(Vt)-1]
        for j in range(i,n):
            if Rv[j-i] in Et.keys():
                tempx = Et[Rv[j-i]]
                if g[curv][Rv[j-i]] < tempx[1]:
                    Et[Rv[j-i]] = [curv, g[curv][Rv[j-i]]]
            else:
                Et[Rv[j-i]] = [curv,g[curv][Rv[j-i]]]
        minkey = findmin(Et)
        tempx = Et.pop(minkey)
        Vt.append(Rv.pop(Rv.index(minkey)))
        Te.append([minkey,tempx[0],tempx[1]])
    return Te

n = int(input("Enter node : "))
g = randomAdjacency(n)
sh(g)
print(prim(g))