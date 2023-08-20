                                                                                                  ''' TCS   QUSTIONS'''  #19  JAN 2023
                                                        ''' INPUT                                                                                                                             OUTPUT
                                                              4                                                                                                                                   Count  Of  Valid   String=2
                                                              Hello Good Morning                                                                                           Count  Of   Inalid   String=2
                                                              abcd123Fghy
                                                              India
                                                              progoti.c                                                                                                                         '''                                          

def string(l):
    v,Iv=0,0
    for i in l:
        n=len(i)
        if(i.isidentifier()):
            v+=1
        else:
            Iv+=1
    print("Count Of Valid String=",v)
    print("Count Of  Invalid String=",Iv)
        
                 
a=int(input())
l=[]
for i in range(a):
    l.append(input())

string(l)    
    
