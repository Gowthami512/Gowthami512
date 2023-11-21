# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
k,n=map(str,input().split())
n=int(n)
k=list(k)
k.sort()
for i in k:
    print(i)
'''for i in range(len(k)):
    for j in range(i+1,len(k)):
        print(k[i]+k[j]) '''
k1="".join(k)
print(list(combinations(k1,3)))
for i in range(2,n):
    k2=list(combinations(k1,i))
    for j in k2:
        l=list(j)
        print("".join(l))




