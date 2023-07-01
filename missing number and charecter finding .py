
'''input                             output
 -----------                     -------------
   23467ghjd9                    [0,1,5,8]
                                 [a,b,c,,e,f,i,k,l,m,n,o,p,q,r,s,t,u,v,w,x.y,z]                           
                                 '''
def num(n):
    n.sort()
    num=[0,1,2,3,4,5,6,7,8,9]
    n1=[]
  
        
    for i in range(len(num)):
        for j in range(len(n)):
            if(num[i]==n[j]):
                break
            else:
                if(j==(len(n)-1)):
                    n1.append(num[i])
                
    print(n1)            
    
def alpas(f):
    f.sort()
    f1=[]
    
    for i in range(97,122+1):
        for j in range(len(f)):
            if(i==ord(f[j])):
                break
            else:
                if(j==(len(f)-1)):
                    f1.append(chr(i))
    print(f1)                
        
    
     
      

#split integer and alphapets
k=input()

f=[]
n=[]
for i in range(len(k)):
    if(48<=(ord(k[i])) and 57>=ord(k[i])):
        l=int(k[i])
        n.append(l)
    elif(97<=(ord(k[i])) and 122>=ord(k[i])):
        f.append(k[i])
        
num(n,f)        
alpas(f)
