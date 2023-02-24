# CatLoaf

def lcm(m,n):
    return (m*n)/gcd(m,n)

def gcd(m,n):
    if n == 0:
        return m
    else :
        return gcd(n,m%n)

print(lcm(120,80))