'''                                       HACKERRANK PROBLEMS

                   i nput                                                  output
             -------------                              ------------
                  ABCDCCDC                                              2
                   CDC       '''
string=input()
findstr=input()
count=0
l=len(findstr)
n=l
''' To avoid string index out of range'''
outofrange=len(string)-len(findstr)
''' odd or even'''
if(len(string)%2==0):
    limit=2
else:
     limit=1

for i in range(len(string)-limit):
      s=string[i]                         # it first take s=A 
      for j in range(1,n):
          j1=i+j
          s=s+string[j1]                   # (i=  1, s=A+B=>AB         2)s=AB+C=>ABC) -----(  i=2 ,s=B+C= BC            j=3,S=BC+D=BCD)
      
      ''' check substring is present or not   '''
      for k in range(l):
          if(s[k]!=findstr[k]):
            break
          else:
              if(k==l-1):
                  count+=1
      s=' '     ''' empty string '''
    
print(count)     
     
     
                    
      
    
