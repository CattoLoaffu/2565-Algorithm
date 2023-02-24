# CatLoaf
a = [2,3,6,10,12,9]

def peu(a) :
    a.sort()
    for i in range(len(a)-1) :
        if a[i] == a[i+1]:
            return False
    
    return True

print(peu(a))