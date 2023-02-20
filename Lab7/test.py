def shiftTable(p):
    m = len(p)
    revp = p[::-1]
    revp = revp[1:]
    dictA = {}
    for i in range(m):
        if revp.find(p[i]) > -1:
            dictA[p[i]] = revp.find(p[i])+1
    return dictA

def BoyerMoore(p,t):
    n = len(p)
    bc = shiftTable(p)
    i =  n - 1
    ans = []
    
    while i <= len(t) -1 :
        j = 0
        while j < n and p[n-j-1] == t[i-j]:
            j+=1
        if j == n :
            ans.append(i - n + 1)
            i += 1
        else :
            shift = bc.get(t[i+j],n)
            if shift == 0 :
                shift = n -1
            skips = shift - j 
            i== skips
    return ans

print(BoyerMoore("HELLO","IFOHIHAHELLOOHFAUIOH"))