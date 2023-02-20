"""
def destributionCountSort(a,l,u):
    n = len(a)
    d = [0] * (u-l+1)
    s = [0] * n
    for i in range(n):
        d[a[i] - l] += 1
    for j in range(1,u-l+1):
        d[j] = d[j-1] + d[j]
    for i in range(n-1,-1,-1):
        j = a[i]-l
        s[d[j] -1] = a[i]
        d[j] -= 1
    return s
"""

def destributionCountSort(a,l,u):
    n = len(a)
    l = ord(l)
    u = ord(u)
    d = [0] * (u-l+1)
    s = [0] * n
    b = []
    for i in range(n):
        b.append(ord(a[i]))
    for i in range(n):
        d[b[i] - l] += 1
    for j in range(1,u-l+1):
        d[j] = d[j-1] + d[j]
    for i in range(n-1,-1,-1):
        j = b[i]-l
        s[d[j] -1] = b[i]
        d[j] -= 1
    ss = ''
    for i in range(len(s)):
        ss += chr(s[i])
    return ss

a = 'abcabcabc'

print(destributionCountSort(a,'a','c'))