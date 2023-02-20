def shiftTable(p):
    m = len(p)
    revp = p[::-1]
    revp = revp[1:]
    dictA = {}
    for i in range(m):
        if revp.find(p[i]) > -1:
            dictA[p[i]] = revp.find(p[i])+1
    return dictA

def horspoolMatching(p,t):
    m = len(p)
    n = len(t)
    table = shiftTable(p)
    i = m
    while i <= n-1 :
        k = 0
        while k <= m-1 and p[m-1-k] == t[i-k]:
            k += 1
        if k == m:
            return i-m+1
        else : 
            if t[i] in table.keys():
                i += table[t[i]]
            else : 
                i += m
    return -1

print(shiftTable("BARBER"))
