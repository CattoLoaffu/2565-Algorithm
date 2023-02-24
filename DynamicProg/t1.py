import random as rd

n = int(input("number of asset(s) :"))
w = int(input("Max load :"))

weight = [0]
Values = [0]
F = []
tempx = [0] *(w+1)
F.append(tempx)
for i in range(n) :
    weight.append(rd.randint(1,5))
    Values.append(rd.randint(10,40))
    tempx = [-1]*w
    tempx.insert(0,0)
    F.append(tempx)

print(weight,Values,F)
def MFknapsack(i,j):
    if F[i][j] < 0:
        if j < weight[i]:
            value = MFknapsack(i-1,j)
        else :
            value = max(MFknapsack(i-1,j),Values[i]+MFknapsack(i-1,j-weight[i]))
        F[i][j] = value
    return F[i][j]

print(MFknapsack(n,w))