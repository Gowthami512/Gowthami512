''' 
Input format:
---------------

The first line contains any 2 positive numbers separated by space.

Output format:
---------------

Print the HCF of given two numbers.

Sample Input:

70 15

Sample Output:

5'''
a,b=map(int,input().split())
m=min(a,b)
l=[]
for i in range(1,m):
    if(a%i==0 and b%i==0):
        l.append(i)
print(l[len(l)-1])        
