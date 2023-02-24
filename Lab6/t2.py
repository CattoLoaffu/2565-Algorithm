# CatLoaf

def presortMode(a):
    a.sort()
    n = len(a)
    i = 0
    mf = 0
    while i <= n-1:
        runl = 1
        runval = a[i]
        while i+runl <= n-1 and a[i+runl] == runval:
            runl += 1
        if runl > mf :
            mf = runl
            mValue = runval
        i += runl
    
    return mValue

a = [2,3,4,4,3,3,2]
print(presortMode(a))