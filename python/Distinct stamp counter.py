'''  Count the total number of distinct country stamps in collection
        Input                             Ouput
       ---------                        ----------     
        7                                   5           
        UK
        China
        USA
        France
        New Zealand
        UK                                                  '''
#code
N=int(input())
l=[]
for i in range(N):
    l.append(input())
l=list(set(l))
print(len(l))    
