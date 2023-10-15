'''                Intersection 
                 set count value
  input                          output
---------                      ----------
9                                  5
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8'''

n=int(input())
set1=set(map(int,input().split()))
b=int(input())
set2=set(map(int,input().split()))
print(len(set1.intersection(set2)))
