def shiftTable(p):
    m = len(p)
    revp = p[::-1]
    revp = revp[1:]
    dictA = {}
    for i in range(m):
        if revp.find(p[i]) > -1:
            dictA[p[i]] = revp.find(p[i])+1
    return dictA

def duplicate_count(text):
    lowerText = text.lower()
    found = []
    for char in lowerText:
        if(not(char in found) and lowerText.count(char) > 1):
            found.append(char)
            
    return len(found)

def boyerMooreMatching(p,t):
    m = len(p)
    n = len(t)
    table = shiftTable(p)
    dup = duplicate_count(p)
    i = m
    while i <= n-1 :
        k = 0
        while k <= m-1 and p[m-1-k] == t[i-k]:
            k += 1
        if k == m:
            return i-m+1
        else : 
            if t[i] in table.keys():
                if table[t[i]] - dup > 0:
                    i += table[t[i]] - dup
                else :
                    i += max(table[t[dup]],1)
            else : 
                i += m-dup
    return -1

print(boyerMooreMatching("TATACA","GCATCGCAGAGAGTATACAGTACG"))