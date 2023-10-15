'''           Differnce function in set
                    {4,5,7,9}
          Input                      Output
        ---------                   -----------
        9                             4
        1 2 3 4 5 6 7 8 9
        9
        10 1 2 3 11 21 55 6 8                  '''

a=int(input())
s1=set(map(int,input().split()))
b=int(input())
s2=set(map(int,input().split()))
#print(len(s1-s2))
print(len(s1.difference(s2)))
